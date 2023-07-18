from flask import Flask, render_template, request, redirect

import sqlite3

app = Flask(__name__)


# Route to retrieve scores from the database and render the template
@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()

    # Fetch scores from the database
    c.execute("SELECT name, score FROM highscores ORDER BY score DESC")
    highscores = c.fetchall()

    # Get the highest score
    highest_score = highscores[0][1]

    # Close the database connection
    conn.close()

    # Render the template with scores data
    return render_template("index.html", highscores=highscores, highest_score=highest_score)


# Route to handle form submission and add scores to the database
@app.route('/add_score', methods=['POST'])
def add_score():
    # Get data from the form submission
    name = request.form['name']
    score = request.form['score']

    # Connect to the SQLite database
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()

    # Insert score into the database
    c.execute("INSERT INTO highscores (name, score) VALUES (?, ?)", (name, score))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    # Redirect to the home page
    return redirect('/')



@app.route('/delete_score', methods=['POST'])
def delete_score():
   # Connect to the SQLite database
    conn = sqlite3.connect('scores.db')
    c = conn.cursor()

    c.execute("SELECT id FROM highscores ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]
    c.execute("DELETE FROM highscores WHERE id=?", (last_id,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
