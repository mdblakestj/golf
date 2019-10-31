import React from "react";
import "./App.css";
import HoleMap from "./components/HoleMap";
import styled from "styled-components";
import List from "./components/List";
import HoleForm from "./components/HoleForm";
import Button from "@kiwicom/orbit-components/lib/Alert";

const Title = styled.h1`
  color: red;
  font-size 155px`;

const Hats = styled.button`
  color: red;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid red;
  border-radius: 3px;
`;
function App() {
  return (
    <div>
      <Title>Guerilla Golf</Title>
      <HoleMap />
      <Hats>Play Hole</Hats>
      <Hats>Play Course</Hats>
    </div>
  );
}

export default App;
