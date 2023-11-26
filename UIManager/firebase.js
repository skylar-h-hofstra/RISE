// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBuPdyVpXV0puIz8C4esTceomOCIWMIXcg",
  authDomain: "rise-website-fe5b3.firebaseapp.com",
  projectId: "rise-website-fe5b3",
  storageBucket: "rise-website-fe5b3.appspot.com",
  messagingSenderId: "1085803537466",
  appId: "1:1085803537466:web:b603cd4babc1a14cd60103",
  measurementId: "G-ZS4LNZ9MKB"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);