import logo from './logo.svg';
import './App.css';
import { ReactComponentElement } from 'react';

function App() {
  this.state = {msg: false}

  function onclick() {
    this.state = {msg: true}
    console.log('yay')
  }


  if (this.state.msg) {
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
  else {
    return (
      <h1>horray</h1>
    )
  }
}

export default App;
