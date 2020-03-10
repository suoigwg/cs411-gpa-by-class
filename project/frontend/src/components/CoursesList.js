import React, { Component } from "react";
import { Table } from "reactstrap";


class CoursesList extends Component {
  render() {
    const courses = this.props.courses;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Subject</th>
            <th>Number</th>
            <th>Title</th>
          </tr>
        </thead>
        <tbody>
          {!courses || courses.length <= 0 ? (
            <tr>
              <td colSpan="3" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            courses.map(course => (
              <tr key={course.pk}>
                <td>{course.subject}</td>
                <td>{course.number}</td>
                <td>{course.title}</td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default CoursesList;