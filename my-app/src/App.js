import logo from './logo.svg';
import './App.css';
import { ReactComponentElement } from 'react';

function App() {

  function onclick() {
    console.log('yay')
    return (
      <h1>yay</h1>
    )
  }

    return (
      <div className="App">
        <h1 onClick={onclick}>bruh</h1>
        <ul>
          <li>one</li>
          <li>two</li>
          <li>three</li>
        </ul>
      </div>
    );
}

export default App;
