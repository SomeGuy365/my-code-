import './App.css';
import searchicon from './search.svg'
import { useState, useEffect } from 'react';
import Moviecard from './moviecard';

//30e91ad4
const API_URL = 'http://www.omdbapi.com?apikey=30e91ad4'

const movie1 = {
  "Title": "Batman Begins",
  "Year": "2005",
  "imdbID": "tt0372784",
  "Type": "movie",
  "Poster": "https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"
}


function App() {
  const [movies,setmovies] = useState([]);
  const [search,setsearch] = useState('');

  const searchmovies = async (title) => {
    const response = await fetch(`${API_URL}&s=${title}`);
    const data = await response.json();

    setmovies(data.Search)
  } 

  useEffect(() => {
    searchmovies('Batman');
  }, [])

  return (
    <div className="app">
      <h1>MovieLand</h1>

      <div className='search'>
        <input
          placeholder='Search for movies'
          value={search}
          onChange={(e) => setsearch(e.target.value)}
        />
        <img src={searchicon} alt='search' onClick={() => searchmovies(search)} />
      </div> 

      {
        movies?.length > 0
          ? (
            <div className='container'>
              {movies.map((movie) => (
                <Moviecard movie1={movie} />
              ))}
            </div>
          ) : (
            <div className='empty'>
              <h2>No Movies Found</h2>
            </div>
          )
      }

    </div>
  );
}

export default App;
