# MileSteps Workout Tracker

MileSteps is a REST API and web application for tracking running workouts. Users can record their running workouts, retrieve workout data, and view aggregated statistics. Additionally, users can upload pictures related to their workouts.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Web Interface](#web-interface)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- Record running workouts with details such as duration, distance, route nickname, date/time, and pictures.
- Retrieve workout records with filtering and searching capabilities.
- Calculate aggregated statistics like total distance, average duration, and more.
- Integrate with a third-party service to fetch weather data for workout timestamps.
- Simple web interface to interact with the API.

## Technologies Used

- Python
- Flask (Web Framework)
- HTML/CSS/JavaScript (Web Interface)
- OpenWeatherMap API (Third-party Weather Service)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/MileSteps-Project.git
   cd MileSteps-Project
## API Endpoints
 Create a New Workout Record
URL: POST http://localhost:5000/workouts
Request Body: JSON containing workout details.
Response: JSON indicating success or failure.
Retrieve All Workout Records
URL: GET http://localhost:5000/workouts
Response: JSON array of all workout records.
Filter Workout Records by Date Range
URL: GET http://localhost:5000/workouts/filter?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
Request Parameters: start_date (start date) and end_date (end date).
Response: JSON array of filtered workout records.
Retrieve Aggregated Summary Data
URL: GET http://localhost:5000/workouts/summary
URL for Weekly Summary: GET http://localhost:5000/workouts/summary?summary_type=weekly
Response: JSON containing aggregated statistics.
Search Workout Records
URL: GET http://localhost:5000/workouts/search?nickname=Nickname
Request Parameter: nickname (nickname to search for).
Response: JSON array of matching workout records.
Web Interface
Access the web interface for the MileSteps Workout Tracker by opening this URL in a web browser:

URL: http://localhost:5000/
