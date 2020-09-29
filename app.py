import os
from flask import (Flask, render_template, redirect,
                   request, url_for, session, flash)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import bcrypt
import math

# Imports the environment variables
from os import path
if path.exists("env.py"):
    import env

# Creates an instance of Flask
app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'foodie'

mongo = PyMongo(app)


# I learned how to set up the register and login pages from this tutorial https://www.youtube.com/watch?v=vVx1737auSE
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('all_recipes'))

    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session["username"] = request.form["username"]
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'),
               login_user['password']) == login_user['password']:

                return redirect(url_for('all_recipes'))

        flash('Invalid username/password combination')
        session.pop('username', None)
        return render_template('login.html', title="Log In")

    return render_template('login.html', title="Log In")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('all_recipes'))
        flash('Sorry,that username already exists.')
        return render_template('register.html')

    return render_template('register.html')


@app.route('/all_recipes')
def all_recipes():
    recipes = mongo.db.recipes
    limit_per_page = 6  # 6 results shown per page
    current_page = int(request.args.get('current_page', 1))
    # I got ideas for implementing pagination from Code Institute students on Slack
    total = recipes.count()
    pages = range(1, int(math.ceil(total / limit_per_page)) + 1)
    recipes = recipes.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*limit_per_page).limit(limit_per_page)

    # profile_name is required here to determine where delete and edit options are visible on recipe cards for the recipe contributor
    profile_name = mongo.db.users.find_one({'name': session['username']})['name']

    return render_template("all_recipes.html", recipes=recipes,
                           current_page=current_page,
                           pages=pages, total=total, profile_name=profile_name)


# Displays form for adding a new recipe
@ app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           title="Add Recipe",
                           categories=mongo.db.categories.find(),
                           levels=mongo.db.levels.find(),
                           cuisines=mongo.db.cuisines.find(),
                           allergens=mongo.db.allergens.find())


# Converts string from text input field to array by splitting the string at each new line break
def convert_to_array(string):
    array = string.split("\n")
    return array


@app.route('/uploads/<filename>', methods=['GET'])
def upload(filename):
    return mongo.send_file(filename)


# Adds recipe data to MongoDB
@ app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    # Saves image to MongoDB
    recipe_image = request.files['recipe_image']
    if request.files:
        mongo.save_file(recipe_image.filename, recipe_image)

    recipes = mongo.db.recipes
    recipes.insert_one({
                'recipe_name': request.form['recipe_name'],
                'contributor': session['username'],
                'recipe_image': recipe_image.filename,
                'category': request.form.get('category'),
                'difficulty': request.form.get('difficulty'),
                'cuisine': request.form.get('cuisine'),
                'servings': request.form['servings'],
                'time': request.form['time'],
                'temperature': request.form['temperature'],
                'ingredients': convert_to_array(request.form['ingredients']),
                'method': convert_to_array(request.form['method']),
                'allergens': request.form.getlist('allergens')
            })
    return redirect(url_for('all_recipes'))


# Displays data from MongoDB on Edit Recipe page
@ app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    existing_ingredients = '\n'.join(recipe['ingredients'])
    existing_method = '\n'.join(recipe['method'])

    return render_template('edit_recipe.html',
                           recipe=recipe,
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           levels=mongo.db.levels.find(),
                           allergens=mongo.db.allergens.find(),
                           existing_ingredients=existing_ingredients,
                           existing_method=existing_method)


# Updates recipe data in MongoDB
@ app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    recipe_image = request.files['recipe_image']

    if 'recipe_image' in request.files:
        mongo.save_file(recipe_image.filename, recipe_image),
        # Update_one updates only the data that has been changed in the form
        recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set":
            {
                'recipe_name': request.form['recipe_name'],
                'contributor': session['username'],
                'category': request.form.get('category'),
                'difficulty': request.form.get('difficulty'),
                'cuisine': request.form.get('cuisine'),
                'servings': request.form['servings'],
                'time': request.form['time'],
                'temperature': request.form['temperature'],
                'ingredients': convert_to_array(request.form['ingredients']),
                'method': convert_to_array(request.form['method']),
                'allergens': request.form.getlist('allergens')
            }})
    if recipe_image.filename != "":
                    recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": {'recipe_image': recipe_image.filename}})

    return redirect(url_for('view_recipe', recipe_id=recipe_id))


# Deletes recipes from MongoDB
@ app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('all_recipes'))


# Displays all recipe details
@app.route('/view_recipe/recipe_id?=<recipe_id>')
def view_recipe(recipe_id):
    mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template('view_recipe.html',
                           recipe=mongo.db.recipes.find_one(
                               {"_id": ObjectId(recipe_id)}),
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           levels=mongo.db.levels.find(),
                           allergens=mongo.db.allergens.find())


# Credit for search feature to https://stackoverflow.com/questions/48371016/pymongo-how-to-use-full-text-search
@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    keyword = request.form["keyword"]

    # Creates index in MongoDB
    mongo.db.recipes.create_index([("$**", 'text')])

    # Searches for keyword in MongoDB
    recipes = mongo.db.recipes.find({"$text": {"$search": keyword}})

    return render_template('all_recipes.html',
                           username=session['username'],
                           recipes=recipes,
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           levels=mongo.db.levels.find(),
                           allergens=mongo.db.allergens.find(),
                           total=recipes.count(),
                           keyword=keyword)


# Displays the recipes the current user has contributed
@ app.route('/my_recipes/<username>', methods=['GET'])
def my_recipes(username):
    current_user = mongo.db.users.find_one({'name': session['username']})['_id']
    profile_name = mongo.db.users.find_one({'name': session['username']})['name']
    # Finds the recipes by the current user
    contributor_recipes = mongo.db.recipes.find({'contributor': profile_name})

    total_recipes = contributor_recipes.count()
    return render_template('my_recipes.html',
                           contributor_recipes=contributor_recipes,
                           username=profile_name,
                           total_recipes=total_recipes)


# Logout
@app.route('/logout')
def logout():
    # removes the username from the session
    session.pop('username', None)
    return redirect(url_for('index'))


# Error Handlers
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html', error=True,
                           title="Page Not Found"), 404


@app.errorhandler(405)
def error_405(error):
    return render_template('errors/405.html', error=True,
                           title="Method Not Allowed"), 405


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html', error=True,
                           title="Internal Server Error"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
