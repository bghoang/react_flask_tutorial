import React, { useEffect, useState } from "react";
import "./App.css";
import { Movies } from "./components/Movies";
import { MovieForm } from "./components/MovieForm";
import { Container } from "semantic-ui-react";

function App() {
  const [movies, setMovies] = useState([]);

  // Add "proxy": "http://localhost:5000/" to the end of package.json to avoid cors issue
  // Note: Start the react app first, then start the flask server to make the /movies call work
  useEffect(() => {
    fetch("/movies").then(response =>
      response.json().then(data => {
        setMovies(data.movies);
      })
    );
  }, []);

  return (
    <Container style={{ marginTop: 40 }}>
      <MovieForm
        onNewMovie={movie =>
          setMovies(currentMovies => [movie, ...currentMovies])
        }
      />
      <Movies movies={movies} />
    </Container>
  );
}

export default App;
