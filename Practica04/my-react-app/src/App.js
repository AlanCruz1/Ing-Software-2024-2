import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Expenses from './components/Expenses/Expenses';
function App(){
  
  const expensesList = [
    {
      concept:"Car wash",
      amount: 65
    },
    {
      concept: "Pet's bath",
      amount: 100
    },
    {
      concept: "Gamer keyboard",
      amount: 650
    }
  ];


    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
          <Expenses items ={expensesList} />
        </p>
      </div>
    );
}

export default App;
