import React from "react";
import { NavLink } from "react-router-dom";
import './Navbar.css'

function Navbar() {
    return (
        <div className="nav">
            <NavLink to="/Home" activeStyle>
                Blogs
            </NavLink>
            <NavLink to="/Second" activeStyle>
                Blogs
            </NavLink>
            <NavLink to="/homecard" activeStyle>
                uhhhhhh
            </NavLink>
        </div>
    )
}

export default Navbar