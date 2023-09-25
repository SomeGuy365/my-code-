import './App.css';
import { useState,useEffect } from 'react';
import Homecard from './Homecard'

function App() {
  const [nav, setnav] = useState()
  const [nasa, setnasa] = useState([])
  const [weather, setweather] = useState([])
  const NASA_API = 'aNPUGKBJgz847fa29nRAkUe01yQlQeCl5Nb1EbIe'
  const W_API = 'ea0c3ac899f343c1b5e173401232509'

  function fectchNasa() {
    fetch(`https://api.nasa.gov/planetary/apod?api_key=${NASA_API}`)
    .then(response => response.json())
    .then(data => setnasa(data))
  }

  function fetchweather() {
    fetch(`http://api.weatherapi.com/v1/forecast.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&days=7&aqi=no&alerts=no1`)
    .then(response => response.json())
    .then(weather => setweather(weather.forecast.forecastday))
    console.log(weather)
  }

  useEffect(()=>setnav(2),[])
  useEffect(fectchNasa,[])
  useEffect(fetchweather,[])



  return (
    <div className="App">
      <nav className='navbar'>
        <div className='nav-border'>
          <div onClick={()=>setnav(1)} className='nav-border-top'>
            One
          </div>
          <div onClick={()=>setnav(2)} className='nav-border-top'>
            Two
          </div>
          <div onClick={()=>setnav(3)} className='nav-border-top'>
            Three
          </div>
        </div>
      </nav>
      <div className='main'>
        {nav === 1
          ? (
            <div className='one-home'>
              <Homecard prop={nasa} />
              <div>
                hello
              </div>
            </div>
          ) :
            console.log(weather)
        }
        {nav === 2
          ? (
            <div>
              <div className='two-home'>
                two
              </div>
              <div className='weather-container'>
                {weather.map((e)=>(
                    <div className='weather'>
                      <span className='weather-date'>{e.date}</span>
                      <img src={e.day.condition.icon} />
                      <span className='weather-temp'>
                        {e.day.avgtemp_c}°C
                      </span><br />
                      <span className='weather-temprange'>
                      { e.day.maxtemp_c}-{e.day.mintemp_c}
                      </span>
                    </div>
                  ))}
              </div>
            </div>
          ) :
            console.log()
        }
        {nav === 3
          ? (
            <div className='three-home'>three</div>
          ) :
            console.log()
        }
      </div>
    </div>
  );
}

export default App;
