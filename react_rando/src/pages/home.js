import './home.css';
import { useState,useEffect } from 'react';
import Homecard from './Homecard'
import WeatherCard from './weather'
import homeicon from './pics/home2.svg'
import weathericon from './pics/weather.svg'
import Filmcard from './filmcard'
import { NavLink } from 'react-router-dom';

function Home() {
  const [user, setuser] = useState()
  const [pass, setpass] = useState()
  const [nav, setnav] = useState()
  const [nasa, setnasa] = useState([])
  const [weather, setweather] = useState({})
  const [foreweth, setforeweth] = useState([])
  const NASA_API = 'aNPUGKBJgz847fa29nRAkUe01yQlQeCl5Nb1EbIe'
  const API_URL = 'http://www.omdbapi.com/?i=tt3896198&apikey=30e91ad4'
  const [movies, setmovies] = useState([])
  const [search, setsearch] = useState('')

  const searchmovies = async (title) => {
    const response = await fetch(`${API_URL}&i=${title}`);
    const data = await response.json();

    setmovies(data.Search)
  } 

  const filmplot = async (title) => {
    const response = await fetch(`${API_URL}&t=${title}`);
    const data = await response.json();

    console.log(data.Search)
  } 

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
            <div /*onClick={()=>setnav(3)}*/ className='nav-border-top'>
                <NavLink to="/second" activeStyle>
                        test
                </NavLink>
            </div>
          </div>
          <div onClick={()=>setnav(4)} className='nav-border-bottom'>
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
            <input 
            placeholder='Film search'
            value={search}
            onChange={(e)=> setsearch(e.target.value)}
            />
            <button style={{height: 18}} onClick={() => searchmovies(search)} />
            {
              movies?.length > 0
               ? (
                <div className='film-box'>
                  {movies.map((movie) => (
                    <div className='film-container'>
                      <img src={movie.Poster} />
                      {movie.Title}
                    </div>
                  ))}
                </div>
               ) : (
                <div>Search for something!!!!</div>
               )
    
            }
            
          </div>
          ) :
            console.log()
        }
      </div>
    </div>
  );
}

export default Home;
