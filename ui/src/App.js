import React from 'react';
import SearchBar from './components/SearchBar';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import './App.css';

function App() {
  return (
    <Container className="App">
      <Row className="App-header">
        <h1 className="App-title">Promot<span style={{color:"#c14953"}}>ED</span></h1>
        <SearchBar/>
      </Row>
    </Container>
  );
}

export default App;
