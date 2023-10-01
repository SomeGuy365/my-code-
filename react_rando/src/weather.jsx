import React from "react";
import { useState, useEffect } from "react";
import './App.css'

const Card = (props) => {
    let array = Array.from(props.fore)
    const [text, settext] = useState()

    function fetchweather() {
        fetch(`http://api.weatherapi.com/v1/forecast.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&days=7&aqi=no&alerts=no1`)
        .then(response => response.json())
        .then(weather => settext(weather.current.condition.text))

        console.log(text)
    }

    useEffect(fetchweather, [props])

    return (
        <div className="two-container">
            <div className="two-home">
                <div className="two-toptext">
                    Weather
                </div>
                <div className="two-toptitle">
                    The weather is {props.curr.temp_c}°C
                </div>
                <span style={{fontSize: 14,marginLeft: 16}}>
                    And it is {text}
                </span>
            </div>
            <div className='weather-container'>
            {array.map((e) => (
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
            ))}
            </div>
        </div>
    )
}

export default Card;