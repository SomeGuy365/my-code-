import { useState, useEffect } from 'react';
import './App.css';
import Pokecard from './pokecard';


function App() {
  const [count, setcount] = useState();
  const [pokemon, setpokemon] = useState([]);
  const [search, setsearch] = useState();


  function fetchKantoPokemon(){
    setpokemon('')

    fetch(`https://pokeapi.co/api/v2/pokemon/${search}`)
    .then(response => response.json())
    .then(allpokemon => setpokemon(allpokemon))
    console.log(pokemon)
  }

  useEffect(() => {
    setcount(0)
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

    </div>
  );
}

export default App;
