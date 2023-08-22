import { useState, useEffect } from 'react';
import './App.css';
import Pokecard from './pokecard';


function App() {
  const NASA_API = 'aNPUGKBJgz847fa29nRAkUe01yQlQeCl5Nb1EbIe'

  const [count, setcount] = useState();
  const [pokemon, setpokemon] = useState([]);
  const [nasa, setnasa] = useState([]);
  const [nasasearch, setnasasearch] = useState([])
  const [search, setsearch] = useState();
  const [nsearch, setnsearch] = useState();

  function fetchKantoPokemon(){
    setpokemon('')

    fetch(`https://pokeapi.co/api/v2/pokemon/${search}`)
    .then(response => response.json())
    .then(allpokemon => setpokemon(allpokemon))
    console.log(pokemon)
  }

  function fectchNasa() {
    fetch(`https://api.nasa.gov/planetary/apod?api_key=${NASA_API}`)
    .then(response => response.json())
    .then(data => setnasa(data))
  }

  function searchNasa() {
    fetch(`https://images-api.nasa.gov/search?q=${nsearch}`)
    .then(response => response.json())
    .then(data => setnasasearch(data.collection.items))

    console.log(nasasearch)
  }


  useEffect(() => {
    setcount(0);
  },[])

  return (
    <div className="App">
      <button onClick={() => setcount(count+1)}>+</button>
      <h1>{count}</h1>
      <button onClick={() => setcount(count-1)}>-</button>
      <input 
      placeholder='Search'
      value={search}
      onChange={(e) => setsearch(e.target.value)}
      />
      <button onClick={fetchKantoPokemon}>Poekemon</button>

      {
        pokemon.name?.length > 0
          ? (
            <Pokecard pokemon = {pokemon} />
          ) : (
            <div className='empty'>
              <h2>No Pokemon Found</h2>
            </div>
          )
      }

      <hr />
      <button onClick={fectchNasa}>Nasa</button>
      <input 
        placeholder='Search in Nasa'
        value={nsearch}
        onChange={(e) => setnsearch(e.target.value)}
      />
      <button onClick={searchNasa}>Search Nasa</button>

      {
        nasa.title?.length > 0
          ? (
            <div>
              {nasa.title}
              <div className='nasacontain'>
                <img src={nasa.url} className='nasaimg'/>
                <p className='nasainfo'>
                  {nasa.explanation}
                </p>
              </div>
            </div>
          ) : (
            <div className='empty'>
              <h2>No nasa</h2>
            </div>
          )
      }

      {
        nasasearch.length > 0
          ? 
            (
              nasasearch.map((e) => (
                <div>
                  <div>{e.data[0].title}</div>
                  <div>{e.data[0].description}</div>
                  <div>
                    {e.data[0].media_type == 'image'
                     ? (
                      <div>
                        <div>imgae</div>
                        {e.href}
                      </div>
                    ) : 
                      console.log(e)
                    }
                  </div>
                </div>
              ))
            )
           : (
            <div className='empty'>
              <h2>No Pokemon Found</h2>
            </div>
          )
      }


    </div>
  );
}

export default App;
