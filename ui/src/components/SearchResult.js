import React, {Component} from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

class SearchResult extends Component {

  render() {
    return (
      <Container className="App-header">
        <h1 className="Result-title">Curriculum Result</h1>

        <Card border="primary" style={{ width: '24rem' }}>
          <Card.Header>edX</Card.Header>
          <Card.Body>
            <Card.Title>Machine Learning by Andrew NG</Card.Title>
            <Card.Text>
              This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition.
            </Card.Text>
          </Card.Body>
          <Card.Footer className="text-muted">Free</Card.Footer>
        </Card>
        <br />

        <Card border="primary" style={{ width: '24rem' }}>
          <Card.Header>Udemy</Card.Header>
          <Card.Body>
            <Card.Title>Deep Learning by Andrew NG</Card.Title>
            <Card.Text>
              In this course, you will learn the foundations of Deep Learning, understand how to build neural networks, and learn how to lead successful machine learning projects
            </Card.Text>
          </Card.Body>
          <Card.Footer className="text-muted">Free</Card.Footer>
        </Card>
        <br />

        <Card border="primary" style={{ width: '24rem' }}>
          <Card.Header>Coursera</Card.Header>
          <Card.Body>
            <Card.Title>Deep Reinforcement Learning</Card.Title>
            <Card.Text>
              Introductory course by Charles Isbell.
            </Card.Text>
          </Card.Body>
          <Card.Footer className="text-muted">Free</Card.Footer>
        </Card>
        <br />

      </Container>
    )
  }
}

export default SearchResult;
