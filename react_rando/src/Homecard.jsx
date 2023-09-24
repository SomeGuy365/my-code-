import React from "react";
import './App.css'
import ReactPlayer from 'react-player'

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
            <div className="flex-grid">
                <div className="flex-grid-one">one</div>
                <div className="flex-grid-two">two</div>
                <div className="flex-grid-three">three</div>
                <div className="flex-grid-four">four</div>
                <div className="flex-grid-five">five</div>
            </div>
            <div className="nasa-contain" style={{backgroundImage: `url(${prop.url})`,backgroundPosition: 'left', backgroundSize: 'cover'}}>
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