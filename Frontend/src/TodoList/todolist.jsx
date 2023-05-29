import {
  TextField,
  Button,
  Typography,
  Checkbox,
  List,
  ListItem,
  Container,
} from "@mui/material";
import { styled } from "@mui/system";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./todolist.css";

const Input = styled(TextField)(({ theme }) => ({
  width: "70%",
  marginBottom: theme.spacing(3),
}));

const AddButton = styled(Button)(({ theme }) => ({
  height: theme.spacing(5), // Adjust the height to your desired value
  marginBottom: theme.spacing(3),
  width: "40%",
}));

const MainContainer = styled(Container)({
  textAlign: "center",
  marginTop: "100px",
});

const ListContainer = styled(List)({
  width: "80%",
  margin: "auto",
  display: "flex",
  justifyContent: "space-around",
  border: "1px solid light-gray",
  flexDirection: "column",
});

const Text = styled(Typography)({
  width: "70%",
});

const ListButtons = styled(Button)(({ theme }) => ({
  marginLeft: theme.spacing(1),
  fontSize: "0.8rem", // Adjust the font size to make the buttons smaller
  padding: theme.spacing(1), // Adjust the padding to make the buttons smaller
}));

const request = (method, endpoint, data, successFn) => {
  const token = localStorage.getItem("auth");
  fetch(`http://localhost:8000/todos${endpoint}`, {
    method: method,
    credentials: "include",
    headers: {
      Accept: "application/json",
      "Access-Control-Allow-Origin": "http://localhost:3000/",
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: data ? JSON.stringify(data) : null,
  })
    .then((response) => {
      if (response) return response.json();
    })
    .then(successFn)
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
};
function Todolist({ isLoggedIn }) {
  const [inputVal, setInputVal] = useState("");
  const [todos, setTodos] = useState([]);
  const [isEdited, setIsEdited] = useState(false);
  const [editTodo, setEditTodo] = useState({});
  const navigate = useNavigate();

  function loadTodos() {
    request("GET", "", null, (data) => {
      setTodos(data);
    });
  }

  console.log(todos);

  useEffect(() => {
    if (!isLoggedIn) {
      navigate("/login");
      return;
    }
    loadTodos();
  }, [isLoggedIn, navigate]);

  const onChange = (e) => {
    setInputVal(e.target.value);
  };

  const handleClick = () => {
    const todoData = {
      todo: inputVal,
    };
    request("POST", "", todoData, (data) => {
      console.log(data);
      loadTodos();
    });
    setInputVal("");
    setIsEdited(false);
  };

  async function onDelete(id) {
    const newTodos = todos.filter((todo) => todo.id !== id);
    request("DELETE", `/${id}`, null, (data) => {
      console.log(data);
    });
    setTodos(newTodos);
  }

  const handleDone = (id) => {
    let updatedTodo = null;
    const updated = todos.map((todo) => {
      if (todo.id === id) {
        todo.is_completed = !todo.is_completed;
        updatedTodo = todo;
      }
      return todo;
    });

    request("PUT", `/${id}`, updatedTodo, (data) => {
      console.log(data);
    });
    setTodos(updated);
  };

  const handleEdit = (id) => {
    setInputVal("");
    const newTodos = todos.filter((todo) => todo.id !== id);
    const editVal = todos.find((todo) => todo.id === id);
    setInputVal(editVal.todo);
    setTodos(newTodos);
    setIsEdited(true);
    setEditTodo(editVal);
  };

  const editTaskOnClick = () => {
    editTodo.todo = inputVal;
    request("PUT", `/${editTodo.id}`, editTodo, (data) => {
      console.log(data);
      setTodos([...todos, editTodo]);
    });
    setIsEdited(false);
    setInputVal("");
  };

  return (
    <div className="todolist">
      <MainContainer>
        <Input
          variant="outlined"
          onChange={onChange}
          label="Type your task"
          value={inputVal}
        />
        <AddButton
          size="large"
          variant={isEdited ? "outlined" : "contained"}
          color="primary"
          onClick={isEdited ? editTaskOnClick : handleClick}
          disabled={!inputVal}
        >
          {isEdited ? "Edit Task" : "Add Task"}
        </AddButton>
        <ListContainer>
          {todos.map((todo) => (
            <ListItem key={todo.id} divider>
              <Checkbox
                onClick={() => handleDone(todo.id)}
                checked={todo.is_completed}
              />
              <Text style={{ color: todo.is_completed ? "green" : "" }}>
                {todo.todo}
              </Text>
              <ListButtons
                sx={{ width: "40%" }}
                onClick={() => handleEdit(todo.id)}
                variant="contained"
              >
                Edit
              </ListButtons>
              <ListButtons
                onClick={() => onDelete(todo.id)}
                sx={{ width: "40%" }}
                color="secondary"
                variant="contained"
              >
                Delete
              </ListButtons>
            </ListItem>
          ))}
        </ListContainer>
      </MainContainer>
    </div>
  );
}

export default Todolist;
