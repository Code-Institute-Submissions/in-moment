# inMoment

If you are a young, striving and ambitious social-media influencer, looking for opportunities to expand your brand and business, then inMoment is just right for you. inMoment is a simple and modern way to gift your audience with a piece of your brand name. inMoment is not just a online shop, it is a great opportunity for your successful business.

## UX

Website was designed in favour of a younger generation with a fresh, simple and robust look. Suitable for people who strive easy access of product of their choice and a fast checkout without any queues.

### User Stories

* As a user I would like to see a nice home page with my idols moto on it.
* As a user I would like to scroll through all merchendise listed on a website.
* As a user I would like to sort all merchandise by category.
* As a user I would like to filter all merchandise by price and name.
* As a user I would like to search for a specific item.
* As a user I would like to have an option to sign up or login to website.
* As a user I would like to see my purchase history on my account page.
* As a user I would like to save my billing information on my account for future purchases.
* As a user I would like to have an option of unauthorized purchases.

### Owner Stories

* As an owner I would like to have full control of a website.
* As an owner I would like to have an option to add merchandise to a website.
* As an owner I would like to have an option to edit existing merchandise on a website.
* As an owner I would like to have an option to delete existing merchandise on a website.

## Features

* User can access home page by clicking on a header logo or menu item button.
* User can access all merchandise page blick clicking call to action button on home page or menu item button.
* User can create account on a website by clicking on a menu item button.
* User can login to a website by clicking on a menu item button.
* User can sort merchandise by category by clicking on a menu item button.
* User can search by accessing search bar on a header.
* User can filter merchandise by clicking on a filter field on top of merchandise showcase page.
* User can access merchandise detail page by clicking on a specific merchandise.
* User can add merchandise to their cart by clicking on add to cart button on merchandise detail view.
* User can specify the quantity of product he want to purchase on merchandise detail view.
* User can access theyre personal cart by clicking on a cart icon on top of the header.
* User can modify the quantity of a selected merchandise inside of a card by providing quantity and clicking on update button.
* User can remove item from shopping cart by clicking delete button.
* User can access checkout page by clicking on a checkout button in cart view.
* User can checkout straight on a website providing personal details and card details.
* User can see order information in the end of a checkout proccess.

* Owner can add, update and delete merchandise on website.

## Technologies Used

- [django](https://www.djangoproject.com/)
  - The project has been built with the **django** framework which provides, out of the box, authentication, routing, security and templating. It is based on the **Python** programming language and also benefits from the opensource community to grow in functionality and code reviews.
- [JQuery](https://jquery.com)
  - The project uses **JQuery** to simplify DOM manipulation.
- [Stripe](https://stripe.com/)
  - The project implements **Stripe Payments** to allow users to process payments over the platform.
- [Heroku](https://www.heroku.com/)
  - The project has been deployed to the **Heroku** platform that provides automatic deploys, as well as a Postgres database.
  
## Testing

This project does not include testing automation as most of the business logic is just data handling that is automatically performed by the django framework. Automating user actions and UI is better to be handled with the visual cues of a real human therefore all testing has been performed in the Manual Testing.

## Deployment

The project has been deployed to Heroku using Github In order to make it work the following environment variables must be defined:

- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET
- DATABASE_URL
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
