import React, { Component } from "react";
import { connect } from "react-redux";
import { addArticle } from "../actions/index";

function mapDispatchToProps(dispatch) {
  return {
    addArticle: article => dispatch(addArticle(article))
  };
}

class ConnectedForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      selected: false,
      players: 0,
      options: [],
      player1: "",
      player2: "",
      player3: "",
      player4: ""
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.id]: event.target.value });
  }
  handleForm(event) {
    console.log(event.target.id);
    this.setState({ [`player${event.target.id}`]: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
    const { title } = this.state;
    this.props.addArticle({ title });
    this.setState({ title });
  }
  render() {
    const { title, player1, player2, player3, player4 } = this.state;
    return (
      <div>
        <h1>How Many Players?</h1>
        <h1>{player1}</h1>
        <select
          onChange={e => {
            var players = e.target.value;
            this.setState(() => ({
              options: Array.from({ length: players }, (v, k) => k + 1)
            }));
            this.setState(() => ({ selected: true }));
          }}
        >
          <option>Select number of players</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
        {this.state.selected &&
          this.state.options.map(el => (
            <form onSubmit={this.handleSubmit}>
              <div>
                <label htmlFor="title">{`Player ${el} Name`}</label>
                <input
                  type="text"
                  id={`player${el}`}
                  value={eval(`player${el}`)}
                  onChange={this.handleChange}
                />
              </div>
            </form>
          ))}
        <button type="submit" onClick={this.handleSubmit}>
          SAVE
        </button>
      </div>
    );
  }
}

const Form = connect(
  null,
  mapDispatchToProps
)(ConnectedForm);

export default Form;
