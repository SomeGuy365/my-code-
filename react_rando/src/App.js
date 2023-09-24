import './App.css';
import { useState,useEffect } from 'react';
import Homecard from './Homecard'

function App() {
  const [nav, setnav] = useState()
  const [nasa, setnasa] = useState([])
  const NASA_API = 'aNPUGKBJgz847fa29nRAkUe01yQlQeCl5Nb1EbIe'

  function fectchNasa() {
    fetch(`https://api.nasa.gov/planetary/apod?api_key=${NASA_API}`)
    .then(response => response.json())
    .then(data => setnasa(data))
  }

  useEffect(()=>setnav(1),[])
  useEffect(fectchNasa,[])



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
            </div>
          ) :
            console.log()
        }
        {nav === 2
          ? (
            <div className='two-home'>two</div>
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
