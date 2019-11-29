import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';
import Slider from 'rc-slider';
import React, {Component} from 'react';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { withRouter } from 'react-router-dom';
import {Link} from 'react-router-dom';
import CardDeck from 'react-bootstrap/CardDeck';

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
      levels: this.props.location.query.includes("Senior") ? new Set(["intermediate"]) : new Set(["beginner"]),
      //levels: new Set(["beginner"]),
      allData: [],
      currentData: []
    }
  }

  getDurationRange = (data, levels) => {
    let minD = Number.MAX_SAFE_INTEGER, maxD = 0;
    for (var i = 0; i < data.length; i++) {
      if (levels.has(this.mappedCourseLevel(data[i].level))) {
        minD = Math.min(minD, data[i].duration)
        maxD = maxD + data[i].duration
      }
    }
    return {
      minD: minD,
      maxD: maxD
    };
  }

  getPriceRange = (data, levels) => {
    let minP = Number.MAX_SAFE_INTEGER, maxP = 0;
    let modified = false
    for (var i = 0; i < data.length; i++) {
      if (levels.has(this.mappedCourseLevel(data[i].level))) {
        modified = true
        minP = Math.min(minP, data[i].price)
        maxP = Math.max(maxP, data[i].price)
      }
    }
    if (!modified) {
      return {
        min: 0,
        max: 0
      };
    }
    return {
      min: Math.round(minP),
      max: Math.round(maxP)
    };
  }

  updatePrice = (value) => {
    this.setState({
      minPrice: value[0],
      maxPrice: value[1]
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

    let {min, max} = this.getPriceRange(this.state.allData, levels)
    let {minD, maxD} = this.getDurationRange(this.state.allData, levels)
    this.setState({
      levels:levels,
      priceRange:[min, max],
      durationRange :[minD, maxD]
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
    let currentData = [];
    let allData = this.state.allData;
    allData.sort((a, b) => {
      if (a.duration === b.duration) {
        return a.title.localeCompare(b.title);
      } else if (a.duration < b.duration) {
        return -1;
      } else {
        return 1;
      }
    })
    console.log(allData);
    let totalD = 0;
    for(let index = 0; index < allData.length; index++) {
      // if (currentData.length >= displayCount)
      //   break;
      let course = allData[index];

      if (course.price >= this.state.minPrice && course.price <= this.state.maxPrice
            && this.state.levels.has(this.mappedCourseLevel(course.level))){
              if (totalD + course.duration > (this.state.duration)) {
                break;
              }
              currentData.push(course);
              totalD += course.duration;
            }

    }

    return currentData;
  }

  componentDidMount() {
    let url = 'http://localhost:5000/get_courses?job_title=' + (this.props.location.query.includes("Senior")? this.props.location.query.substring(7) : this.props.location.query);

    fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(response => response.json())
            .then(data => {
                let {min, max} = this.getPriceRange(data, this.state.levels);
                let {minD, maxD} = this.getDurationRange(data, this.state.levels);
                this.setState({
                  priceRange:[min, max],
                  minPrice: min,
                  maxPrice: max,
                  durationRange :[minD, maxD],
                  duration: maxD,
                  allData: data
                });
            });
  }

  render() {
    let currentData = this.getCurrentData();
    let coursesDataJSX = [];

    for (var i = 0; i < currentData.length; i+=2) {
      coursesDataJSX.push(
        <Row key={i}>
        <Col md={{span:8, offset:2}} style={{marginTop: "2vmin"}}>
        <CardDeck>
          <Card>
            <Card.Header>{currentData[i].site}</Card.Header>
            <Card.Body>
              <Card.Title>{currentData[i].title}</Card.Title>
              <Card.Text>
                Duration : {currentData[i].duration} weeks
              </Card.Text>
              <Card.Text>
                Price: ${currentData[i].price}
              </Card.Text>
            </Card.Body>
          </Card>
          {i+1 < currentData.length ? (<Card>
            <Card.Header>{currentData[i+1].site}</Card.Header>
            <Card.Body>
              <Card.Title>{currentData[i+1].title}</Card.Title>
              <Card.Text>
                Duration : {currentData[i+1].duration} weeks
              </Card.Text>
              <Card.Text>
                Price: ${currentData[i+1].price}
              </Card.Text>
            </Card.Body>
          </Card>) : null}
          </CardDeck>
        </Col>
      </Row>)
    }


    return (
      <Container id="filter-container" fluid={true}>
        <Row>
          <Col md={3} id="filters-title-col">
            <h2 id="filters-title">Promot<span style={{color:"#5da9e9"}}>Ed</span></h2>
          </Col>
          <Col md={{span:2, offset:7}}>
            <Button style={{marginTop: "2vh"}} variant="primary" id="backBtn"><Link to="/">Back to search</Link></Button>
          </Col>
        </Row>
        <Row style={{marginTop:"2vmin"}}>
          <Col md={{span:8, offset:2}}>
            <div id="goal-div">
              <h3>Results for: <span style={{color:"#5da9e9"}}>{this.props.location.query}</span></h3>
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
                       <p>Time Budget: {this.state.duration} weeks</p>
                       <SliderWithTooltip min={this.state.durationRange[0]} max={this.state.durationRange[1]} value={this.state.duration} tipFormatter={value => `${value}`} onChange={this.updateDuration}/>
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

export default withRouter(Filters);
