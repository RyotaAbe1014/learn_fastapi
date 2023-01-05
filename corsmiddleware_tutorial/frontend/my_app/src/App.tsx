import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
export const App = () =>  {
  const [message, setMessage] = useState("");

  const getMessage = () => {
    axios.get("http://localhost:8000")
    .then((res) => {
      console.log(res.data.message);
      setMessage(res.data.message);
    })
  };

  useEffect(() => {
    getMessage();
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {message}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
