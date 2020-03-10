import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import CoursesList from "./CoursesList";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
  state = {
    courses: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCourses = () => {
    axios.get(API_URL).then(res => this.setState({ courses: res.data }));
  };

  resetState = () => {
    this.getCourses();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <CoursesList
              courses={this.state.courses}
              resetState={this.resetState}
            />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;