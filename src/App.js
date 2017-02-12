import React, { Component } from 'react';
import './App.css';
import "bulma/css/bulma.css"
import "./workouts.json"

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            weeks: ["a", "b"]
        };
    }

    render() {
        return (
            <div className="columns">
                {this.state.weeks.map(week => {
                    return <div className="column">HELLO {week}</div>
                })}
            </div>
        );
    }

}

export default App;
