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

5. [Testing](#Testing)

6. [Deployment](#Deployment)

7. [Credits and Acknowledgements](#Credits)

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

## Design
There several pieces of information associated with each recipe or list of recipes so I chose a colour scheme with a small number of colours and a minimal design overall for a simple interface focused on the recipe images and content.<br>
The buttons and hover states for menu items are all red colors to indicate to the user that they are interactive.<br>
I chose more neutral black, white and cream colours for the footer, navbars and body elements across the site to bring focus to the colours in the recipe images, and to contrast with the red CTAs.<br>
I used the Google Font [Indie Flower](https://fonts.google.com/specimen/Indie+Flower?selection.family=Indie+Flower#standard-styles) throughout the site to add a playful, informal style while keeping the text legible.<br>
I used Materialize to add elements such as the navbar, footer, pagination, and search bar and kept some default styles as they fitted well with the overall theme.<br>
The favicon ('F') is taken from the Foodie title logo so that people will develop a familiarity with it and to promote a consistent brand experience that could be built on later when social, community and ecommerce features are added to the app.<br><br>


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
![Log Out Image](/static/images/readme/navbar.png)<br><br>
**Error Messaging and Warnings** - Error handlers, flash messages, and warning modals have been added to the project to inform the user if there is a site error or incorrect input.<br><br>
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

## Testing

### Automated Testing - Validation Programs
HTML files have been tested using [W3C Markup Validator](https://validator.w3.org/). See results [here](/testing).
The CSS file has been tested using [Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/). See results [here](/testing).
The Javascript file has been tested using [JSHint](https://jshint.com/). See results [here](/testing).
The Python file has been tested using [PEP8](http://pep8online.com/). There are a number of "line too long" warnings in the test results which I haven't been able to resolve without breaking the code but it is mentioned as a known issue online. See results [here](/testing).

### Manual Testing
This project has been tested manually on desktop and mobile in Chrome and Firefox. I used Chrome Developer Tools to carry out some of the mobile testing.
All images are under 5MB to ensure they load quickly.

### Testing User Stories
* **As a user, I want to create a Foodie account.**<br>
By navigating to http://foodie-project.herokuapp.com/ I can click 'Create one here' to open the register page and enter a username and password to create an account.  <br>
* **As a user, I want to log in to Foodie.**<br>
By navigating to http://foodie-project.herokuapp.com/ I can enter my account details to log in. Once I've logged in successfully, the 'All Recipes' page is displayed. <br>
I entered an incorrect password to test the login process and an incorrect username/password combination message is displayed. <br> <br>
**Error Handlers**:
At this point, I also tested the 404, 405 and 500 error handlers by adding the links to the html files manually to the URL. <br>

* **As a user, I want to navigate easily through the site.**
For this story I tested the links in the Materialize navbar and sidebars as well as the 'Back to Recipes' button on some of the pages. All worked correctly.
* **As a user, I want to view recipes that other users have shared, and view all details required to make a dish.**
"All recipe card 'View' buttons are clickable on the 'All Recipes' page, search results, and 'My Recipes' section for each recipe tested.<br>
All recipe details (that would have been submitted on the 'Add/Edit Recipe' pages are visible on the 'View Recipe' page for each of the recipes tested.
* **As a user, I want to search for specific recipes or recipes with specific ingredients or keywords.**
Results for recipe titles and specific ingredients or keywords display in a list when a term is entered into the search bar.
* **As a user, I want to add my own recipe.**
By navigating to the 'Add Recipe' page, I can add the details for a recipe along with a recipe image. If I don't fill a required field and try to submit the recipe, I see a prompt to fill out the field.
* **As a user, I want to view the recipes that I have added.**
I can view recipes I've added on the 'My Recipes' page, if I haven't added any recipes, there are links to browse recipes or add a recipe, and both are working correctly. 
* **As a user, I want to edit recipes that I have added.**
When I click edit on a recipe card for a recipe I've added, I can see the 'Edit Recipe' page with the recipe details in editable fields. If I change the content of a field or upload a new image file, the recipe is updated when I click 'Update Recipe'.
* **As a user, I want to delete recipes that I have added.**
I can click 'Delete' on a recipe card or the 'Edit Recipe' page for a recipe I've added to Foodie to remove the recipe from the app. I also checked the database to make sure the information was deleted. Initially I had not added any warning for the user and the recipes were deleted immediately so I added a modal prompting the user to confirm the action before anything is deleted for a better user experience.
* **As a user, I want to access the site from a desktop or laptop, and from a mobile device.**
The site is accessible from desktop, laptop and mobile device, and functions well on each device. I added some additional media queries to improve the display for smaller screen sizes.
* **As a user, I want to log out when I've finished browsing or adding recipes.**
Clicking 'Log Out' ends the user session and displays the login page. Note: I don't log out but closed the browser, the session will continue when I visit the site again. 


### Bugs
I encountered the following bugs during development of this project:
<br>

**Issue 1**
**Problem:** Materialize sidenav opened on mobile but it remained static and the options weren't clickable.
<br>

**Solution:**The navbar was set as 'fixed' and removing this class resolved the issue.
<br>

**Issue 2**
**Problem:**Selected options from the Allergens checkbox menu displayed in a string for the Edit and View pages.
<br>

**Solution:**I used the .getlist method to save and display them in a list.
<br>

**Issue 3**
**Problem:**When a user views a recipe from the My Recipes page, the Back to Recipes button takes the user back to the first page of the All Recipes page. 
<br>

**Proposed Solution:**I'd like to add context URL variables for the next release of the project to take the user back to the My Recipes page at that point. They can always access the My Recipes page using the navbar but I think it would improve the user experience.
<br>

**Issue 4**
**Problem:**The search bar was missing a 'Clear search' option so the user had to use the main navigation to return to the All Recipes page.
<br>

**Solution:**I've added a 'Reset' button which links back to the All Recipes page - I'd like to replace this with an icon placed in the search bar for the next release.
<br><br> 


## Deployment

### Local Deployment
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
8. Click 'Open App' at the top of the Heroku dashboard and the project will open in a new tab.<br><br>

## Credits and Acknowledgements

### Content and Media
* Recipe Content - All recipe content (text and images) is from [BBC goodfood](https://www.bbcgoodfood.com/) and for educational purposes only.

* Images - Two images from the project were downloaded from Unsplash: [Login and Register page image](https://unsplash.com/photos/XoByiBymX20) and [Recipe Image Placeholder](https://unsplash.com/photos/wtevVfGYwnM)
<br><br>

### Acknowledgements
I learned the key concepts of HTML, CSS, Python, and Javascript in the Code Institute course materials and read further material in [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and [MongoDB Documentation](https://docs.mongodb.com/) to improve my knowledge of Flask and MongoDB. <br>

I found information for some specific features used in the project from the following sources:
* [Login and Register Setup](https://www.youtube.com/watch?v=vVx1737auSE)
* [Sticky Footer](https://css-tricks.com/couple-takes-sticky-footer)
* [Flash Messages](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)
* [Delete Modal](https://www.w3schools.com/howto/howto_css_delete_modal.asp)
I used resources like [Stack Overflow](stackoverflow.com) and [W3Schools](w3schools.com) as well as the Code Institute Slack channels for help with troubleshooting smaller issues during the project. I got support from Code Institute tutors and great guidance from my mentor, Guido, throughout the project.<br><br>

--------

[Back to top](#Foodie)

