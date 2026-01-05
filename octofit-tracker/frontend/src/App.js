
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';
import logo from '../public/octofitapp-small.png';

function App() {
  return (
    <div className="App bg-light min-vh-100">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div className="container-fluid">
          <img src={logo} alt="Octofit Logo" className="app-logo" />
          <span className="navbar-brand mb-0 h1">Octofit Tracker</span>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <a className="nav-link" href="#users">Users</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#activities">Activities</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#teams">Teams</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#leaderboard">Leaderboard</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#workouts">Workouts</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <main className="container">
        <section id="users" className="mb-4">
          <Users />
        </section>
        <section id="activities" className="mb-4">
          <Activities />
        </section>
        <section id="teams" className="mb-4">
          <Teams />
        </section>
        <section id="leaderboard" className="mb-4">
          <Leaderboard />
        </section>
        <section id="workouts" className="mb-4">
          <Workouts />
        </section>
      </main>
    </div>
  );
}

export default App;
