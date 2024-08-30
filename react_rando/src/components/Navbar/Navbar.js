import React from "react";
import { NavLink } from "react-router-dom";
import './Navbar.css'
import homepic from "./home.svg"

function Navbar() {
    return (
        <div className="nav">
            <div className="sec-1">

                <div className="nav-home">
                    <NavLink to="/Home" style={{color:"white",textDecoration: "none"}} activeStyle>
                        <img src={homepic} className="homepic" />
                    </NavLink>
                </div>

                <div className="nav-weather">
                    <NavLink to="/Second" style={{color:"white",textDecoration: "none"}} activeStyle>
                        Blogs
                    </NavLink>
                </div>

                <div className="nav-three">
                    <NavLink to="/homecard" style={{color:"white",textDecoration: "none"}} activeStyle>
                        uh
                    </NavLink>
                </div>
                  
            </div>
        </div>
    )
}

export default Navbar