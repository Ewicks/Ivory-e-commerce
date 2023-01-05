# Universal Blogs

## Introduction

Ivory is a modern clothing brand that is selling there stock via their online shop.

This website is for educational purposes only, the website is not setup to receive real payments, only fake payments are viable. 
To make a fake payment use the below credit card detials.


* 4242424242424242 (Visa)
* Expiration date = Any future date (Example: 12/24)
* CVN = any 3 digits (Example: 132)
* Postcode = any 5 digits (Example: 12345)

![Card Details](docs/images/card-details.png)

## Preview


### Live Website
To visit the deployed website click [here](https://ivory-e-commerce.herokuapp.com/)


# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Agile Development Process](#agile-development-process)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## UX User Experience
### User Stories

### Site Admin/Creator:


### Site User


## Agile Development Process



## Design
### Wireframes
<details>
  <summary>Click here to view all wireframes both Desktop & mobile:</summary>

  

  </details>


### Database Schema




## features 

### navbar

- I have created a simple narbar that has a creamy white theme to it. I have also created a mobile navbar that collapes to show a dropdown menu. The mobile menu replaces the main navbar for small to medium devices only.

![Navbar](docs/images/navbar.png)

![Mobile Navbar](docs/images/mobile-nabar.png)


### Home Page

- This page displays a model in stylish clothing alongside links to the latest drop page, products page and the contact page.

![Home Page](docs/images/home-page.png)


### Contact Page

- I used a basic boostrap template for the contact form.

![Contact Page](docs/images/contact-page.png)


### Edit Post

- When an admin is logged in, the links to edit and delete appear on each clothing post. They can change the details here with a click of a button.

![Edit Page](docs/images/edit-page.png)


### Signup Page

- If the user has already got an account, they can press the login link to be directed to the login page.

![Signup Page](docs/images/sign-up-page.png)

### Login Page

- If the user has not created an account, the details they use to log in will not work. Once they have an account they can have a profile.

![Login Page](docs/images/login-page.png)

### Admin Panel

![Admin Page](docs/images/admin-panel.png)


### 404 Error Page

- This page provides a link to direct them back to the website if user gets a  navigational page error.

![404 Error Page](doc/images/404-page.png)



### Future Features

- Allowing the user to filter posts by how many likes and comments each post has.

- Allow each user to only edit or delete the posts they created.

- Create a section where a user can donate money too support the ongoing publications.

### Bugs/Errors encountered during development

* Postgress database url link changed in Heroku on it's own, so I copied and pasted the new one into the env.py file.

* The blog post images was displaying locally but not in Heroku, so instead of using the dynamic image pathing, I uploaded the images to Cloudinary and used the url to display them within a if statement to get them working on Heroku.
![issue](doc/images/Image-path-bug.png)

* This is isn't a bug but I changed the add post and edit post views from class based views to function based views, becuase they are shorter, cleaner and works well in this instance. 

* Missing comma at the end of this line "STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]" in manage.py.

* When the user is using a smaller device, the row of images would become a column of images. I needed to swap the middle two div's around so that the step title was above the image where as in the image below it is below. I used to order porperty in the media query section to swap them around on 800px width.
![Issue](doc/images/about-swap-div.png)

* I used JavaScript so that when the user would hover over the bottom half of a post, the title would change color. This was only working for the first post, so I used CSS instead which is a easier way of doing this as seen in the image below
![Issue](doc/images/hover-title-issue.png)

* When the user clicks on the add post button, the form would display with the error This field is required on each field on the form when the user has not submitted the form yet. This was becuase in views.py addd_post function I was referencing 'post_form' before assignment. My function was not handling GET requests, so I added the else block to handle this, so that when the form loads without any errors because the user has not made a post request yet. See image belo

![Add_Post View](doc/images/addpost-view.png)

* When the user hovered over one of the navbar page elements that takes the user to a new page. For example, the blog button, all the page elements would move up 2 pixels when I hovered over one of them. To fix this I gave the class border-line a transparent border-bottom of 2px so that when the hover effect appears 2px border-bottom isn't added, instead it will be replaced with the red color via the hover css below.

![Hover issue](doc/images/hover-issue.png)


## Technologies Used

Languages Used
- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

Frameworks, Libraries & Programs Used

- [amiresponsive](https://ui.dev/amiresponsive) to display the responsive website image on different size devices.
- [Balsamiq](https://balsamiq.com) to create wireframes.
- [Cloudinary](https://cloudinary.com) used to upload, store, manage, minipulate and provide images.
- [Django](https://www.djangoproject.com) is a free open-source Python web framework that follows the model-template-views architectural pattern.
- [Font Awesome](https://fontawesome.com) used to display icons for asthetic purposes
- [Git](https://git-scm.com) is version control software which can be used via the Gitpod terminal to commit and push to GitHub
- [Github](https://github.com) is used to store projects containing code
- [Gitpod](https://www.gitpod.io) is a online IDE linked to the GitHub repository used to write this project
- [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) used for debugging code
- [Heroku](https://www.heroku.com) is used to deploy this project. Heroku is a cloud platform as a service supporting several programming languages.
- [JQuery](https://jquery.com/) is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation

## Testing

### The W3C Markup Validator

Home Page

![Home Page](doc/images/html-checker-index.png)
About Page

![About Page](doc/images/html-checker-about.png)

Blog Page
![Blog Page](doc/images/html-checker-blog.png)

Contact Page
![Contact Page](doc/images/html-checker-contact.png)

Signup Page
![Signup Page](doc/images/html-checker-signup.png)

Topic Page

![Topic Page](doc/images/html-checker-topic.png)

Search Posts Page
![Seach Posts Page](doc/images/html-checker-seachposts.png)

### CSS Validation

![CSS Checker](doc/images/css-checker.png)

### Python Validation

Here are the files within the Blog App.

Admin 
![Admin](doc/images/python-checker-admin.png)

Forms
![Forms](doc/images/python-checker-forms.png)

Models
![Models](doc/images/python-checker-models.png)

Urls
![Urls](doc/images/python-checker-urls.png)

Views
![Urls](doc/images/python-checker-views.png)

### Javascript Validation

Index Page

- I have used Jquery within this section which jshint does not account for.

![Index Page](doc/images/jshint-index.png)

Update Page

![Update Page](doc/images/jshint-update.png)

### Browser Compatibility

There are no Compatibility issues that I am aware of.

### Chrome

- Mobile Size
![Blog Page](doc/images/mobile-blog-chrome.png)

- Desktop Size
![Contact Page](doc/images/desktop-contact-chrome.png)

### Safari

- Tablet Size
![Blog Page](doc/images/tablet-blog-safari.png)

- Tablet Size
![Index Page](doc/images/tablet-index-safari.png)


### Responsiveness

There are no Responsiveness issues that I am aware of.

- Desktop
![Contact Page](doc/images/desktop-contact-chrome.png)

![Blog Page](doc/images/blog-desktop.png)

- Tablet Size

![Index Page](doc/images/tablet-index-safari.png)

![Blog Page](doc/images/tablet-blog-safari.png)

- Mobile Size

![Blog Page](doc/images/mobile-blog-chrome.png)

![About Page](doc/images/mobile-about.png)

### User Testing

- Users were sent to the website to try and break the website in some way by inputing invalid data where possible.
- They also had tasks to complete which are below
1. Register an account and create a blog post
2. Attempt to edit or delete another users post
3. Edit your own post
4. Delete you own post
5. search for posts that do not exit.

- Feedback from users was a success, however 1 common issue was that the user could not upload their own image. They chose a category image from the selected images available to get round this.

* Could not upload there own image

## Deployment

* Log in to [Heroku](https://id.heroku.com/login) or create an account
* On the main page click New and Create New App
* Note: new app name must be unique
* Next select your region, I chose Europe.
* Click Create App button
* Click in resources and select Heroku Postgres database
* Click Reveal Config Vars and add new config "SECRET_KEY"
* Click Reveal Config Vars and add new config "CLOUDINARY_URL"
* Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
* The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
* Next, go to Buildpack section click Add Buildpack select python and Save Changes
* Scroll to the top of the page and choose the Deploy tab
* Select Github as the deployment method
* Confirm you want to connect to GitHub
* Search for the repository name and click the connect button
* Scroll to the bottom of the deploy page and select the preferred deployment type
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github
* Create a requirements.txt in the root directory file so Heroku can install the packages needed.
* To update requirements.txt with all package installments type the command in the terminal "pip3 freeze --local > requirements.txt"
* To obtain the Postgres DATABASE_URL from Heroku, navigate to the resources tab in your app, under the title Add-ons search for Heroku Postgres, submit this option. The DATABASE_URL will be added to config bars automatically.
* To obtain a cloudinary key, navigate to your cloudinary accounts details under the Dashboard tab. Add the url to the cloudinary config var.
* In GitPod create a file called env.py in the root directory.
* Import os in the env.py file then type os.environ["WRITE_KEY_HERE"] = "VALUES_GO_HERE"
* Fill in the above line with the "SECRET_KEY", "CLOUDINARY_URL" AND "DATABASE_URL". The values for each key are found in the config vars in Heroku.


### Final Deployment 

* Create a runtime.txt `python-3.8.13`
* Create a Procfile `web: gunicorn heardit.wsgi`
* When development is complete change the debug setting to: `DEBUG = False` in settings.py
* In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
* In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

### Forking This Project

* Open [GitHub](https://github.com/Ewicks/universal-blogs-project-4)
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository
* Create a requirements.txt in the root directory file so Heroku can install the packages needed.
* To update requirements.txt with all package installments type the command in the terminal "pip3 freeze --local > requirements.txt"

### Cloning This Project

* Clone this project by following the steps:

* Open [GitHub](https://github.com/Ewicks/universal-blogs-project-4)
* You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
* Once you click the button the fork will be in your repository
* Open a new terminal
* Change the current working directory to the location that you want the cloned directory
* Type 'git clone' and paste the URL copied in step 3
* Press 'Enter' and the project is cloned
* Create a requirements.txt in the root directory file so Heroku can install the packages needed.
* To update requirements.txt with all package installments type the command in the terminal "pip3 freeze --local > requirements.txt"


## Credits

* Code Institute "I think therefore i blog" - Django blog project Walkthrough
* Codemy.com blog post tutorials using django - [Youtube playlist](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
* W3Schools, youtube clips and stackoverflow resources helped my throughout the project
* [link](https://www.youtube.com/watch?v=h_Uv_9OxA2k) to video for typewriter effect
* Images were taken from [Google Images](https://images.google.com/)


## Acknowledgements
* I used Code Institute's material in the Full Stack Development course.
* W3Schools, youtube clips and stackoverflow resources helped my throughout the project
* Tim - Code Institute mentor

This project is for educational use only and was created for the Code Institute Module.

Created by Ethan Wicks

