import React, { Component } from "react";
import axios from "axios";
import { connect } from "react-redux";
import { getData } from "../actions/index";

import ReactMapGL, {
  Marker,
  Popup
  // NavigationControl,
  // FullscreenControl
} from "react-map-gl";

// import ControlPanel from "./control-panel";
import CityPin from "./city-pin";
import CityInfo from "./city-info";

const TOKEN = process.env.REACT_APP_MAPBOX_KEY;

class Map extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewport: {
        width: 1000,
        height: 400,
        latitude: 42.379659,
        longitude: -71.096053,
        zoom: 15
      },
      popupInfo: null,
      holes: []
    };
  }

  componentDidMount() {
    this.props.getData();
  }

  getHoles = () => {
    axios
      .get("http://127.0.0.1:8000/api/hole/")
      .then(res => {
        this.setState({ holes: res.data });
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
      <Marker
        key={city.id}
        longitude={Number(city.lng)}
        latitude={Number(city.lat)}
      >
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
          {this.props.holes.map(this._renderCityMarker)}
          {this._renderPopup()}
        </ReactMapGL>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    holes: state.remoteArticles.slice(0, 10)
  };
}
export default connect(
  mapStateToProps,
  { getData }
)(Map);
