from flask import Flask, render_template, request, redirect

import sqlite3

app = Flask(__name__)




# Route to retrieve scores from the database and render the template
@app.route('/')
def get_application_by_id():
    # Connect to the SQLite database
    conn = sqlite3.connect('appcon.db')
    c = conn.cursor()

    # Fetch scores from the database
    c.execute("SELECT name, ipfilter FROM application")
    application = c.fetchall()

 

    # Close the database connection
    conn.close()

    # Render the template with the applications data
    return render_template('appscherm.html', application=application)

@app.route('/appscherm/<int:id>')
def show_application(id):
    application = get_application_by_id(id)
    if application:
        return render_template('appscherm.html', application=application)
    else:
        return "Application not found."
    
if __name__ == '__main__':
    app.run(debug=True)



# Route to handle form submission and add scores to the database
@app.route('/add_application', methods=['POST'])
def add_application():
    # Get data from the form submission
    name = request.form['name']
    ipfilter = request.form['ipfilter']

    # Connect to the SQLite database
    conn = sqlite3.connect('appcon.db')
    c = conn.cursor()

    # Insert score into the database
    c.execute("INSERT INTO application (name, ipfilter) VALUES (?, ?)", (name, ipfilter))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

    # Redirect to the home page
    return redirect('/')


@app.route('/delete_application', methods=['POST'])
def delete_score():
   # Connect to the SQLite database
    conn = sqlite3.connect('appcon.db')
    c = conn.cursor()

    c.execute("SELECT id FROM application ORDER BY id DESC LIMIT 1")
    last_id = c.fetchone()[0]
    c.execute("DELETE FROM application WHERE id=?", (last_id,))
    conn.commit()
    conn.close()
    return redirect('/')