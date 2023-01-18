# **Faire**

Faire is a full-stack web application built to manage tasks in the form of a basic to-do list. It has CRUD functionality for registered users, and a username and password ensures data privacy. The user authentication system leveraged for this purpose is the contrib module included in django.contrib.auth., as Django is the web framework I used to write the app. 

This is my first full-stack development project and I've stuck to an MVP project plan to keep the different aspects of it managable. I used an Agile orientated approach to developing the product and my kanban board can be found in my repo as an attached GitHub project called 'Faire Kanban Board'.

The deployed site can be visited by clicking [**here**](https://faire.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://https://github.com/farah-maria/Faire).

I designed the app for submission as my 'Portfolio Project 4', part of the [**Code Institute Fullstack Software Development Diploma**](https://codeinstitute.net/ie/full-stack-software-development-diploma/). The aim of this project is to build a full-stack site based on business-oriented logic, used to control a centrally-owned dataset. A requirement is to set up an authentication mechanism and provide role-based access to the site's data, and for the site to be fully deployed for public use. The required technologies for the project are:

- HTML, CSS, JavaScript (JS not compulsory), Python+Django
- A relational database (recommending MySQL or PostgreSQL)

I have used PostgreSQL as my database management system, via ElephantSQL to install and manage the SQL database. I used Heroku to deploy the project, and GitHub for version control. 

The principles of UX (user experience) are based on business logic, and in this sense my app is based on business oriented logic despite it not being a paid for service. The Code Institute brief for this project does not outline a requirement for the integration of a payment system.

A full overview of the design and development of my app, including testing and code validation, is included below.

## **Table of Contents**

1. [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Design and Scope](#design-and-scope)
        * [Agile Approach](#agile-approach)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
        * [UI Design Changes](#ui-design-changes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        * [Base HTML](#base-html)
    - [Future Features](#future-features)

3. [Technologies Used - Full List](#technologies-used-list)

4. [Testing](#testing)
    - [Testing Devices](#testing-devices)
    - [Media Queries](#media-queries)
    - [Validation](#validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JavaScript](#javascript)
        * [Python](#python)
    - [Bugs](#bugs)

5. [Deployment](#deployment)
6. [Agile Reflections on Product Development](#agile-reflections)
7. [Acknowledgements & Credits](#acknowledgements-and-credits)
    - [Images](#images)
    - [Code](#code)


___

## **User Experience**
‘Faire’ is the French verb for ‘to do’, and this fits the idea of the site as a simple and functional yet stylish-looking app. The concept for it was minimalist from the outset, with just one image evoking a pen-and-paper feel to be used as the background, and fonts that reflect handwritten text.
The French theme extends to the use of the colours blue, white and red, from the French flag, for the logo. For the text, I continued the pen-and-paper theme to the use of just blue, red and black, which are the most commonly coloured pens (red for editing), as well as grey to suggest the colour of a graphite pencil. The colour scheme is consistent throughout the site, with the same logo at the head of each page, which also functions as a link to the main page/ home page. The navigation bar consists of the same logo and links for logging in and logging out on each page.
The app was designed with a mobile-first approach, given that most users access sites on their phones and a phone is most likely already used for entering and striking off a list of tasks for the day. However, the media queries (in my CSS file) also ensure the app looks pleasant and is functional on tablets and desktop computers.

![mock-up of site on different sized devices]( https://res.cloudinary.com/farahtasia/image/upload/v1674066441/amiresponsive_ol2omm.png)

### **User Stories**

There are only two user types – admin (with backend access to fix bugs etc) and all other users who register to use the app. The general user provides a username and password to access their data, and this also protects the privacy of their data.
The following user stories were created for the general user. Usage of the site is only possible by first registering an account via the login page.

1* As a **potential new user** I can **land on clear information about the purpose of the app at the start of my navigation journey on an ‘About’ page** so that **I know whether it is appropriate to my needs and decide whether I want to register or not**.

2* As a **new user** I can **register and account with an email address and password** so that **I can create a task list that is private to me and available each time I come back**.

3* As a **registered user** I can **log in to my account** so that **I can access my to-do list, which is private to me and not available to read for other users**.

4*  As a **registered user** I can **add new tasks** so that **my to-do list can be updated with new items**.

5* As a **registered user** I can **read a complete list of my to-do items** so that **I can remind myself of tasks I need to do**.

6*  As a **registered user** I can **edit my task details** so that **my to-do list items are not carrying mistakes and are kept up to date**.

7* As a **registered user** I can **delete tasks** so that **my task-list remains correct and up to date**.

8* As a **registered user** I can **cross off my tasks when they are completed** so that **my to-do list is up to date, and I can see what I’ve achieved**.

9* As a **user** I can **see whether I am logged in or not** so that **I don't forget my log-in status and can access appropriate info according to my status**.

10* As a **registered user** I can **press a button** so that **I can easily print off my to-do list in case my phone dies later!**.

11* As a **registered user** I can **search for my tasks by keyword** so that **I can access my list items with ease**.

12* As a **registered user** I can **reset my password** so that **I can safely make sure I can log-in if I've forgotten my log-in details**.


<br>

### **Design and Scope**
The scope of the project was to have a MVP with a few extras if time permitted, and I used the user stories as a guide for this.

#### Agile Approach

Each of the twelve user stories were written as ‘issues’ in Github and mapped to a Kanban Board (‘Faire Kanban Board’ attached as a Github project in my repository). Those user stories labelled  ‘must have’ for the MVP were mostly attached to the Github milestone that I named  ‘Iteration 1’, so that by the end of the first Agile sprint, a roughly workable app had been produced. The rest of the ‘must have’s were mapped to Iteration 2, so that an app with full CRUD functionality could be completed as soon as possible. The ‘should have’s were mapped to Iteration 2 or 3, so that they were completed after the must have functionalities were in place. Some of the ‘won’t have’ or ‘should have’ user story tasks were mapped to Iteration 3, in case I had time to complete all of the tasks for the full list of 12 user stories outlined above.  
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003570/userstoriesAgile_juoaoq.png" alt="Screenshot of user-stories/ issues in Github" width="60%"/></center>
<br>

The time-boxing aspect of Agile was approached by setting the due-date for each iteration in advance, taking into account how long I thought the steps took me when I was completing tutorials that taught the same skills (I took a bit of time off this, as I knew it would take me less time to code something that I'd already learnt to do).

#### Wireframes

The basic **wireframes** are available as eight PNG files; one which shows the initial log-in page, which is the first page that loads on the site. 

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003473/wire6_ndz5lw.png" alt="Wireframe for log in page, desktop version." width="60%"/></center>
<br>

If the user doesn’t have an account, there’s an option to sign-up, which leads to a sign-up page where the username and password are set. The fields will be set by Django’s automated system, but using crispy forms, if possible, to make the form look nicer.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674076847/signup_lbpkae.png" alt="Wireframe for log in page, mobile version." width="40%"/></center>
<br>

I envisaged all the mobile versions of each page as identical to the ones for desktop, but with the body text centred directly beneath the logo. The tablet layouts were planned as identical to the desktop ones.
The main page consists of the actual list of jobs to-do:

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1673890339/wire_psv5nw.png" alt="Wireframe for jobs list, mobile version." width="40%"/></center>
<br>

Here, there are the options to add jobs, delete them, read the details already saved for each job, and to edit them, by pressing on the appropriate icon.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1673890356/wire1_mcu5g7.png" alt="Wireframe for jobs list, desktop/ tablet version." width="60%"/></center>
<br>

By pressing on the ‘add a task here’ plus-sign icon, a job can be added by entering details into a form.

<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003353/wire3_keouey.png" alt="Wireframe for jobs form, mobile version." width="40%"/></center>
<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003500/wire7_ei5moa.png" alt="Wireframe for jobs form, desktop/ tablet version." width="60%"/></center>
<br>

By pressing the icon for reading the info for a job (from the jobs list page), a page comes up that shows the details entered regarding the job without the option of amending anything (it’s a read-only page). There’s a button for going back to the main jobs list page.

<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003447/wire4_scv5jo.png" alt="Wireframe for job details page, mobile version." width="40%"/></center>
<br>

The main jobs list also has an icon next to each task with the option of deleting the task. If the delete button is pressed, a confirmation page loads up to check if the user really wants to delete the item.

<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003434/wire5_ysdqtu.png" alt="Wireframe for deletion confirmation page, mobile version." width="40%"/></center>
<br>
The main jobs list also has an icon button next to each task that allows the user to update the details of the task, which includes the option of checking a box to indicate whether the task has been completed.
<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674003500/wire7_ei5moa.png" alt="Wireframe for the task update page, desktop/ tablet version." width="60%"/></center>
<br>

This could be the same page used to add a new job, as there’s a significant overlap in content. 
It would be great to have an ‘about’ home page right at the start, which would consist of the same logo/ login bar at the top and a block of text underneath, something like the job details page. I’ll see if I have time for this. I think that the navigation paths and basic concept of the website are/ is so simple that any user would be to use to ‘get it’ without instruction. If I have the time to go beyond the MVP, though, I will definitely add a home page that introduces the site to new visitors as this would help create a path of smooth navigation with the user aware of where the journey begins, and what features to expect.

####  Database Schema

I created the simplest possible database schema for my app, and the corresponding entity relationship diagram below was drawn using Lucid Charts early on in the planning phase. Beyond the units employed from Django, the one model (in models.py) that I created from scratch was the single model required for a to-do app in this case, which was for the jobs/ tasks created. I used class-based views, as taught in the Code Institute lessons on creating the blog ‘I think therefore I blog’ (in views.py).   

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1673890372/ERD_Faire_b5v04d.png" alt="Database schema in form of an Entity Relationship Diagram." width="60%"/></center>
<br>

#### UI Design Changes

I stuck to my brief, and the theme of pen and paper as well as a colour scheme inspired by the French Flag. I found a plain image that I used as the background for all of the site pages, and it's a detailed close-up of handmade paper. I felt that it added texture and warmth to what could be seen as a clinical app that ticks off tasks, but fits with the minimalist and hand-made feel.

The image is by 'Kiwihug' from Unsplash and can be found at https://unsplash.com/photos/y_2GC4EhOP4.

<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674085129/kiwihug-y_2GC4EhOP4-unsplash_1_tzbhk9.jpg" alt="Background image for the site." width="60%"/></center>
<br>

Sadly, I didn't have time to create an 'about' page or section for the site. 



