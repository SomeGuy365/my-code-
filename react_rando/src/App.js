import React from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Home from "./pages/home";
import Second from "./pages/second"
import Homecard from "./pages/Homecard/Homecard"
import Weather from "./pages/weather"
import { NavLink } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import './App.css'
 
function App() {
    return (
        <Router>
            <div className="ovcontainer">
                <Navbar />
                <Routes>
                    <Route path="/Home" element={<Homecard />} />
                    <Route path="/Second" element={<Weather />} />
                    <Route path="/Homecard" element={<Home />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;