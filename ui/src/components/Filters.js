import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';
import Slider from 'rc-slider';
import React, {Component} from 'react';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';

import '../styles/Filters.css';

const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);
const SliderWithTooltip = createSliderWithTooltip(Slider);

class Filters extends Component {

  constructor(props) {
    super(props);

    this.state = {
      minPrice: -1,
      maxPrice: -1,
      priceRange:[],
      durationRange:[],
      duration: -1,
      //level: this.props.location.query.includes("Senior") ? "Intermediate" : "Beginner"
      levels: new Set(["beginner"]),
      allData: [],
      currentData: []
    }
  }

  getDurationRange = () => {
    return {
      minD: 1,
      maxD: 12
    }
  }

  getPriceRange = () => {
    return {
      min: 0,
      max: 100
    };
  }

  updatePrice = (value) => {
    this.setState({
      minPrice: value[0],
      maxPrice: value[1]
    });
  }

  showLevelOptions = () => {
    this.setState({
      showLevelOptions: !this.state.showLevelOptions
    });
  }

  updateLevel = (event) => {
    let level = event.currentTarget.value;

    let levels = this.state.levels;
    if (levels.has(level)) {
      levels.delete(level);
    } else {
      levels.add(level);
    }
    this.setState({
      levels:levels
    });
  }

  updateDuration = (value) => {
    this.setState({
      duration: value
    });
  }

  mappedCourseLevel(level) {
    let allLevels = ["beginner", "intermediate", "advanced"]
    return allLevels[level];
  }

  getCurrentData() {
    let displayCount = 10;
    let currentData = [];
    for(let index = 0; index < this.state.allData.length; index++) {
      if (currentData.length >= displayCount)
        break;
      let course = this.state.allData[index];
      if (course.duration <= this.state.duration
            && course.price >= this.state.minPrice
            && course.price <= this.state.maxPrice
            && this.state.levels.has(this.mappedCourseLevel(course.level)))
          currentData.push(course);
    }
    return currentData;
  }

  componentDidMount() {
    let {min, max} = this.getPriceRange();
    let {minD, maxD} = this.getDurationRange();
    let url = 'http://localhost:5000/get_courses?job_title=' + this.props.location.query;
    //let url = 'http://localhost:5000/get_courses?job_title=' + "Software Developer";
    fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json())
            .then(data => {
                console.log(data);
                this.setState({
                  priceRange:[min, max],
                  minPrice: min,
                  maxPrice: max,
                  durationRange :[minD, maxD],
                  duration: maxD,
                  allData: data,
                });
            });
  }

  render() {
    let currentData = this.getCurrentData();
    let coursesDataJSX = currentData.map(course =>
      <Row>
        <Col md={{span:8, offset:2}} style={{marginTop: "2vmin"}}>
          <Card>
            <Card.Header>{course.site}</Card.Header>
            <Card.Body>
              <Card.Title>{course.title}</Card.Title>
              <Card.Text>
                Duration : {course.duration} weeks
              </Card.Text>
            </Card.Body>
            <Card.Footer className="text-muted">${course.price}</Card.Footer>
          </Card>
        </Col>
      </Row>
    );

    return (
      <Container id="filter-container" fluid={true}>
        <Row>
          <Col md={3} id="filters-title-col">
            <h2 id="filters-title">Promot<span style={{color:"#5da9e9"}}>Ed</span></h2>
          </Col>
        </Row>
        <Row style={{marginTop:"2vmin"}}>
          <Col md={{span:8, offset:2}}>
            <div id="goal-div">
              <h3>Curriculum for: <span style={{color:"#5da9e9"}}>{this.props.location.query}</span></h3>
            </div>

          </Col>
        </Row>
        <Row>
          <Col md={{span:8, offset:2}} id="filters">
            <Form style={{marginTop: "2vmin", width:"100%"}}>
              <Row style={{width:"100%"}}>
                <Col md={5} className="filter">
                 <p>Level:</p>

                 <Form.Check inline type="checkbox" value="beginner" label="Beginner" checked={this.state.levels.has("beginner")} onChange={this.updateLevel}/>
                 <Form.Check inline type="checkbox" value="intermediate" label="Intermediate" checked={this.state.levels.has("intermediate")} onChange={this.updateLevel}/>
                 <Form.Check inline type="checkbox" value="advanced" label="Advanced" checked={this.state.levels.has("advanced")} onChange={this.updateLevel}/>
               </Col>
               {this.state.minPrice !== -1 ?
                 (
                   <Col md={3}  className="filter">
                    <p>Price: {this.state.minPrice} $ - {this.state.maxPrice} $</p>
                    <Range min={this.state.priceRange[0]} max={this.state.priceRange[1]} defaultValue={[this.state.minPrice, this.state.maxPrice]} tipFormatter={value => `${value}`} onChange={this.updatePrice}/>
                  </Col>
                  ) : null }
              {this.state.duration !== -1 ?
                    (
                      <Col md={3}  className="filter">
                       <p>Duration: {this.state.duration} weeks</p>
                       <SliderWithTooltip min={this.state.durationRange[0]} max={this.state.durationRange[1]} defaultValue={this.state.duration} tipFormatter={value => `${value}`} onChange={this.updateDuration}/>
                     </Col>
                   ) : null }
              </Row>
            </Form>
          </Col>
        </Row>

        {coursesDataJSX}

      </Container>
    );
  }
}

export default Filters;
