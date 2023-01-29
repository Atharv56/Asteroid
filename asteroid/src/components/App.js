
import Signup from "./signup";

import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import React, { useEffect, useState } from "react";
import Login from "./login";
import Home from "./home";
import { auth } from "../firebase";
function App() {
  // const [userName, setUserName] = useState("")

  // useEffect(()=> {
  //   auth.onAuthStateChanged(user=>{
  //     if(user){
  //       setUserName(user.displayName)
  //     }else{
  //       setUserName("")
  //     }
  //     console.log(user)
  //   })
  // }, [])
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/login" element={<Login/>}/>
          <Route path="/" element={<Signup/>}/>
          <Route path="/home" element={<Home/>}/>
        </Routes>
      </Router>
    </div>
  
  )
}

export default App;
