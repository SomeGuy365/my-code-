import React from "react";
import { useState, useEffect } from "react";
import './weather.css'

const Card = ({props}) => {
    //let array = Array.from(props.fore)
    const [weather, setweather] = useState()
    const [array, setarray] = useState([])

    function fetchweather() {
        fetch(`http://api.weatherapi.com/v1/current.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&aqi=no`)
        .then(response => response.json())
        .then(weather => setweather(weather))

    }

    //TODO:Fix API rendering(GGGGRRRRAAAAAAAAA)

    return (
        <div className="two-container">
            yay
            <div className="two-home">
                <div className="two-toptext">
                    Weather
                </div>

                {weather != null ? (
                    <div>
                    <div className="two-toptitle">
                    The weather is {weather.current.temp_c}°C
                    </div>
                    <span style={{fontSize: 14,marginLeft: 16}}>
                        And it is {weather.current.condition.text}
                    </span>
                    </div> ): ()=>{fetchweather();setarray(Array.from(weather.forecast))}}

                
            </div>
            <div className='weather-container'>
            {array != null ?
                array.map((e) => (
                    <div className="weather">
                        <div className="weather-date">
                            {e.date}
                        </div>
                        <img src={e.day.condition.icon} />
                        <div className="weather-temp">
                            {e.day.avgtemp_c}
                        </div>
                        <span className="weather-temprange">
                            {e.day.mintemp_c}-{e.day.maxtemp_c}
                        </span>
                    </div>
                )) : (<div>uh oh</div>) }
            </div>
            
        </div>
    )
}

export default Card;