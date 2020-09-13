import os
from flask import (Flask, render_template, redirect,
                   request, url_for, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# imports environment variables
from os import path
if path.exists("env.py"):
    import env

# creates instance of Flask
app = Flask(__name__)

app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = 'foodie'

mongo = PyMongo(app)


@app.route('/')
@app.route('/all_recipes')
def all_recipes():
    recipes = mongo.db.recipes.find()
    return render_template('all_recipes.html', recipes=recipes)


# add a new recipe
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           title="Add Recipe",
                           categories=mongo.db.categories.find(),
                           levels=mongo.db.levels.find(),
                           cuisines=mongo.db.cuisines.find(),
                           allergens=mongo.db.allergens.find())


# add recipe data to MongoDB
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('all_recipes'))


# Edit recipe information
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html',
                           recipe=recipe,
                           categories=mongo.db.categories.find(),
                           cuisines=mongo.db.cuisines.find(),
                           difficulty=mongo.db.levels.find(),
                           allergens=mongo.db.allergens.find())

# browse recipes
@app.route('/browse_recipes')
def browse_recipes():
    recipes = mongo.db.recipes.find()
    return render_template('browse_recipes.html', recipes=recipes)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
