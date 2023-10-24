# RISE
Ideal Workflows: Staggering refers to multiple calls by a given item

- run() //called on creation of website instance
  - run_backend()
    - pull_ticker_list()
    - push_ticker_list()
    - make_database()
    - push_database()
      - interpret_JSON()
        - pull_data()
  - run_frontend()
    - initialize_website()
      - pull_stored_data()
      - get_stock_price()
      - get_stock_info()
      - get_stock_news()
      - get_stock_info_time()
      - get_stock_graph() //mutually exclusive with get_stock_history()
      - get_stock_history() //mutually exclusive with get_stock_graph()
    - Each Location where data is necessary will call respective display functions (to update displays)


Key: H = Heading, T = Task, F = Function, 'X' = Completed

Tasks and Functions Outline:

- [ ] H1 - Test API
  - [X] T1.1 - Create test_folder/ directory for Testing
  - [X] T1.2 - Install libraries needed for API
  - [X] T1.3 - Testing Data Pulls
    - [X] T1.3.1 - Create File and include all imports necessary
    - [ ] F1.3.2 - Write function pull_data() which makes a call to the API Function and returns data to terminal or file
    - [ ] T1.3.3 - Cross-check with API README.md to confirm data is pulled correctly
    - [ ] T1.3.4 - Cross-check during open market hours to ensure data is accurate and real-time
  - [ ] T1.4 - Data Pull Speed
    - [ ] T1.4.1 - Import necessary time-measurement libraries
    - [ ] F1.4.2 - Write function test_pull_speed() which makes a call to pull_data() and returns speed of 1 call, 5 calls, 10 calls, and 100 calls
    - [ ] F1.4.3 - Write function test_pull_efficiency() which makes a call to pull_data() and returns the number of calls that can be made in 30 seconds
    - [ ] T1.4.4 - If test_pull_speed() is more than 3 seconds for 1 call (or proportionally to the higher call counts) debug or look into changing APIs if necessary
    - [ ] T1.4.5 - If test_pull_efficiency() is less than 30 calls over 30 seconds (necessary for at least main display) debug or look into changing APIs if necessary
  - [ ] T1.5 - Debug and Create Module
    - [ ] F1.5.1 - If all procedures are working according to expectations, write unit tests for each function (to attempt to catch potential errors)
    - [ ] T1.5.2 - If all unit tests are passed, begin moving functions and file content to the backend_files/ directory
    - [ ] T1.5.3 - Review with at least 2 members of the team before confirming completion of section

- [ ] H2 - Interpret Data Pulls
  - [ ] T2.1 - Create file in test_folder/ directory for JSON interpretation
  - [ ] T2.2 - Review JSON format specified in API README.md and official API documentation
  - [ ] F2.3 - Write function interpret_JSON() which takes the output of pull_data() and returns an array of values indexed according to data in JSON
  - [ ] T2.4 - Test interpret_JSON()
    - [ ] T2.4.1 - Write .json file sample_API_output.json which creates a JSON file in the format specified by the API documentation
    - [ ] F2.4.2 - Write unit test to compare true output of interpret_JSON() with the expected output (written by developer)
    - [ ] T2.4.3 - If unit test fails, review interpret_JSON and check to ensure sample input and expected output are valid and correspond
  - [ ] F2.5 - Write function interpret_JSON_speed() which calls pull_data() => interpret_JSON() and finds speed of entire operation for 1 and 10 consecutive calls
  - [ ] T2.6 - Debug and Create Module
    - [ ] T2.6.1 - If interpret_JSON_speed() is insufficient, look into optomization techniques or debug for cause of delay
    - [ ] T2.6.2 - If all unit tests are passed, begin moving functions and file content to the backend_files/ directory
    - [ ] T2.6.3 - Review with at least 2 members of the team before confirming completion of section

- [ ] H3 - Push Data to Database
  - [ ] T3.1 - Download and Install the MongoDB Python Driver
  - [ ] T3.2 - Create file in test_folder/ directory and initialize Database for one instance
  - [ ] F3.3 - Write function make_database() which uses driver functions to automatically make a database for an instance of the website
  - [ ] F3.4 - Write function push_database() which uses driver functions to upload output from interpret_JSON
  - [ ] T3.5 - Test make_database() and push_database()
    - [ ] F3.5.1 - Write unit test for make_database() and attempt to make multiple instances of databases by calling make_database() multiple times
    - [ ] F3.5.2 - Write unit test for push_database() that uses sample_API_output.json from T2.4.1 to test uploading interpreted JSOn data to database
    - [ ] F3.5.3 - Write unit test for push_database() that uploads data from API from pull_data() => interpret_JSON() => push_database()
    - [ ] T3.5.4 - If unit tests fail, review functions and MongoDB documentation to debug and modify functions
  - [ ] T3.6 - Debug and Create Module
    - [ ] T3.6.1 - If any unit tests are failed, look into MongoDB documentation or associated function procedure
    - [ ] T3.6.2 - If all unit tests are passed, begin moving functions and file content to the backend_files/ directory
    - [ ] T3.6.3 - Review with at least 2 members of the team before confirming completion of section

