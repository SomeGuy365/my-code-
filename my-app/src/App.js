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
        <nav className='navbar'>
          <div onClick={onclick}>
            home
          </div>
          <div>
            podcasts
          </div>
          <div>
            for you
          </div>
          <div>
            library
          </div>
        </nav>
      </div>
    );
}

export default App;
