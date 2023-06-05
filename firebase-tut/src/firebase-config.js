// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from 'firebase/auth';
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBI2CzLmqXzvPcY0jn6VeMDIsr-KGp6WsU",
  authDomain: "thing-db0f7.firebaseapp.com",
  projectId: "thing-db0f7",
  storageBucket: "thing-db0f7.appspot.com",
  messagingSenderId: "547660272890",
  appId: "1:547660272890:web:642ff9b85e1d0674422543",
  measurementId: "G-227HXXHP79"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

export const auth = getAuth(app)