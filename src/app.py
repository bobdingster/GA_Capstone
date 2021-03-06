import food_functions
from flask import Flask, url_for, request, redirect, render_template

#initializing the flask app
app = Flask('funcMap')

#Initializing the first page
@app.route("/")

# Initializing and Defining what happens on the home page
@app.route("/home")
def home():
    return render_template('home.html')


# Initializing and Defining what happens on the about page
@app.route("/about")
def about():
    return render_template('about.html')

# Initializing and Defining what happens on the results page
@app.route("/results")
def results():
    return render_template('results.html')


# Initializing and Defining what happens when someone clicks submit
@app.route("/submit")
def form_submit():
    user_input = request.args
    search = str(user_input['search'])
    response = str(user_input['user_text']) # get the user input
    if search == "ingr":
        output1 = food_functions.ingredient_find(response)
        output = output1[['name', 'minutes', 'ingredients', 'match']]
        output.set_index('name', inplace=True)
    return render_template('results.html', tables=[output.to_html(classes='data')], titles=output.columns.values) # Show html output on page



if __name__ == '__main__':
    app.run(debug=True)
