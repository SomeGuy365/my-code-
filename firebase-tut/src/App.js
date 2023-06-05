import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { createUserWithEmailAndPassword, onAuthStateChanged,signOut, signInWithEmailAndPassword} from 'firebase/auth'
import { auth } from './firebase-config'

function App() {

  const [registerEmail, setRegisteremail] = useState('')
  const [registerPass, setRegisterpass] = useState('')
  const [loginEmail, setLoginemail] = useState('')
  const [loginPass, setLoginpass] = useState('')

  const [user, setUser] = useState({})
  onAuthStateChanged(auth, (currentUser) => {
    setUser(currentUser)
  })

  const register = async () => {
    try{
      const user = await createUserWithEmailAndPassword(auth, registerEmail, registerPass)
      console.log(user)
    } catch (error) {
      console.log(error.message)
    }
  }

  const logout = async () => {
    await signOut(auth)
  }

  const login = async () => {
    try{
      const user = await signInWithEmailAndPassword(auth, loginEmail, loginPass)
      console.log(user)
    } catch (error) {
      console.log(error.message)
    }
  }



  return (
    <div className="App">
      Create
      <div>
        User:
        <input onChange={(event) => {setRegisteremail(event.target.value)}}/>
      </div>
      <div>
        Pass:
        <input onChange={(event) => {setRegisterpass(event.target.value)}}/>
      </div>
      <button onClick={register}>
        Create
      </button><br />
      Sign in:
      <div>
        User:
        <input onChange={(event) => {setLoginemail(event.target.value)}}/>
      </div>
      <div>
        Pass:
        <input onChange={(event) => {setLoginpass(event.target.value)}}/>
      </div>
      <button>
        Login
      </button><br />
      {loginEmail}
      <button onClick={logout}>
        Sign out
      </button>
    </div>
  );
}

export default App;
