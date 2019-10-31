import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import store from "./store/index";
import "./index.css";
import { addArticle } from "./actions/index";
import * as serviceWorker from "./serviceWorker";
import AppRouter from "./routers/AppRouter";

store.dispatch(
  addArticle({ title: "React Redux Tutorial for Beginners", id: 1 })
);

store.dispatch(
  addArticle({ title: "React Redux Tutorial for Beginners 2", id: 2 })
);

window.store = store;
window.addArticle = addArticle;

ReactDOM.render(
  <Provider store={store}>
    <AppRouter />
  </Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
