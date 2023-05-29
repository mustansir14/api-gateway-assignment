import "./App.css";
import Login from "./Login/login";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Signup from "./Signup/signup";
import Todolist from "./TodoList/todolist";
import Navbar from "./Navbar/Navbar";
import News from "./News/News";
import { useState, useEffect } from "react";
function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    if (localStorage.getItem("auth")) {
      setIsLoggedIn(true);
    }
  }, []);

  return (
    <BrowserRouter>
      <div className="App">
        <Navbar isLoggedIn={isLoggedIn} setIsloggedIn={setIsLoggedIn} />
        <Routes>
          <Route path="/" element={<News />} />
          <Route path="/news" element={<News />} />
          <Route
            path="/login"
            element={<Login setIsLoggedIn={setIsLoggedIn} />}
          />
          <Route path="/signup" element={<Signup />} />
          <Route
            path="/todolist"
            element={<Todolist isLoggedIn={isLoggedIn} />}
          ></Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
