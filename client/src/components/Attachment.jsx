import React, { Component } from "react";
import axios from "axios";

export default class Attachment extends Component {
  state = {
    attachment: [],
    newAttachment: {
      name: ""
    }
  };
  updatePage = () => {
    axios.get("/api/v1/attachment").then(res => {
      this.setState({ attachment: res.data });
      console.log(this.state.attachment);
    });
  };
  componentDidMount() {
    this.updatePage();
  }

  render() {
    let attachment = this.state.attachment.map(attachment => {
      return (
        <div>
          <h1>{attachment.name}</h1>
        </div>
      );
    });
    return attachment;
  }
}
