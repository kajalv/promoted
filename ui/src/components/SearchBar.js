import React, {Component} from 'react';
import '../styles/SearchBar.css';
import Container from 'react-bootstrap/Container';

//reference: https://alligator.io/react/react-autocomplete/

class SearchBar extends Component {
  constructor() {
    super();

    this.state = {
      activeSuggestion: 0,
      filteredSuggestions: [],
      showSuggestions: false,
      userInput: "",
      search: false,
      showFilters: false
    };

    this.suggestions = []
  }

  onChange = e => {
    const userInput = e.currentTarget.value;

    // Filter our suggestions that don't contain the user's input
    const filteredSuggestions = this.suggestions.filter(
      suggestion =>
        suggestion.toLowerCase().indexOf(userInput.toLowerCase()) > -1
    );

    // Update the user input and filtered suggestions, reset the active
    // suggestion and make sure the suggestions are shown
    this.setState({
      activeSuggestion: 0,
      filteredSuggestions,
      showSuggestions: true,
      userInput: e.currentTarget.value
    });
  };

  onClick = e => {
    console.log("in click");
    // Update the user input and reset the rest of the state
    this.setState({
      activeSuggestion: 0,
      filteredSuggestions: [],
      showSuggestions: false,
      userInput: e.currentTarget.innerText
    });
  };

  onKeyDown = e => {
    const { activeSuggestion, filteredSuggestions } = this.state;

    // User pressed the enter key, update the input and close the
    // suggestions
    if (e.keyCode === 13) {
      e.preventDefault(); // Have to prevent default or enter would reload the page
      this.setState({
        activeSuggestion: 0,
        showSuggestions: false,
        userInput: filteredSuggestions[activeSuggestion]
      });
    }
    // User pressed the up arrow, decrement the index
    else if (e.keyCode === 38) {
      if (activeSuggestion === 0) {
        return;
      }

      this.setState({ activeSuggestion: activeSuggestion - 1 });
    }
    // User pressed the down arrow, increment the index
    else if (e.keyCode === 40) {
      if (activeSuggestion - 1 === filteredSuggestions.length) {
        return;
      }

      this.setState({ activeSuggestion: activeSuggestion + 1 });
    }
  };

  componentDidMount() {
    this.suggestions=[
          "Social Worker",
          "Software Developer",
          "Administrative Assistant",
          "Bartender",
          "Cashier",
          "Delivery Driver",
          "Human Resources",
          "Interior Designer",
          "Warehouse worker",
          "Marketing"
        ]
  }

  render() {
    let {showSuggestions, userInput, filteredSuggestions, activeSuggestion, search, showFilters} = this.state

    let filtersComponent;

    if (showFilters) {

    }


    let suggestionsListComponent;

    if (showSuggestions && userInput) {
      if (filteredSuggestions.length) {
        suggestionsListComponent = (
          <ul className="suggestions">
            {filteredSuggestions.map((suggestion, index) => {
              let className;

              // Flag the active suggestion with a class
              if (index === activeSuggestion) {
                className = "suggestion-active";
              }

              return (
                <li
                  className={className}
                  key={suggestion}
                  onClick={this.onClick}
                >
                  {suggestion}
                </li>
              );
            })}

          </ul>
        );
      } else {
        suggestionsListComponent = (
          <div className="no-suggestions">
            <em>No suggestions, you're on your own!</em>
          </div>
        );
      }
    }

    return (
    <Container className="searchbar-container">
      <form className={"search-form" + ((showSuggestions && userInput)? " with-suggestions" : "")}>
        <input type="text" value={this.state.userInput} onKeyDown={this.onKeyDown} onChange={this.onChange} placeholder="Search for your next career role" className="search-input"/>
        <i className="fa fa-search fa-2x" id="searchBtn" aria-hidden="true"></i>
      </form>

      {suggestionsListComponent}
    </Container>
    );
  }
}

export default SearchBar;
