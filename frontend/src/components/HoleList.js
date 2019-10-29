import React, { Component } from "react";
import axios from "axios";

export default class HoleList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      list: []
    };
  }

  componentDidMount() {
    this.getHoles();
  }

  getHoles = () => {
    axios
      .get("http://127.0.0.1:8000/api/hole/")
      .then(res => {
        this.setState({ list: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  };

  render() {
    return (
      <div>
        {console.log(this.state)}
        {this.state.list.map(item => (
          <div key={item.id}>
            <h1>{item.name}</h1>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    );
  }
}
