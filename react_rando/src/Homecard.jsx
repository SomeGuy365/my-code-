import React from "react";
import './App.css'
import ReactPlayer from 'react-player'

const card = ({prop}) => {
    return (
        <div className="one-container">
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
            <div className="flex-grid">
                <div className="flex-grid-one">
                    <span className="gridtext">
                        One
                    </span>
                </div>
                <div className="flex-grid-two">
                    <span className="gridtext">
                        Two
                    </span>
                </div>
                <div className="flex-grid-three">
                    <span className="gridtext">
                        Three
                    </span>
                </div>
                <div className="flex-grid-four">
                    <span className="gridtext" style={{color: 'grey'}}>
                        Four
                    </span>
                </div>
                <div className="flex-grid-five">
                    <span className="gridtext" style={{color: 'black'}}>
                        Five
                    </span>
                </div>
            </div>
            <div className="nasa-contain" style={{backgroundImage: `url(${prop.url})`,backgroundPosition: '25% 20%', backgroundSize: 'cover'}}>
                <span className="nasatext">
                    <span className="nasatitle">
                        {prop.title}
                    </span><br />
                    {prop.explanation}
                </span><br />
                {prop.media_type === 'video'
                    ? (
                        <div className="video">
                            <ReactPlayer url={prop.url} controls={false} muted={true} playing={true} width={400} height={250} />
                        </div>
                    ) : 
                    console.log()
                }
            </div>
        </div>

    )
}

export default card;