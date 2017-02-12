import React, { Component } from 'react';
import './App.css';
import "bulma/css/bulma.css"
import "./workouts.json"

class App extends Component {
  render() {
    return (
        <div className="columns">
            <div className="column">
                Hello worlds
            </div>
            <div className="column">
                <a className="button is-primary">Primary</a>
            </div>
        </div>
    );
  }
}

export default App;