- [ ] H4 - Create Website Outline
  - [X] T4.1 - Create frontend_files/ directory
  - [X] T4.2 - Create index.html and styles.css and add HTML Boilerplate
  - [X] T4.3 - Outline Website Framework
    - [X] T4.3.1 - Using Flexbox methodology, outline the Website according to the Requirements Specification Document
    - [X] T4.3.2 - Style each div using id and class tags and create vars in CSS to standardize certain design patterns
  - [ ] T4.4 - Getter Scripts ***NEEDS TO BE EXPANDED***
    - [ ] T4.4.1 - Using Javascript or JS Framework, outline the following functions:
    - [ ] F4.4.2 - Write pull_stored_data() which pulls data from the MongoDB Database made for the website
    - [ ] F4.4.3 - Write get_stock_price() which takes data from pull_stored_data() and returns the stock price for a given Ticker symbol
    - [ ] F4.4.4 - Write get_stock_info() which takes data from pull_stored_data() and returns an array containing the stock info
    - [ ] F4.4.5 - Write get_stock_news() which takes data from pull_stored_data() and returns two news articles in an array for a given Ticker symbol
    - [ ] F4.4.6 - Write get_stock_info_time() which takes data from pull_stored_data() and returns the time of the latest update of the stock data
    - [ ] F4.4.7 - Write get_stock_graph() which takes data from pull_stored_data() and returns a graph containing stock data for a given interval (1 day/week/month/year)
    - [ ] F4.4.8 - Write get_stock_history() which takes data from pull_stored_data() and returns an array of data of stock data for a given interval (1 day/week/month/year)
  - [ ] T4.5 - Interpretation Scripts ***MAY NEED TO BE EXPANDED***
    - [ ] F4.5.1 - Write make_stock_graph() calls get_stock_history() and creates a graph using node points on fixed spacing for a given interval (1 day/week/month/year)
    - [ ] F4.5.2 - Write make_stock_delta() calls get_stock_price() and get_stock_info() to compare the market open and current price to return the delta (either as true or %)
  - [ ] T4.6 - Display Scripts ***NEEDS TO BE EXPANDED***
    - [ ] F4.6.1 - Write display_stock_price() which calls get_stock_price() and displays the data in the associated div
    - [ ] F4.6.2 - Write display_stock_info() which calls get_stock_info() and runs subfunctions to interpret the data and format it for display purposes
    - [ ] F4.6.3 - Write display_stock_news() which calls get_stock_news() and displays the data to the associated div flex-container
    - [ ] F4.6.4 - Write display_stock_time() which calls get_stock_info_time() and displays the time of the last update to the associated div
    - [ ] F4.6.5 - Write display_stock_graph() which either calls and displays get_stock_graph() or make_stock_graph() (Mutually Exclusive Cases)
    - [ ] F4.6.6 - Write display_stock_delta() which calls make_stock_delta() and displays the data in the associated div

- [ ] H5 - Implement Searchbar
  - [ ] T5.1 - Create Valid Stock Ticker/Name Database
    - [ ] T5.1.1 - Pull data from API(s) of all supported Stock Names and Ticker Symbols in backend
    - [ ] F5.1.2 - Write function pull_ticker_list() which uses API functions to access a list of all supported Ticker Symbols
    - [ ] F5.1.3 - Write function push_ticker_list() which pushes the ticker symbol list to a MongoDB Database (generated once per session or alternatively is static)
  - [ ] T5.2 - Outline Searchbar Functionality
    - [ ] T5.2.1 - Searchbar should take string input and suggest various ticker symbols based on text match (sorted search/hash algorithm for efficiency)
    - [ ] F5.2.2 - Write find_associated_tickers() which takes string input and returns an array of 5 suggested stocks by ticker symbol
    - [ ] T5.2.3 - Each suggested search result should be a link which triggers an event to update the main display (or alternatively has a button to do so)

- [ ] H6 - Creating Website and Updating Display
  - [ ] T6.1 - Creating Website
    - [ ] T6.1.1 - Website should be created and have default stocks in the sidebar and main display
    - [ ] T6.1.2 - Website should on creation run the backend programs to generate the database to pull data
    - [ ] F6.1.3 - Write backend_run() which calls all necessary backend functions to initialize website
    - [ ] F6.1.4 - Write frontend_run() which calls all necessary frontend functions to initialize website
    - [ ] F6.1.5 - Write run() which calls both backend_run() and frontend_run() and start_clock()
    - [ ] F6.1.6 - Write initialize_website() which calls all the getter scripts initially
  - [ ] T6.2 Updating Display
    - [ ] T6.2.1 - Website should maintain an internal clock that triggers event based on tick intervals
    - [ ] F6.2.2 - Write start_clock() which maintains an internal timer for the website instance
    - [ ] F6.2.3 - Write get_clock_state() which returns the current time that the clock has been running

- [ ] H7 - Additional Features
  - [ ] T7.1 - Account Authentication and Login
  - [ ] T7.2 - Saved Lists for User
  - [ ] T7.3 - UI Color Scheme Selector
  - [ ] T7.4 - Advanced Analytics Option (requires a settings option)

     
