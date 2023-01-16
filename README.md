# **Faire**

Faire is a full-stack web application built to manage tasks in the form of a basic to-do list. It has CRUD functionality for registered users, and a username and password ensures data privacy. The user authentication system leveraged for this purpose is the contrib module included in django.contrib.auth., as Django is the web framework I used to write the app. 

This is my first full-stack development project and I've stuck to an MVP project plan to keep the different aspects of it managable. I used an Agile orientated approach to developing the product and my kanban board can be found in my repo as an attached GitHub project called 'Faire Kanban Board'.

The deployed site can be visited by clicking [**here**](https://faire.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://https://github.com/farah-maria/Faire).

I designed the app for submission as my 'Portfolio Project 4', part of the [**Code Institute Fullstack Software Development Diploma**](https://codeinstitute.net/ie/full-stack-software-development-diploma/). The aim of this project is to build a full-stack site based on business-oriented logic, used to control a centrally-owned dataset. A requirement is to set up an authentication mechanism and provide role-based access to the site's data, and for the site to be fully deployed for public use. The required technologies for the project are:

- HTML, CSS, JavaScript, Python+Django
- A relational database (recommending MySQL or PostgreSQL)

I have used PostgreSQL as my database management system, via ElephantSQL to install and manage the SQL database. I used Heroku to deploy the project, and GitHub for version control. 

The principles of UX (user experience) are based on business logic, and in this sense my app is based on business oriented logic despite it not being a paid for service. The Code Institute brief for this project does not outline a requirement for the integration of a payment system.

A full overview of the design and development of my app, including testing and code validation, is included below.

## **Table of Contents**

1. [User Experience](#user-experience)
    - [User Stories](#user-stories)
    - [Design and Scope](#design-and-scope)
        * [Agile approach](#agile)
        * [Wireframes](#wireframes)
        * [Database Schema](#database-schema)
        * [UI design choices & changes](#ui-design-choices)

2. [Features](#features)
    - [Existing Features](#existing-features)
        * [Base HTML](#base-html)
    - [Future Features](#future-features)

3. [Technologies Used](#technologies-used)

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
