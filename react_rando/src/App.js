import logo from './logo.svg';
import './App.css';
import { useState,useEffect } from 'react';

function App() {
  const [nav, setnav] = useState()

  useEffect(()=>setnav(1),[])

  return (
    <div className="App">
      <nav className='navbar'>
        <div onClick={()=>setnav(1)}>
          one
          {nav == 1
            ? (
                <div>
                  yay
                </div>
              ) : 
                console.log('nay')
            }
        </div>
        <div onClick={()=>setnav(2)}>
          two
          {nav == 2
            ? (
                <div>
                  yay
                </div>
              ) : 
                console.log('nay')
            }
        </div>
        <div onClick={()=>setnav(3)}>
          three
          {nav == 3
            ? (
                <div>
                  yay
                </div>
              ) : 
                console.log('nay')
            }
        </div>
      </nav>
    </div>
  );
}

export default App;
