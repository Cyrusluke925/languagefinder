# **languagefinder**
## What is Language Finder?
Language Finder is a site where users can search the world and see what technologies are being most used around them. They can also submit languages or frameworks they use at their job if they have an account.

## Inspiration For This Project
At a meetup, I saw someone give a short presentation on their project which showed which networking events around you gave out free food. I thought it was an interesting project and a few days later while applying to jobs, a friend and I realized that there wasn't any type of map or site that we knew of which showed which languages or frameworks were being mostly used in our area. I thought it would be very useful, especially for fellow web developers looking for work. Thus, I decided to do this personal project.

## Technology Used
* Django 2.0.5 and Python
* PostgreSQL (Database Management System, used for storing app state, in this case the google markers)
* Google Maps Api
* JavaScript/JQuery
* HTML/CSS
* Pillow (media file uploader)

## Users
The target users are fellow software engineers who would like to contribute and know what technologies are being used around them.

## Features
* Can create an account on petpals with authentification.
* User will be able to see a search bar and map centered over USA. They can type any location into the field. It will then load the new location. If available, It will show markers, each representing a specific language or framework.

## User Story
 * A user will visit our homepage where they have an option to sign in or sign up from the displayed NAV Bar. 
   A map will be displayed.
   
* If a user is signed in, the Nav Bar will show an option to add a marker to the map. When the page is loaded, it will show a text field and a drop down menu letting you pick between three technologies (Ruby, Python, JavaScript) *NOTE: MORE OPTIONS WILL BE ADDED

## Future Features 
* More technologies and framework options
* A profile page
* Users will be able to post companies they work for
* There will be a system in place to prevent users from creating multiple markers.
* users will be able to connect with other users in a possible forums or 'friends list' way.
