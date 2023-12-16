import './App.css';
import { useState,useEffect } from 'react';
import Homecard from './Homecard'
import WeatherCard from './weather'
import homeicon from './pics/home2.svg'
import weathericon from './pics/weather.svg'

function App() {
  const [nav, setnav] = useState()
  const [nasa, setnasa] = useState([])
  const [weather, setweather] = useState({})
  const [foreweth, setforeweth] = useState([])
  const NASA_API = 'aNPUGKBJgz847fa29nRAkUe01yQlQeCl5Nb1EbIe'

  function fectchNasa() {
    fetch(`https://api.nasa.gov/planetary/apod?api_key=${NASA_API}`)
    .then(response => response.json())
    .then(data => setnasa(data))
  }

  function fetchcurrweather() {
    fetch(`http://api.weatherapi.com/v1/forecast.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&days=7&aqi=no&alerts=no1`)
    .then(response => response.json())
    .then(weather => setweather(weather.forecast.forecastday))
  }

  function fetchweather() {
    fetch(`http://api.weatherapi.com/v1/forecast.json?key=ea0c3ac899f343c1b5e173401232509&q=Bristol&days=7&aqi=no&alerts=no1`)
    .then(response => response.json())
    .then(weather => setforeweth(weather.current))
  }

  useEffect(()=>setnav(1),[])
  useEffect(fectchNasa,[])
  useEffect(fetchweather,[nav])
  useEffect(fetchcurrweather,[nav])



  return (
    <div className="App">
      <nav className='navbar'>
        <div className='nav-border'>
          <div className='nav-border-one'>
            <div onClick={()=>setnav(1)} className='nav-border-top'>
              <img src={homeicon} className='home-icon' />
            </div>
            <div onClick={()=>setnav(2)} className='nav-border-top'>
              <img src={weathericon} className='weather-icon' />
            </div>
            <div onClick={()=>setnav(4)} className='nav-border-top'>
              acc
            </div>
          </div>
          <div onClick={()=>setnav(3)} className='nav-border-bottom'>
            <div>
              Films
            </div>
          </div>
        </div>
      </nav>
      <div className='main'>
        {nav === 1
          ? (
            <div>
              <Homecard prop={nasa} />
            </div>
          ) :
            console.log()
        }
        {nav === 2
          ? (
            <WeatherCard curr={foreweth} fore={weather} />
          ) :
            console.log()
        }
        {nav === 3
          ? (
            <div className='three-home'>three</div>
          ) :
            console.log()
        }
        {nav === 4
          ? (
            <div className='acc-container'>
              life
            </div>
          ) :
            console.log()
        }
      </div>
    </div>
  );
}

export default App;
