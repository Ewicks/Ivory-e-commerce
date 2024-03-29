# Testing

Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2F) | ![screenshot](docs/images/html-validator-home.png) | Pass: No Errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fcontact) | ![screenshot](docs/images/html-validator-contact.png) | Pass: No Errors |
| Bag | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fbag) | ![screenshot](docs/images/html-validator-bag.png) | Pass: No Errors |
| Products | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fproducts) | ![screenshot](docs/images/html-validator-products.png) | Pass: No Errors |
| Checkout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fcheckout) | ![screenshot](docs/images/html-validator-checkout.png) | Pass: No Errors |
| Latest Drops | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fproducts%2Flatest_drops) | ![screenshot](docs/images/html-validator-latest-drops.png) | Pass: No Errors |
| Product | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Fproducts%2F2%2F) | ![screenshot](docs/images/html-validator-product.png) | Pass: No Errors |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Faccounts%2Flogin) | ![screenshot](docs/images/html-validator-login.png) | Pass: No Errors |
| Sign Up | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fivory-e-commerce.herokuapp.com%2Faccounts%2Fsignup) | ![screenshot](docs/images/html-validator-signup.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

![CSS Checker](docs/images/html-validator-css.png)

### Python Validation

## Flake8

Flake8 was used because pep8online.com website is down. Migrations errors remain as advised by Code Institute.

![Flake8](docs/images/flake8-validation.png)

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

Stripe JS
![Stripe JS](docs/images/stripe-js-validation.png)

Quantity button
![Quantity Button](docs/images/quantity-js-validation.png)

### Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](docs/images/home-page.png) | Works as expected |
| Chrome | ![screenshot](docs/images/checkout-success-page.png) | Works as expected |
| Chrome | ![screenshot](docs/images/chrome-mobile-products.png) | Works as expected |
| Safari | ![screenshot](docs/images/safari-product.png) | Minor CSS differences |
| Safari | ![screenshot](docs/images/safari-contact.png) | Works as expected |
| Safari | ![screenshot](docs/images/safair-home.png) | Works as expected |
| Firefox | ![screenshot](docs/images/firefox-products.png) | Works as expected |
| Firefox | ![screenshot](docs/images/safari-contact.png) | Works as expected |
| Firefox | ![screenshot](docs/images/safair-home.png) | Works as expected |


### Responsiveness

| Device | Screenshot | Notes |
| --- | --- | --- |
| Desktop | ![screenshot](docs/images/checkout-success-page.png) | Works as expected |
| Desktop | ![screenshot](docs/images/checkout-page.png) | Works as expected |
| Desktop | ![screenshot](docs/images/safair-home.png) | Works as expected |
| Tablet | ![screenshot](docs/images/safari-product.png) | Works as expected |
| Tablet | ![screenshot](docs/images/safair-home.png) | Works as expected |
| Tablet | ![screenshot](docs/images/safari-contact.png) | Works as expected |
| Mobile | ![screenshot](docs/images/mobile-checkout.png) | Works as expected |
| Mobile | ![screenshot](docs/images/mobile-bag.png) | Works as expected |
| Mobile | ![screenshot](docs/images/chrome-mobile-products.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](docs/images/lighthouse-mobile-home.png) | Slow response time |
| Home | Desktop | ![screenshot](docs/images/lighthouse-desktop-home.png) | Few warnings |
| Contact | Desktop | ![screenshot](docs/images/lighthouse-desktop-contact.png) | Some minor warnings |
| Contact | Mobile | ![screenshot](docs/images/lighthouse-desktop-contact.png) | Few warnings |
| Products | Desktop | ![screenshot](docs/images/lighthouse-desktop-products.png) | few warnings|
| Products | Mobile | ![screenshot](docs/images/lighthouse-mobile-products.png) | Slow response time |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Products Page | | | | |
| | Click on product takes user to product page | Pass | |
| | Load images | All images load as expected | Pass | |
| Latest Drop Page | | | | |
| | Click on product takes user to product page | Pass | |
| | Load images | All images load as expected | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to contact page | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| Bag | | | | |
| Click on delete and update buttons will delete or update item | Pass | |
| Click on secure checkout takes user to checkout page | Pass | |
| Checkout | | | | |
| Checkout forms requires all valid data | Pass | |
| Card details section only receives fake card number | Pass | |
| Click on complete order triggers process animation | Pass | |
| Click on complete order which then processes the order via stripe | Pass | |



## User Story Testing

| User Story | Link | Screenshot |
| --- | --- | --- |
| As a new site user, I would like to access the site on differing devices, so that I can interact with content on my preferred device. | [link](https://github.com/Ewicks/Ivory/issues/1) | ![Screenshot](docs/images/mobile-checkout.png) ![Screenshot](docs/images/safari-product.png) |
| As a new site user, I would like to press the back button if I get a 404 error page, so that I can easily go back to the website. | [link](https://github.com/Ewicks/Ivory/issues/3) | ![Screenshot](docs/images/404-btn.png) |
| As a new site user, I would like to view my recent orders, so that I can quickly check all the items that was ordered were the correct ones. | [link](https://github.com/Ewicks/Ivory/issues/5) | ![Screenshot](docs/images/order-history.png) |
| As a returning site user, I would like to be able to register for a newsletter. | [link](https://github.com/Ewicks/Ivory/issues/11) | ![Screenshot](docs/images/newsletter-register.png) |
| As a returning site user, I would like to view the product up close, so that I can make an informed decision to purchase. | [link](https://github.com/Ewicks/Ivory/issues/13) | ![Screenshot](docs/images/product.png) |
| As a returning site user, I would like to search for products by entering descriptive words, so that I can find what I want quickly. | [link](https://github.com/Ewicks/Ivory/issues/12) | ![Screenshot](docs/images/search-bar.png) |
| As a returning site user, I should be able to update my card details on my account and also view the saved card details. | [link](https://github.com/Ewicks/Ivory/issues/9) | ![Screenshot](docs/images/card-details-bar.png) |
| As a returning site user, I should be able to be able to view all items that will be purchased before I proceed to checkout. | [link](https://github.com/Ewicks/Ivory/issues/10) | ![Screenshot](docs/images/bag-items.png) |
| As a Site User I want to be able to register an account. | [link](https://github.com/Ewicks/Ivory/issues/8) | ![Screenshot](docs/images/register-account.png) |
| As a Superuser I can delete, edit or add posts to the website. All other user's do not have this access | [link](https://github.com/Ewicks/Ivory/issues/4) | ![Screenshot](docs/images/superuser-account.png) |
| As a Administrator I can view the messages that a user has sent via the contact us form so that I can get back to them answering queries they may have.. | [link](https://github.com/Ewicks/Ivory/issues/7) | ![Screenshot](docs/images/contact-msg.png) |
|  As a Superuser I can delete and add reviews on the front end so that it is quicker to update the reviews section  | [link](https://github.com/Ewicks/Ivory/issues/14) | ![Screenshot](docs/images/delete-review.png) |
|  As a site user I can send a message to the store so that I can get answers to any questions | [link](https://github.com/Ewicks/Ivory/issues/15) | ![Screenshot](docs/images/contact.png) |
|  As a Superuser I can edit how many items are in stock so that the store does not sell more items than we have in stock | [link](https://github.com/Ewicks/Ivory/issues/16) | ![Screenshot](docs/images/stock-levels.png) |

## Bugs


* There was an extra excess white space to the right of the screen, to fix this I placed a p-0 so there was no padding on the row the image was on.
![Bug](docs/images/white-space-bug.png)

* After migrating changes to the database, this error occurred, to fix this I deleted the database and created a new one by deleting all migrations and pycache files within the migrations folder. I also reset the database on ElephantSQL.
![Bug](docs/images/database-error.png)

* On the login and sign up pages, when the user inputted invalid data, the error message would appear and push the html elements down and under under the footer. This was becuase the space within the header and footer had a height of 60vh, this was forcing the height of the page so that the elements could not shift down without going underneath the footer.
![Bug](docs/images/overlap-elements-bug.png)

- explain mobile nav bug
- When the user opened the drop down navbar, the elements inside would overlap with the elements on the product page. To fix this I added a min-height to the navbar a min-height of 101px, before it was a height on 101px. The min-height prevents the navbar from shrinking in height creating overlapping issues.
![Bug](docs/images/mobile-nabar-bug.png)


- When I tried to open a local server via gitpod using the command "python3 manage.py runserver", the page would throw the below error. To fix this is I typed the command "pkill -9 python3" in the terminal. This command was ran to kill all instances of the port server.
![502 Error](docs/images/502-error.png)

- When the user is in mobile mode, the allauth pages content files half the page. To change this I added "col-12 col-md-6" to the column. This ensures that the contents take up half the page on medium devices and up and mobile devices and below the contents take up the whole page. 
![Bug](docs/images/mobile-allauth-bug.png)

- The homepage vertical line and image gets longer when the height of the device increases, while growing at different speeds leaving them to not be aligned. To fix this I gave the vertical line and image a min and max height so that when the device increases in height, the image and line stays the same length and does not increase.

- In the product page, the number of reviews was displaying the number of reviews for all products. I wanted to change the number so it displayed the number of reviews for that product so I added the code below.

Python -  ```
{{ product.reviews.all | length }}```

- Stripe only allows users to checkout with a balance more than £0.30, so whenever the total of items was less an error message would come up explaining this and they would not be allowed to checkout.

![Screenshot](docs/images/stripe-bug.png)


### GitHub **Issues**

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/Ewicks/Ivory/issues


## Unfixed Bugs

- Here the two elements side by side of the title Ivory are not centered like the title ivory is. I tried aligning the items center using flexbox.

![Bug](docs/images/unfixed-bug-header.png)
