# Movie Mixer

Movie Mixer is a web application that displays information about a randomly selected movie. It uses Flask, TMDB API, and Wikipedia API to fetch movie data, poster images, and Wikipedia links.

## Table of Contents

- [Technologies](#technologies)
- [Setup](#setup)
- [Fly.io URL](#flyio-url)
- [Technical Issues](#technical-issues)
- [Known Problems and Improvements](#known-problems-and-improvements)

## Technologies

This project is created with:

- Flask: Web framework for Python
- TMDB API: API for fetching movie data
- Wikipedia API: API for fetching Wikipedia links
- Google Fonts: Custom font "Gloock"
- HTML and CSS

## Setup

To set up the project, follow these steps:

1. Clone the repository:

2. Install the required packages:

3. Create a `.env` file in the root folder of the project and add your TMDB API key:

4. Run the Flask app:

## Fly.io URL

You can find the deployed app at [https://rough-thunder-6621.fly.dev/](https://rough-thunder-6621.fly.dev/)

## Technical Issues

1. **Issue 1: Displaying Movie Posters**: Initially, movie posters were not displaying properly on the web page. The issue was due to an incorrect URL construction for the TMDB image API. To fix this issue, I researched the TMDB API documentation and found the correct base URL and image size parameters. After updating the URL construction in the `index()` function, movie posters now display correctly on the page.

2. **Issue 2: Handling API Errors**: In the beginning, the app didn't handle API errors gracefully. When there was an issue with the API request (e.g., invalid API key or movie ID), the app would crash. To fix this, I added error handling in the `get_movie_data()` and `get_wikipedia_link()` functions. These functions now return `None` if there's an issue with the API request, and the app can continue to run without crashing.

## Known Problems and Improvements

1. **Improvement 1: Expand Movie Selection**: Currently, the app selects a random movie from a hardcoded list of movie IDs. To improve the app, the movie selection process could be expanded to include a larger pool of movies. This could be done by querying the TMDB API for popular or top-rated movies or by implementing a search feature that allows users to search for movies by title, genre, or director.

2. **Improvement 2: Responsive Design**: The current design of the app may not be fully responsive or optimized for mobile devices. To make the app more accessible on different screen sizes, the CSS could be updated to use media queries, flexible layouts, and responsive design best practices.
