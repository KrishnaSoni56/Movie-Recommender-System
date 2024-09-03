# Movie-Recommender-System

# Project Overview :
This project is a Movie Recommender System that aims to help users to find movies according to their own preferences . This Recommender System is based on a TMDB data obtained from Kaggle. The system uses collaborative filtering and content-based filtering techniques to suggest movies similar to the interest of the user .

# Dataset :
The dataset used in this project is sourced from Kaggle and contains detailed information about the Movies .

Key feature :-
1. Movie_Id : Unique id determined for each individual movie.
2. Title : Basically the name of the movie.
3. Overview : Short discription about movie like year of release or fundamental concept on which the movie is based .
4. Genres : Include some special characteristics of a movie in a differenct styple like '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]'
5. Cast and Crew : Consists of actors , producers , directors and rest of the team that are involves in making a movie .

# Technologies and Tools Used:

1. Python: Core programming language for building the recommendation algorithms.
2. Numpy & Pandas: For data Cleaning & Manipulation.
3. Scikit-Learn: For implementing machine learning algorithms.
4. Nltk: Used Nltk for stemming process.
5. Pickle : Performing serialization for our recommender system so that it can be used with our web interface
6. Streamlit : Used for creating the web app for our recommender system .

# How It Works:

1. Data Collection: The system uses a movie dataset that includes movie name, cast & crew and other relevant information.
2. Preprocessing: The data is cleaned and prepared for analysis, including handling missing values and normalizing discription of movies.
3. Feature Extraction : Merging Data sets , removing less important features , converting string of list to list only , Applying list comprehension on some of the features , Creating a new feature called 'Tags' that involves of information regrading the movie like cast , overview and any other keywords. At last we have three features that describes whole thing about the movies i.e 'movie_id', 'title', 'Tags' .
4. Model Building: Both collaborative and content-based models are trained on the data.
5. Recommendation Generation: Based on the user's input (e.g., Movie Name = Avatar), the system generates personalized movie recommendations.
6. Building the Web App for are system  : Used streamlit for this task and loaded our model for real time movie recommendation .

