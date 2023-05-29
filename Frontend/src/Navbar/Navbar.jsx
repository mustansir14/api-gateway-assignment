import { Link } from "react-router-dom";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import "./Navbar.css";

export default function Navbar({ isLoggedIn, setIsloggedIn }) {
  const handleLogout = () => {
    // Perform logout actions here (e.g., clearing local storage, redirecting to login)
    localStorage.removeItem("auth");
    setIsloggedIn(false);
    navigate("/");
  };

  const navigate = useNavigate();
  return (
    <div className="navbar">
      <div>
        <Link to="/news">News</Link>
        <Link to="/todolist">Todos</Link>
      </div>
      <div>
        {isLoggedIn ? (
          <Button
            variant="contained"
            color="error"
            sx={{ width: "100px", height: "30px" }}
            onClick={handleLogout}
          >
            Logout
          </Button>
        ) : (
          <>
            <Link to="/signup">Signup</Link>
            <Link to="/login">Login</Link>
          </>
        )}
      </div>
    </div>
  );
}
