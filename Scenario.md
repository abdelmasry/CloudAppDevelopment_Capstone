# Capstone Project

* A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.

* You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.

* After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

### Use cases for anonymous users:

* View the "Contact Us" page.
* View the "About Us" page.
* View the list of dealerships.
* Filter the list of dealerships by state.
* Click on a dealership to view the reviews for that dealership on the details page.
* Log in using their credentials.

### Use cases for authorized users: 
In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

* A Review button should be provided against each dealer listed in the dealership table.
* Clicking on the Review button should take the user to the review page.
* Filling the form on the review page and submitting it should add the review. 
```{ "user_id": 1, 

"name": "Berkly Shepley", => from Django "dealership": 15, => from the form "review": "Total grid-enabled service-desk", => form textbox "time": "", => current time "purchase": true, => form checkbox "purchase_date": "07/11/2020", => form calendar (bootstrap) "car_make": "Audi", => from django dropdown "car_model": "A6", => from django dropdown "car_year": 2010 => form django dropdown } 

```

* On submission, user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.

### Use cases for admin users:

* Log in to the admin site with a predefined username and password.
* Add new make, model, and other attributes.