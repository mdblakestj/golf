import React, { Component } from "react";
import axios from "axios";

import ReactMapGL, {
  Marker,
  Popup,
  NavigationControl,
  FullscreenControl
} from "react-map-gl";

// import ControlPanel from "./control-panel";
import CityPin from "./city-pin";
import CityInfo from "./city-info";

const TOKEN = process.env.REACT_APP_MAPBOX_KEY;

export default class Map extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewport: {
        width: 1000,
        height: 400,
        latitude: 37.7577,
        longitude: -100.0,
        zoom: 8
      },
      popupInfo: null,
      holes: []
    };
  }

  componentDidMount() {
    this.getHoles();
  }

  getHoles = () => {
    axios
      .get("http://127.0.0.1:8000/api/hole/")
      .then(res => {
        this.setState({ holes: res.data });
        console.log(this.state);
      })
      .catch(err => {
        console.log(err);
      });
  };

  _updateViewport = viewport => {
    this.setState({ viewport });
  };

  _renderCityMarker = (city, index) => {
    return (
      <Marker longitude={Number(city.lng)} latitude={Number(city.lat)}>
        <CityPin size={20} onClick={() => this.setState({ popupInfo: city })} />
      </Marker>
    );
  };

  _renderPopup() {
    const { popupInfo } = this.state;

    return (
      popupInfo && (
        <Popup
          tipSize={5}
          anchor="top"
          longitude={Number(popupInfo.lng)}
          latitude={Number(popupInfo.lat)}
          closeOnClick={false}
          onClose={() => this.setState({ popupInfo: null })}
        >
          <CityInfo info={popupInfo} />
        </Popup>
      )
    );
  }
  mapboxApiAccessToken = { TOKEN };
  render() {
    const { viewport } = this.state;

    return (
      <div style={{ align: "center" }}>
        <ReactMapGL
          {...viewport}
          onViewportChange={this._updateViewport}
          mapboxApiAccessToken={TOKEN}
        >
          {this.state.holes.map(this._renderCityMarker)}
          {this._renderPopup()}
        </ReactMapGL>
      </div>
    );
  }
}
