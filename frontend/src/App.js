import React from "react";
import "./App.css";
import HoleList from "./components/HoleList";

import HoleMap from "./components/HoleMap";
import styled from "styled-components";

const Title = styled.h1`
  color: red;
  font-size 155px`;
function App() {
  return (
    <div>
      <Title>Guerilla Golf</Title>
      <HoleMap />

    </div>
  );
}

export default App;
