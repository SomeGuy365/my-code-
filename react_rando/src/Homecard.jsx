import React from "react";
import './App.css'

const card = ({prop}) => {
    return (
        <div>
            <div className="one-home">
                <span className="one-toptext">
                    Home
                </span>
                <div className="one-toptitle">
                    Welcome Home
                </div>
                <span style={{fontSize: 14}}>
                    Your hub for whatever this is!
                </span>
            </div>
            <div className="nasa-contain" style={{background: prop.url}}>
                <img src={prop.url} className='nasaimg'/>
                {prop.explanation}
            </div>
        </div>

    )
}

export default card;