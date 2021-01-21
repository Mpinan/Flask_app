import React from "react";

const Movies = ({movies}) => {

    return ( 
    <div>
        {movies.map(movie => {
            return (
            <ul key={movie.film_id}>
                <li>
                    {movie.film_name}
                </li>
                <li>
                    {movie.director}
                </li>
                <li>
                    {movie.summary}
                </li>
            </ul>
            )})}
    </div> 
    );
}
 
export default Movies;