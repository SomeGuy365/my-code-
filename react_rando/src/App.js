import React from "react";
import {
    BrowserRouter as Router,
    Routes,
    Route,
} from "react-router-dom";
import Home from "./pages/home";
import Second from "./pages/second"
import { NavLink } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import './App.css'
 
function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/Home" element={<Home />} />
                <Route path="/Second" element={<Second />} />
            </Routes>
          
        </Router>
    );
}

/* FIX WEIRD SIZING CSS THINGY
  ORGANISE CSS (ITS AN ABSOLUTE MESS!!!!!!!!!!)
*/

export default App;