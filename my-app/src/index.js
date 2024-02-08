import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
/*import Axios from 'axios';*/
import { useEffect, useState} from 'react'

const root = ReactDOM.createRoot(document.getElementById('root'));
let incorr = ''
let quote = ''

function Onclick(){
  const home = (<div>

    <nav className='nav-bar'>
      <div>
        Home
      </div>
      <div>
        About
      </div>
      <div>
        Projects
      </div>
      <div>
        Contact
      </div>
    </nav>

    <div className='border'>
      <div className='quote'>
        'Cool quote'<br />Author
      </div>
    </div>
    <div className='info-one'>
      info:)
    </div>
  </div>)

  let userfield = document.getElementById('user-imp')
  let userfield2 = userfield.value

  let passfield = document.getElementById('pass-imp')
  let passfield2 = passfield.value

  console.log(userfield2)
  if (userfield2 === JSON.parse(localStorage.getItem('user'))) {
    if (passfield2 === JSON.parse(localStorage.getItem('pass'))) {
      /*Axios.get('https://api.quotable.io/random').then((res)=>{
        console.log(res.data.content)
        Render(home)
      })*/
      Render(home)
    }
  }
}

function saveuser() {
  let userfield = document.getElementById('user-imp2')
  let userfield2 = userfield.value

  let passfield = document.getElementById('pass-imp2')
  let passfield2 = passfield.value

  localStorage.setItem('user',JSON.stringify(userfield2))
  localStorage.setItem('pass',JSON.stringify(passfield2))
}

function savenew() {
  root.render(
    <div className='login-border'>
      <div className='user'>
      User:
      <input type='text' className='user-imp' id='user-imp2' defaultValue={''}/>
    </div>
    <div className='pass'>
      Pass:
      <input type='text' className='pass-imp' id='pass-imp2' defaultValue={''}/>
    </div>
    <button onClick={saveuser} className='login-but'>Save</button>
  </div>
  )
}

function Render(code){
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(code);
}

const login = (
  <div className='login-border'>
    <div className='user'>
      User:
      <input type='text' className='user-imp' id='user-imp' defaultValue={''}/>
    </div>
    <div className='pass'>
      Pass:
      <input type='text' className='pass-imp' id='pass-imp' defaultValue={''}/>
    </div>
    <button onClick={Onclick} className='login-but'>Login</button>
    <div className='forget'>
      Forgot password?
      <button onClick={savenew}>Save new</button>
    </div>
  </div>
)

Render(login);