import React from "react";
import { useState } from "react";

const Moviecard = ({ movie1 }) => {
    const API_URL = 'http://www.omdbapi.com?apikey=30e91ad4'
    const [movies, setmovies] = useState([])
    const [search, setsearch] = useState('')

    const searchmovies = async (title) => {
        const response = await fetch(`${API_URL}&i=${title}`);
        const data = await response.json();
    
        setmovies(data.Search)
      } 

    return (
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
    )
}

export default Moviecard;