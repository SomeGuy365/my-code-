import React from "react";
import './App.css'

const card = (props) => {

    {console.log(props.fore)}

    return (
        <div>
            <div className="two-home">
                <div className="two-toptext">
                    Weather
                </div>
                <div className="two-toptitle">
                    Say Hello to your weather
                </div>
                <span style={{fontSize: 14,marginLeft: 10}}>
                    I dont know what to put here
                </span>
            </div>
            <div className='weather-container'>
            </div>
        </div>
    )
}

export default card;