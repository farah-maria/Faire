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
        * [UI design choices & changes](#ui-design-choices)

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

