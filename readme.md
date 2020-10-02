# inMoment

inMoment is a small e-commerce website.

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



