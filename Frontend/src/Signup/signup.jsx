import { useState } from "react";
import { Link } from "react-router-dom";
import { Box, AlertTitle, Alert } from "@mui/material";
import axios from "axios";
import "semantic-ui-css/semantic.min.css";
import "./signup.css";

function Signup() {
  const initialValues = { username: "", password: "" };
  const [formValues, setFormValues] = useState(initialValues);
  const [formErrors, setFormErrors] = useState({});
  const [isSubmit, setIsSubmit] = useState(false);
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === "username") {
      setUsername(value);
      localStorage.setItem("loggedInUserUsername", value);
    } else {
      setPassword(value);
    }
    setFormValues({ ...formValues, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validate(formValues);
    setFormErrors(errors);
    setIsSubmit(true);
    if (Object.keys(errors).length === 0) {
      try {
        const response = await axios.post(
          "http://localhost:8000/auth/signup",
          {
            username: username,
            password: password,
          },
          {
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            withCredentials: true,
          }
        );
        if (response.statusText === "OK") {
          localStorage.setItem(
            "auth",
            JSON.stringify(response.data.access_token)
          );
        }
        console.log(response.data.access_token);
      } catch (error) {
        console.log(error);
        if (
          (error.response && error.response.status === 400) ||
          error.response.status === 422
        ) {
          setFormErrors({ loginError: "Invalid username or password" });
        } else {
          setFormErrors({
            loginError: "An error occurred. Please try again later.",
          });
        }
      }
    }
  };

  const validate = (values) => {
    const errors = {};
    if (!values.username) {
      errors.username = "Username is required!";
    }
    if (!values.password) {
      errors.password = "Password is required!";
    }
    return errors;
  };
  return (
    <div className="Signup">
      <div className="container">
        <form onSubmit={handleSubmit}>
          <h1>User Signup</h1>
          <div className="ui divider"></div>
          <div className="ui form">
            <div className="field">
              <label>Username</label>
              <input
                type="text"
                name="username"
                placeholder="Username"
                value={formValues.username}
                onChange={handleChange}
              />
              {formErrors.username && <p>{formErrors.username}</p>}
            </div>
            <div className="field">
              <label>Password</label>
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={formValues.password}
                onChange={handleChange}
              />
              {formErrors.password && <p>{formErrors.password}</p>}
              <p>{formErrors.loginError}</p>
            </div>
            <button className="fluild ui button">Signup</button>
          </div>
          <div className="signupbox">
            Already a user? <Link to="/">Login!</Link>
          </div>
          <Box display="flex" justifyContent="center" mt="30px">
            {isSubmit && (
              <Alert severity="success">
                <AlertTitle>Success</AlertTitle>
                <strong>User Account Created!</strong>
              </Alert>
            )}
          </Box>
        </form>
      </div>
    </div>
  );
}
export default Signup;
