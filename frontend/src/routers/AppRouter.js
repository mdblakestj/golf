import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import App from "../App";
import List from "../components/List";
import Form from "../components/PlayerSelect";

const AppRouter = () => (
  <Router>
    <div>
      <Switch>
        <Route path="/home" component={App} />
        <Route path="/list" component={List} />
        <Route path="/playerform" component={Form} />
      </Switch>
    </div>
  </Router>
);

export default AppRouter;
