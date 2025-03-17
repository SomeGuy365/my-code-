import React from "react";
import { useState, useEffect } from "react";
import './weather.css'

const Card = ({props}) => {
    //let array = Array.from(props.fore)
    const [weather, setweather] = useState(null)


    function fetchweather() {
        fetch(`http://api.weatherapi.com/v1/forecast.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&days=7&aqi=no&alerts=no`)
        .then(response => response.json())
        .then(weather => setweather(weather))
        console.log(weather)

    }

    useEffect(()=>fetchweather(),[]) 

    return (
        <div className="two-container">
            <div className="two-home">
                <div className="two-toptext">
                    Weather
                </div>
                
                {weather ? (
                    <div>
                    <div className="two-toptitle">
                    The Temperature is {weather.current.temp_c}°C
                    </div>
                    <span style={{fontSize: 14}}>
                        And it is {weather.current.condition.text}
                    </span>
                </div> ): (<div>Loading</div>)}

                
            </div>
            <div className='weather-container'>
            {weather ?
                weather.forecast.forecastday.map((e) => (
                    <div className="weather">
                        <div className="weather-date">
                            {e.date}
                        </div>
                        <img src={e.day.condition.icon} />
                        <div className="weather-temp">
                            Average: {e.day.avgtemp_c}°C
                        </div>
                        <span className="weather-temprange">
                            Range: {e.day.mintemp_c} - {e.day.maxtemp_c}°C
                        </span>
                    </div>
                )) : (<div>uh oh</div>)}
            </div>
            
        </div>
    )
}

export default Card;