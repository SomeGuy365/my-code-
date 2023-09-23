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
            <div className="nasa-contain" style={{backgroundImage: `url(${prop.url})`,backgroundPosition: 'left', backgroundSize: 'cover'}}>
                <span className="nasatext">
                    <span className="nasatitle">
                        {prop.title}
                    </span><br />
                    {prop.explanation}
                </span>
            </div>
        </div>

    )
}

export default card;