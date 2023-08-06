import React from "react";

const Pokecard = ({pokemon}) => {
    return (
        <div>
            <h1 className='container'>
                {pokemon.name}<br />
                <img src={pokemon.sprites.versions["generation-ii"].crystal.front_default} alt="poke" />
            </h1>
        </div>
    )
}

export default Pokecard;