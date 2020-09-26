# Foodie
![Cover Image](/static/images/readme/foodie-cover.png)
Foodie is a recipe-sharing app for people with an interest in cooking and baking who'd like to discover new recipe ideas and share their own recipes with others. The purpose of this project is to create a simple, user-friendly app where users can create new recipe entries, browse and search for recipes, and update or delete recipes they've added.<br>
Foodie is a Flask project that uses MongoDB to build a recipe database so that users can create, read, update, and delete (CRUD) their recipes.The long-term goal for this project is to add ecommerce and social features to build an online community of Foodie members and influencers.
<br>

[Log in to Foodie here](https://foodie-project.herokuapp.com/)
<br>


## Project Outline

1. [UX](UX)

2. [Documentation](Documentation)

3. [Features](Features)

4. [Technologies Used](Technologies)

5. [Testing]()

6. [Deployment](Deployment)

7. [Project Credits]()

<br><br>

## UX <br><br>
My main goal for this project was to create a simple site that is easy to use and that users would want to recommend to their friends. The target audience for this site is people who are interested in cooking, baking, or making drinks, who want to share their own recipes with others or look for inspiration. There is a 'My Recipes' section where the user can see all of the recipes they've added to the site, so they can also store their own recipes in this way. The search feature allows the user to quickly search for a recipe if they are in a hurry at the supermarket, for example, and the 'Add Recipe' and 'Edit Recipe' pages have a minimal UI to allow the user to focus on the different details they need to include for their recipe entry. The lists of recipes displayed for the user on the site show the key details for each recipe so they can quickly scan through it and select the recipe they need based on the title, difficulty level, or time investment.
<br><br>

### Who is this website for?
* People who wish to store and update recipes and recipe images online
* People who'd like to share their recipes with like-minded people
* People who are looking for some inspiration for their cooking or baking projects
* People who are looking for specific recipes<br><br>

### User Stories
As a user, I want to:
* create a Foodie account.
* log in to Foodie.
* navigate easily through the site.
* view recipes that other users have shared.
* view recipes that include all of the details I need to make the dish (ingredients, method, time, temperature, servings).
* search for specific recipes.
* search for recipes with specific ingredients or keywords.
* add my own recipe.
* view the recipes that I have added.
* edit recipes that I have added.
* delete recipes that I have added.
* access the site from a desktop or laptop.
* access the site from a mobile device.
* log out when I've finished browsing or adding recipes.
<br><br>


## Documentation

### Database Schema
Before starting to build the Foodie app, I planned the overall structure of the recipe database to ensure that all of the data pieces were included.
* [Data Schema Sample - Recipe](documentation/schema.png)
<br><br>

### Wireframes
The desktop and mobile wireframes for this project are located in the 'documentation' folder:
* [Desktop Wireframe](documentation/wireframe.pdf)
* [Mobile Wireframe](documentation/mobile-wireframe.pdf)
<br><br>


## Features

### Existing Features

**Navbars and Navigation** - There are two version of the navbar (one for desktop and one for mobile) that were created using Materialize. The navigation panel allows the user to move quickly to specific pages on the site.<br><br>
![Nav Image](/static/images/readme/navbar.png)<br><br>
The mobile navbar displays the Foodie title logo and a hamburger icon that users can tap to open the sidenav.<br><br>
![Nav Image](/static/images/readme/sidenav.jpg)<br><br>
**Login and Register Pages** - The login page is the first page presented to the user. If the user hasn't already created an account, they can click 'Create one here' to open the register page. Once the user has logged in or registered, they are redirected to the 'All Recipes' page.<br><br>
![Login Image](/static/images/readme/login.png)<br><br>
**All Recipes Page** - The 'All Recipes' page displays all of the recipes that have been added to the site. Users can see a list of recipe cards with a summary of each recipe (image, title and some key details) and can click 'View' on a recipe card to view that particular recipe. <br><br>
![All Recipes Image](/static/images/readme/all-recipes.png)<br><br>
**Search Bar** - Users can type a keyword into the search bar at the top of the 'All Recipes' page to search the recipes for a specific word or recipe title.<br><br>
![Search Bar Image](/static/images/readme/searchbar.png)<br><br>
**Pagination** - If the number of recipes on the site exceeds 6, the list is paginated and the user can use the page navigation at the bottom of the page to move to another page of recipes.<br><br>
![Pagination Image](/static/images/readme/pagination.png)<br><br>
**View Recipe Page** - Shows the full details of the recipe and displays Edit and Delete options for the user who has contributed the recipe.<br><br>
![View Recipe Image](/static/images/readme/view-recipe.png)<br><br>
**Add and Edit Recipe Pages** - The 'Add Recipe' page is a form with several input fields to allow the user to add all of the recipe details. Each field has a label, button, or dropdown menu to indicate to the user what information is required. If the user submits the form without entering all of the required fields, they will see a prompt asking them to fill them in. The 'Edit Recipe' page has similar layout and functionality but the input fields are pre-populated with information already submitted by the user, which they can amend.<br><br>
![Add or Edit Recipe Image](/static/images/readme/add-edit-recipe.png)<br><br>
**My Recipes Page** - The 'My Recipes' page is a private page showing a list of the recipes added by the user. The recipe cards have the same format as the 'All Recipes' page but also include Edit and Delete options for the user.<br><br>
![My Recipes Image](/static/images/readme/my-recipes.png)<br><br>
**Footer** - The footer contains links to social pages, and a copyright notice for the site owner.<br><br>
![Footer Image](/static/images/readme/footer.png)<br><br>
**Log Out** - The user can click 'Log Out' in the navbar or sidebar to end the session and the login page will be displayed.<br><br>
![Log Out Image](/static/images/readme/navbar.png)
<br><br>

## Features Left to Implement
**Social Sharing** - I'd like to add 'Quick Share' feature for social apps such as WhatsApp and Pinterest for users to easily share recipes.

**Download Recipes** - I'd like to add a PDF or print option to the 'View Recipe' page so that users can save and print recipes.

**Advanced Search** - I'd like to add functionality to allow users to refine and filter search results (e.g. by contributor, meal type, and so on). 

**Contributor Pages**  - I'd like to add contributor/profile pages that users can customize to display their activity and recipes to other users, if they wish. Users would have the option to follow or connect with other Foodie members and tag them or comment on their recipes. This would be a valuable feature for the site owner as they could introduce business pages for food brands and influencers and potentially generate revenue in this way.

**Foodie Forum** - I'd like to add a community forum where Foodie members can ask questions, discuss recipes and share useful baking tips in an informal way.

**Video Tutorials** - I'd like to add a section with video tutorials to demonstrate different cooking and baking techniques. This could include videos submitted by users as well as some premium content from well known chefs and bakers.
<br><br>

## Technologies Used
The following languages and frameworks were used to build this project:

**Gitpod IDE** -
[Gitpod](https://www.gitpod.io/) was used as an IDE to build this project.

**Flask** -
This project uses Flask to create and render pages.

**HTML, CSS, JavaScript and Python** -
This project uses HTML, CSS, JavaScript and Python programming languages.

**Google Fonts** -
This project uses [Google Fonts](https://fonts.google.com/) to style fonts.

**Font Awesome** -
The project uses [Font Awesome](https://fontawesome.com/) to present icons throughout the site.

**Materialize** - 
This project uses [Materialize](https://materializecss.com/) for navigation and other elements such as the search bar.

**PIP** -
This project uses PIP to install required tools.

**MongoDB Atlas** -
This project uses [MongoDB Atlas](https://www.mongodb.com/) for the database.

**PyMongo** -
This project uses [PyMongo](https://pypi.org/project/pymongo/) to communicate between Python and MongoDB.

**GitHub and Heroku** -
This project is stored on [GitHub](https://github.com/) and has been deployed to [Heroku](https://www.heroku.com/). 

<br>

## Local Deployment
To run this project locally on your computer, you'll need:
* [GitPod](https://www.gitpod.io/), or another online IDE
* A [MongoDB Atlas](https://www.mongodb.com/) account or run MongoDB locally on your device
And you'll need to install:
* [Python](https://www.python.org/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [Git](https://git-scm.com/)
<br><br>

### Instructions
1. Clone the repository using the command `git clone https://github.com/coderkatew/foodie` or, save a copy of the GitHub repository located at https://github.com/coderkatew/foodie by clicking the green 'Code' button in the repository menu and selecting 'Download ZIP' to extract the zip file to your chosen folder. 
2. In the terminal, change the directory (cd) to the correct location of the file.
3. Set up the environment variables:
 * Create an env.py file in the root directory.
 * At the beginning of the file, type `import os` to set the environment variables in the operating system.
 * Set the connection to the MongoDB database and set up a secret key by adding the following (with your own unique values):
     <br>`os.environ["SECRET_KEY"] = "YourSecretKey"`
     <br>`os.environ["MONGO_URI"] = "MongoURI"`
4. Install the project requirements using this command in the terminal:
`pip3 install -r requirements.txt`
5. Create a new database in MongoDB and name it 'foodie'. 
6. Run the application with the command `python3 app.py`.
<br><br>

## Deploying to Heroku
To deploy the project to Heroku, you can follow these steps:
1. Create a requirements.txt file (this is also required for local deployment, step 4 above).
2. Create a Procfile using the command `echo web: python app.py > Procfile`.
3. Make sure the env.py has been added to the .gitignore file.
4. Create an app in Heroku named 'foodie-project'.
5. Go to 'Reveal Config Vars' in settings in Heroku and add the environmental variables for IP, PORT, MONGODB_URI and SECRET_KEY (they should match the env.py file in order to connect successfully).
6. Log in to Heroku through the terminal with the comman `heroku login -i`.
7. Once you are logged in, use the command `git push heroku master` to push the project to Heroku.
8. Click 'Open App' at the top of the Heroku dashboard and the project will open in a new tab.

--------

[Back to top](Foodie)
