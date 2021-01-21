import React, { Component } from "react";
import Movies from "./components/movie"

class App extends Component {
  state = {
    movies: [],
  };

  componentDidMount() {
    this.getMovies();
  }

  getMovies() {
    fetch(`http://127.0.0.1:5000/movies`)
      .then(response => response.json())
      .then(result => this.setState({ movies: result }))
      .then(result => console.log(this.state.movies))
      .catch(err => console.log(err));
  }


  render() {

    return (
      <div className="App">
        <h4>
          <Movies
            movies={this.state.movies}
          />
        </h4>
      </div>
    );
  }
}

export default App;