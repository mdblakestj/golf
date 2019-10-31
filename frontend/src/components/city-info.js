import React, { PureComponent } from "react";

export default class CityInfo extends PureComponent {
  render() {
    const { info } = this.props;
    const displayName = `${info.name}, ${info.description}`;

    return (
      <div>
        <div>{displayName}</div>
      </div>
    );
  }
}

// <img width={240} src={info.image} />
