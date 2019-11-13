import React, {Component} from 'react';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import '../styles/Filters.css';

class Filters extends Component {

  render(){
    return (
      <Container>
        <Row>
          <Col md={3} id="filters-title-col">
            <h1 id="filters-title">Promot<span style={{color:"#5da9e9"}}>Ed</span></h1>
          </Col>
        </Row>
        <Row>
        <Col md={{span:8, offset:3}}>
          <div>
            <h1>Goal: {this.props.query}</h1>
          </div>
        </Col>
        </Row>

      </Container>
    );
  }
}

export default Filters;
