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
    - [Future Features](#future-features)

3. [Technologies Used - Full List](#technologies-used-list)

4. [Testing](#testing)
    - [Testing Devices](#testing-devices)
    - [Media Queries](#media-queries)
    - [Testing Accessability](#lighthouse)
    - [Testing Code](#testing-code)
        * [HTML](#html)
        * [CSS](#css)
        * [Python](#python)
    - [Bugs](#bugs)

5. [Deployment](#deployment)
6. [Acknowledgements & Credits](#acknowledgements-and-credits)
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

I wrote my model early on, before the rest of the project, and decided that I wanted the list of jobs to have the uncompleted jobs at the top, to emphasise that they are to be prioritised, and struck off items at the bottom of the list.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674085809/models_vxgmtu.png" alt="model from models.py file." width="60%"/></center>
<br>

#### UI Design Changes

I stuck to my brief, and the theme of pen and paper as well as a colour scheme inspired by the French Flag. I found a plain image that I used as the background for all of the site pages, and it's a detailed close-up of handmade paper. I felt that it added texture and warmth to what could be seen as a clinical app that ticks off tasks, but fits with the minimalist and hand-made feel.

The image is by 'Kiwihug' from Unsplash and can be found at https://unsplash.com/photos/y_2GC4EhOP4.

<br>
<center><img src="https://res.cloudinary.com/farahtasia/image/upload/v1674085129/kiwihug-y_2GC4EhOP4-unsplash_1_tzbhk9.jpg" alt="Background image for the site." width="40%"/></center>
<br>

After creating a search box for the user to easily search the task they want to look up using keywords, I decided it was 
an unnecessary feature, because the list info is very basic and the app is optimised for a just a few items that can be viewed on a single page. If I extended the functionality of the app, with more details stored on each task, I would add a search box again. 

Sadly, I didn't have time to create an 'about' page or section for the site. 


## **Features**

There are six pages to the Faire app, with the addition of a page (the jobs list page) that appears altered with extra information on it for users that do not have any jobs on their list. There are a number of features I would like to add in future to improve the app beyond the MVP level.

### **Existing Features**
List of pages to the site:
1.	Log-in page, with a ‘Sign up here’ message in a different colour to redirect the user to the sign-up page. The following image is a screenshot of how the log-in page looks on my mobile phone, which is a Huawei P30 lite.
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674065347/mobileview_ahhh6f.jpg" alt="Log in page as it appears on my mobile phone – a Huawei P30 lite." width="60%"/></center>
<br>

2.	Sign-up page for new users. The fields were created by Django and I used crispy forms to improve the appearance of the form. The following image is the sign-up page as it appears on my Dell laptop. There’s a link for logging in at the bottom of the text area, in case the user is accidentally on this page and already has login details.
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674087822/signuphere_sho7dl.png" alt="Sign-up page as it appears on my Dell laptop." width="60%"/></center>
<br>

3.	Jobs list page, with CRUD functionalities indicated by icons that the user can click on to take them to other relevant pages. This is the homepage for logged in users. The image below shows the informational text that appears, with the trash/ delete icon turned red as the cursor hovers over it.

A message at the top tells the user how many incomplete tasks they have outstanding.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674088599/inconred_cordjt.png" alt="Jobs list page as it appears on my Dell laptop." width="60%"/></center>
<br>

ICONS ->

These are next to the list items and change colour from blue to red when the cursor hovers over them.
Magnifying glass icon takes user to the job details page (4). This displays information as a read-me only option. If the job has been ticked as done, an extra message appears at the bottom to say ‘This job is completed. Well done!”
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674089497/feedcat_mnn9zi.png" alt="job details, read-me only" width="60%"/></center>
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674089703/completed_hhkntg.png" alt="completed task message on screen" width="60%"/></center>
<br>

A trash icon takes user to ‘are you sure you want to delete?’ page (5), where user can either confirm or go back to the list of jobs. 

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674089940/suredelete_rl2zmb.png" alt="delete confirmation message" width="60%"/></center>
<br>

Pencil icon takes user to the add/ update page (6), where the user can complete or change information and tick a ‘done’ box if the task is completed. If the task is completed, it will appear as having a line drawn through it on the jobs list page. There is a ‘go back’ (to jobs list) link, in case the user changes their mind, and a ‘confirm’  button that saves the input information and updates the jobs list on the list page.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674090138/enterupdate_s57gg9.png" alt="enter and update form page" width="60%"/></center>
<br>

An add icon in a white circle on the with blue text next to it (‘add task here’) takes the user from the jobs list page to page 6 where a new job can be entered and saved. 
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674090347/addtast_npbnfn.png" alt="add task here" width="30%"/></center>
<br>

The logo at the top of every page is a link that goes back to the jobs list page.
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674090467/navbar_ohci5l.png" alt="logo and login" width="50%"/></center>
<br>
 
**If there are no jobs on the to do list, the jobs list page will display a message informing the user of this, and have an extra link included that takes the user to the add/ update form on page 6.**

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674090642/nojobs_z17foy.png" alt="no jobs message" width="50%"/></center>
<br>


**The login status of the user is reflected in the data available to the user on their navigation journey. If a user is logged in, a ‘hello, **username**’ message will be on the nav bar, with a link underneath for logging out if they want to. If the user is logged out, there is no login greeting, just the option to login, which appears as a link next to the logo. Data from the jobs on the lists is only available via the account that created the data, with the exception of the admin superuser who has access to the backend of the site.** 


The favicon is a royalty free image of a hand drawn clipboard, courtesy of Vector Stock, and can be found here: 
https://vectorstock.com/royalty-free-vector/hand-drawn-doodle-clipboard-icon-in-doodle-style-vector-34557850

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674091025/favicon_vloox0.jpg" alt="favicon" width="20%"/></center>
<br>

It works well, I think, with the minimalist and hand-written theme of the site. It also sticks to the existing colour palette. 

<br>

** Security Features & Admin User Functionality (backend) **

* User Authentication

I have used Django's LoginRequiredMixin to limit access based on permissions. Where the user isn’t passing user authentication due to an incorrect password and username, the following message in red will come up after attempted login:

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674094262/invalid_wbnuqa.png" alt="Login Failed Message" width="60%"/></center>
<br>

* Database Security

The Database URL and the secret key are in my env.py file so that no unwarranted access to the database is possiblle.

I have also used Cross-Site Request Forgery (CSRF) Tokens for my forms.


* Admin access

Django comes with admin control functionality, and the control panel is easy to use. It can be accessed for my app via: https://faire.herokuapp.com/admin/login/?next=/admin/  

There are options here to view content, change passwords, change permissions of different users, and generally look into different registered accounts as well as their authentication and authorisation settings.



### **Future Features**

Proposed future features:

1.	An ‘about’ page or section that introduces the app, its functionality, and the navigational paths/ structure.

2.	An easy ‘print this list’ button on the jobs list page. This could be done easily using JavaScript.

3.	Sign in options that use existing accounts with Facebook, Instagram and Google to make life easier for the user. I think, these days, people are tired of logging in to so many apps separately!


## **Technologies Used - Full List of Tech, Tools & Libraries Used**

* HTML
* CSS
* Django
* Heroku (for deployment)
* Google Chrome dev tools, including use of Lighthouse to check performance
* Bootstrap
* Python
* PostgreSQL
* ElephantSQL
* Crispy Forms
* Github
* Gitpod (IDE)
* Balsamiq (for wireframes)
* Cloudinary for storage of static files
* Am I Responsive? (site used for mock up images on different sized screens)
* HTML Code Checker (https://validator.w3.org)
* CSS Code Checker (https://jigsaw.w3.org/css-validator)
* The Code Institute's own Python Code Checker: PEP8CI (https://pep8ci.herokuapp.com/)
* Unsplash for images
* Font Awesome for icons
* Google Fonts for all fonts used
* Vector Stock for favicon
<br>

## **Testing**

### **Manual Testing of Features**

<br>
The following functionalities were manually tested by myself and a few friends using 
the deployed version on mobile phones and desktops.
<br>
<br>

#### **Header** (on all pages)

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Logo  	| Navigation Link               | Click On |   ✔       | 
|  LoggedIn greeting              | Text               | None |   ✔       |
|  Log in  	| Navigation Link & Text               | Click On |   ✔       | 
|  Log out  | Nav Link & Text                      | Click on |   ✔       |
Hover effect on log in and logout links | Turns darker blue & underline appears  | Hover |   ✔       | 

<br>

#### **Log in**

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Form - enter username  	| Text box with validation | Text input by user |   ✔       | 
|  Form - enter password    | Text box with validation | Text input by user |   ✔       |
|  Confirm button  	| Acceptance & redirect to Jobs List page or request to reenter info | Click On |   ✔     | 
|  Sign up option  | Nav Link                      | Click on |   ✔       |

#### **Sign up**

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Form - enter a username  	| Text box with advice on valid input | Input text/ nums/ symbols |   ✔       | 
|  Form - enter a password    | Text box with advice on valid input | Input text/ nums/ symbols |   ✔       |
|  Confirm button  	| Acceptance & redirect to Jobs List page or Rejection and request to reenter info | Click On |   ✔     | 
|  Log in option  | Nav Link                      | Click on |   ✔       |

<br>

#### **Jobs list page**

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Add task icon| Go to add job form | Click |   ✔       | 
|  See details icon (mag glass)| Read only text saved from previous input | Click |   ✔       |
|  Trash icon  	| Select deletion option for item on list a job, get redirected to confirmation page| Click |   ✔     | 
|  Text at top stating number of incomplete jobs  | Text updated from previous input  | None |   ✔       |
|  'No jobs in your list' text | Text generation from 0 jobs previously input  | None |   ✔       |
|  Extra 'Add a new task' option if no jobs on list  | Nav Link | Click on |   ✔       |
 Hover effect on icons and links  | Change in color for icons, underline appearance for links | Hover |   ✔       |

<br>


#### **Job details view page**

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Text, read only | All info on an individual job displayed, read only | None |   ✔       | 
|  Go back option| Nav link > job list page| Click |   ✔       |
 Hover effect on go back link  | Change in color and addition of underline | Hover |   ✔       |

<br>


#### **Add job/ Update job form** (it's the same page, form and url)

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Form - header field| Input max 210 characters for title of job | text input &  save |   ✔       | 
|  Form - info | Input  | Click |   ✔       |
|  Trash icon  	| Select deletion option for item on list a job, get redirected to confirmation page| Click |   ✔     | 
|  Text at top stating number of incomplete jobs  | Text updated from previous input  | None |   ✔       |
|  'No jobs in your list' text | Text generation from 0 jobs previously input  | None |   ✔       |
|  Extra 'Add a new task' option if no jobs on list  | Nav Link | Click on |   ✔       |
 Hover effect on icons and links  | Change in color for icons, underline appearance for links | Hover |   ✔       |

<br>

#### **Job details page**
<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Form - header field| Input max 210 characters for title of job | text input &  save |   ✔       | 
|  Form - info | Input text field for extra info on the job that needs doing  | text input & save |   ✔       |
|  Done?  	| Check/Tick box for when job done | Click to tick |   ✔     | 
|  Save | Button to save form input| Click on |   ✔       |
|  'No jobs in your list' text | Text generation from 0 jobs previously input  | None |   ✔       |
|  'Go back' option| Nav Link (directs back to jobs list)| Click on for redirect |   ✔       |
 Hover effect on 'go back' link | Turns darker blue & underline appears  | Hover |   ✔       | 

<br>

#### **Are you sure you want to delete? page (result of clicking on trash icon on jobs list)**

<br>

| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|  Tailored Text: 'Are you sure you want to delete....?'| Name of user's job will appear at end of sentence | None |   ✔       | 
|  'Yes, delete!' button| Confirmation button that will delete job| Click on - removes from jobs list |   ✔       |
|  'No, go back!'| Button that redirects back to jobs list | Click on > redirect |   ✔     | 
|  Hover effect on 'go back' link | Turns darker blue & underline appears  | Hover |   ✔       | 

<br>

### **Media Queries** & **Testing responsivity on different devices**

The app was tested on all main screen sizes from the smallest screen size of an iPhone 4 upwards. 
The use of Bootstrap meant very few media queries needed to be added in CSS to make the app layout work on 
different sized screens, especially as Bootstrap takes a mobile-first approach, so the app worked reasonably well on phone
screens without changes made.

The app also appears well enough on the Galaxy Fold phone.

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674065347/mobileview_ahhh6f.jpg" alt="mob phone view of app" width="40%"/></center>
<br>

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674065323/desktopview_txspuc.png" alt="desktop view of app" width="60%"/></center>
<br>

Media queries were added for the header bar and larger headings to still be in the expected place (left side of top of screen) with sufficient space around these items to look pleasant enough and readable on smaller phone screens. This was also done to maintain consistency in style with the desktop/ tablet appearance of the app and vice versa.

I used the Google Chrome dev tools to test the appearance of the app on the following devices in addition to the iPhone 4:

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674149041/responseSizes_okpsiv.png" alt="screen sizes
" width="40%"/></center>
<br>

Some of the smaller sizes do require more spacing to the left of the screen, and I would add this if time were available. For the time being, there is basic functionality on all screen sizes with the logos and headings still looking distinctive enough compared with the rest of the body text.

<br>

### **Testing Accessibility** **and Code Best Practice**

I focused on using colours with a high level of contrast for people with sign issues, and a soft coloured background so that
there is isn't a harsh glare from the screen.

I used the Lighthouse report app in Chrome dev tools to check that my app has a high accessibility score.

I also used Lighthouse to check that I have a high score for best practices, The best practice audit highlights opportunities to improve the overall code health of a web app.

*DESKTOP VERSION - LIGHTHOUSE REPORT*

<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674050784/Lighthouse_desk_wtknbq.png" alt="Lighthouse report on best practices and accessability for desktop version" width="60%"/></center>
<br>

*MOBILE VERSION - LIGHTHOUSE REPORT*
<br>
<center> <img src="https://res.cloudinary.com/farahtasia/image/upload/v1674050777/Lighthouse_isu1qy.png" alt="Lighthouse report on best practices and accessability for mobile version" width="40%"/></center>
<br>


### **Testing Code (Validation)**