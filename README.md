<h1>Recom</h1>
<p>Recom is a recommendation system for movies developed by Praveen Raj, Sarthak Chawla, and Aman Dixit. The system utilizes movie data from the MovieLens dataset to provide personalized movie recommendations to users based on their preferences. The project consists of a Flask web application that allows users to input their userID, which then fetches and displays relevant movie recommendations.</p>
<h2>File Structure:</h2>
<pre>
RECOM
│   app.py
│   average_merged_movies.csv
│   sorted_movies_by_rating.csv
│   user_favorite_genres_and_movies.csv   
│
└───__pycache__
│
└───assets
│
└───static
│   │   style.css
│   │   styles2.css 
│
│   index.html 
│   results.html  
│
└───venv 
</pre>
<h2>File Descriptions:</h2>
<ul>
  <li><code>app.py</code>: The main Python script containing the Flask application logic.</li>
  <li><code>average_merged_movies.csv</code>: A CSV file containing the average rating of all movies.</li>
  <li><code>sorted_movies_by_rating.csv</code>: A CSV file containing movies sorted by rating in descending order.</li>
  <li><code>user_favorite_genres_and_movies.csv</code>: A CSV file containing genre-specific movies highly rated by the user.</li>
  <li><code>index.html</code>: HTML file for the user interface where the user inputs their userID.</li>
  <li><code>results.html</code>: HTML file for displaying the movie recommendations to the user.</li>
  <li><code>static</code>: Directory containing static files such as CSS stylesheets.</li>
  <li><code>venv</code>: Directory containing the Python virtual environment.</li>
</ul>
<h2>How to Run the Project:</h2>
<ol>
  <li>Extract the contents of the Recom.zip file to a directory on your system.</li>
  <li>Ensure that Flask is installed on your system. If not, install Flask using pip:
    <pre>pip install flask</pre>
  </li>
  <li>Open a terminal or command prompt and navigate to the directory where the project files are extracted.</li>
  <li>Activate the Python virtual environment (if not already activated):
    <pre>source venv/bin/activate</pre>
    or
    <pre>venv\Scripts\activate</pre>
  </li>
  <li>Run the Flask application by executing the <code>app.py</code> script:
    <pre>python app.py</pre>
  </li>
  <li>Once the Flask application is running, open a web browser and go to <code>http://localhost:5000</code> to access the application.</li>
  <li>Enter your userID in the provided input field on the index page and submit the form.</li>
  <li>The application will fetch and display personalized movie recommendations based on your preferences on the results page.</li>
</ol>
<p><strong>Note:</strong> Ensure that all CSV files (<code>average_merged_movies.csv</code>, <code>sorted_movies_by_rating.csv</code>, <code>user_favorite_genres_and_movies.csv</code>) are present in the same directory as <code>app.py</code> for the application to function correctly.</p>
<h2>Project Contributors:</h2>
<ul>
  <li>Praveen Raj</li>
  <li>Sarthak Chawla</li>
  <li>Aman Dixit</li>
</ul>
