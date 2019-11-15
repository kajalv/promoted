import React, {Component} from 'react';
import SearchBar from './components/SearchBar';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';
import { withRouter } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';


class App extends Component {

  render() {
    return (
      <Container className="App" fluid={true}>
        <Row className="App-header">
          <h1 className="App-title">Promot<span style={{color:"#5da9e9"}}>ED</span></h1>
          <SearchBar/>
        </Row>
      </Container>
    );
  }
}

export default withRouter(App);
