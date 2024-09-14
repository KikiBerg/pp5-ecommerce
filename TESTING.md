# Seed & Sprout - Testing

![Seed & Sprout shown on a variety of screen sizes](documentation/sesp-mockup.png)

Visit the deployed site: [Seed & Sprout](https://seedandsprout-ab1eae7ba537.herokuapp.com/)

Return back to the [README.md](README.md) file.

- - -

## AUTOMATED TESTING

### Code Validation

- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate all the Python files.
- [W3C](https://validator.w3.org/) was used to validate the HTML and CSS.
- [JSHint](https://jshint.com/) was used to validate the Javascript.

#### CI Python Linter
**`about app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| about/admin.py | ![screenshot](documentation/testing/validation/sesp-val-about-admin.png) | Passed. No warnings or errors |
| about/apps.py | ![screenshot](documentation/testing/validation/sesp-val-about-apps.png) | Passed. No warnings or errors |
| about/forms.py | ![screenshot](documentation/testing/validation/sesp-val-about-forms.png) | Passed. No warnings or errors |
| about/models.py | ![screenshot](documentation/testing/validation/sesp-val-about-models.png) | Passed. No warnings or errors |
| about/urls.py | ![screenshot](documentation/testing/validation/sesp-val-about-urls.png) | Passed. No warnings or errors |
| about/views.py | ![screenshot](documentation/testing/validation/sesp-val-about-views.png) | Passed. No warnings or errors |

**`bag app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| bag/apps.py | ![screenshot](documentation/testing/validation/sesp-val-bag-apps.png) | Passed. No warnings or errors |
| bag/contexts.py | ![screenshot](documentation/testing/validation/sesp-val-bag-contexts.png) | Passed. No warnings or errors |
| bag/urls.py | ![screenshot](documentation/testing/validation/sesp-val-bag-urls.png) | Passed. No warnings or errors |
| bag/views.py | ![screenshot](documentation/testing/validation/sesp-val-bag-views.png) | Passed. No warnings or errors |
| bag/views.py | ![screenshot](documentation/testing/validation/sesp-val-bag-bag_tools.png) | Passed. No warnings or errors |

**`checkout app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| checkout/admin.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-admin.png) | Passed. No warnings or errors |
| checkout/apps.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-apps.png) | Passed. No warnings or errors |
| checkout/forms.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-forms.png) | Passed. No warnings or errors |
| checkout/models.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-models.png) | Passed. No warnings or errors |
| checkout/signals.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-signals.png) | Passed. No warnings or errors |
| checkout/urls.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-urls.png) | Passed. No warnings or errors |
| checkout/views.py | ![screenshot](documentation/testing/validation/sesp-val-checkout-views.png) | Passed. No warnings or errors |
| checkout/webhook_handler.py| ![screenshot](documentation/testing/validation/sesp-val-checkout-webhook_handler.png) | Passed. No warnings or errors |
| checkout/webhooks.py| ![screenshot](documentation/testing/validation/sesp-val-checkout-webhooks.png) | Passed. No warnings or errors |

**`faqs app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| faqs/admin.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-admin.png) | Passed. No warnings or errors |
| faqs/apps.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-apps.png) | Passed. No warnings or errors |
| faqs/forms.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-forms.png) | Passed. No warnings or errors |
| faqs/models.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-models.png) | Passed. No warnings or errors |
| faqs/urls.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-urls.png) | Passed. No warnings or errors |
| faqs/views.py | ![screenshot](documentation/testing/validation/sesp-val-faqs-views.png) | Passed. No warnings or errors |

**`home app`**
File | Screenshot | Notes |
| --- | --- | --- |
| home/apps.py | ![screenshot](documentation/testing/validation/sesp-val-home-apps.png) | Passed. No warnings or errors |
| home/urls.py | ![screenshot](documentation/testing/validation/sesp-val-home-urls.png) | Passed. No warnings or errors |
| home/views.py | ![screenshot](documentation/testing/validation/sesp-val-home-views.png) | Passed. No warnings or errors |

**`newsletter app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| newsletter/admin.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-admin.png) | Passed. No warnings or errors |
| newsletter/apps.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-apps.png) | Passed. No warnings or errors |
| newsletter/forms.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-forms.png) | Passed. No warnings or errors |
| newsletter/models.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-models.png) | Passed. No warnings or errors |
| newsletter/urls.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-urls.png) | Passed. No warnings or errors |
| newsletter/views.py | ![screenshot](documentation/testing/validation/sesp-val-newsletter-views.png) | Passed. No warnings or errors |

**`products app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| products/admin.py | ![screenshot](documentation/testing/validation/sesp-val-products-admin.png) | Passed. No warnings or errors |
| products/apps.py | ![screenshot](documentation/testing/validation/sesp-val-products-apps.png) | Passed. No warnings or errors |
| products/forms.py | ![screenshot](documentation/testing/validation/sesp-val-products-forms.png) | Passed. No warnings or errors |
| products/models.py | ![screenshot](documentation/testing/validation/sesp-val-products-models.png) | Passed. No warnings or errors |
| products/urls.py | ![screenshot](documentation/testing/validation/sesp-val-products-urls.png) | Passed. No warnings or errors |
| products/views.py | ![screenshot](documentation/testing/validation/sesp-val-products-views.png) | Passed. No warnings or errors |
| products/widgets.py | ![screenshot](documentation/testing/validation/sesp-val-products-widgets.png) | Passed. No warnings or errors |

**`profiles app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| profiles/apps.py | ![screenshot](documentation/testing/validation/sesp-val-profiles-apps.png) | Passed. No warnings or errors |
| profiles/forms.py | ![screenshot](documentation/testing/validation/sesp-val-profiles-forms.png) | Passed. No warnings or errors |
| profiles/models.py | ![screenshot](documentation/testing/validation/sesp-val-profiles-models.png) | Passed. No warnings or errors |
| profiles/urls.py | ![screenshot](documentation/testing/validation/sesp-val-profiles-urls.png) | Passed. No warnings or errors |
| profiles/views.py | ![screenshot](documentation/testing/validation/sesp-val-profiles-views.png) | Passed. No warnings or errors |

**`seed_and_sprout`**
File | Screenshot | Notes |
| --- | --- | --- | 
| settings.py | ![screenshot](documentation/testing/validation/sesp-val-settings.png) | Passed. No warnings or errors |
| urls.py | ![screenshot](documentation/testing/validation/sesp-val-urls.png) | Passed. No warnings or errors |
| views.py | ![screenshot](documentation/testing/validation/sesp-val-views.png) | Passed. No warnings or errors |
| wsgi.py | ![screenshot](documentation/testing/validation/sesp-val-wsgi.png) | Passed. No warnings or errors |

#### W3C HTML Validator

Page | Screenshot | Notes |
| --- | --- | --- |
| **Homepage** | ![screenshot](documentation/testing/validation/val-html-home.png) | Passed. No warnings or errors |
| **Products page** | ![screenshot](documentation/testing/validation/val-html-products.png) | Passed. No warnings or errors |
| **Products add page** | ![screenshot](documentation/testing/validation/val-html-products_add.png) | Passed. No warnings or errors |
| **Products edit page** | ![screenshot](documentation/testing/validation/val-html-products_edit.png) | Passed. No warnings or errors |
| **Products delete page** | ![screenshot](documentation/testing/validation/val-html-products_delete.png) | Passed. No warnings or errors |
| **Products detail page** | ![screenshot](documentation/testing/validation/val-html-products_detail.png) | Passed. No warnings or errors |
| **Bag page** | ![screenshot](documentation/testing/validation/val-html-bag.png) | Passed. No warnings or errors |
| **Checkout page** | ![screenshot](documentation/testing/validation/val-html-checkout.png) | Passed. 1 warning, no errors |
| **Checkout success page** | ![screenshot](documentation/testing/validation/val-html-checkout_success.png) | Passed. No warnings or errors |
| **Faqs page** | ![screenshot](documentation/testing/validation/val-html-faqs.png) | Passed. No warnings or errors |
| **Faqs add page** | ![screenshot](documentation/testing/validation/val-html-faqs_add.png) | Passed. No warnings or errors |
| **Faqs edit page** | ![screenshot](documentation/testing/validation/val-html-faqs_edit.png) | Passed. No warnings or errors |
| **Faqs delete page** | ![screenshot](documentation/testing/validation/val-html-faqs_delete.png) | Passed. No warnings or errors |
| **Newsletter page** | ![screenshot](documentation/testing/validation/val-html-newsletter.png) | Passed. No warnings or errors |
| **About page** | ![screenshot](documentation/testing/validation/val-html-about.png) | Passed. No warnings or errors |
| **Profile page** | ![screenshot](documentation/testing/validation/val-html-profile.png) | Passed. No warnings or errors |
| **Signup page** | ![screenshot](documentation/testing/validation/val-html-signup.png) | Error: "Element ul not allowed as child of element small in this context." I ignored this error, as it is a known one from the latest versions of allauth |
| **Signin page** | ![screenshot](documentation/testing/validation/val-html-login.png) | Passed. No warnings or errors |
| **Signout page** | ![screenshot](documentation/testing/validation/val-html-logout.png) | Passed. No warnings or errors |

#### W3C CSS Validator

File | Screenshot | Notes |
| --- | --- | --- |
| **base.css** | ![screenshot](documentation/testing/validation/val-css-base.png) | Passed. No errors |
| **bag.css** | ![screenshot](documentation/testing/validation/val-css-bag.png) | Passed. No errors |
| **checkout.css** | ![screenshot](documentation/testing/validation/val-css-checkout.png) | Passed. No errors |
| **faqs.css** | ![screenshot](documentation/testing/validation/val-css-faqs.png) | Passed. No errors |
| **home.css** | ![screenshot](documentation/testing/validation/val-css-home.png) | Passed. No errors |
| **products.css** | ![screenshot](documentation/testing/validation/val-css-products.png) | Passed. No errors |
| **product_detail.css** | ![screenshot](documentation/testing/validation/val-css-products_detail.png) | Passed. No errors |
| **profile.css** | ![screenshot](documentation/testing/validation/val-css-profile.png) | Passed. No errors |

#### JSHint Javascript Validator

File | Screenshot | Notes |
| --- | --- | --- |
| **stripe_elements.js** | ![screenshot](documentation/testing/validation/val-js-stripe_elements.png) | Warnings about: 'const', 'let in ES6', 'arrow function syntax', 'template literal syntax in ES6'. I ignored these warnings. |
| **accordion.js** | ![screenshot](documentation/testing/validation/val-js-accordion.png) | Warnings about: 'const', 'let in ES6', 'arrow function syntax', 'template literal syntax in ES6'. I ignored these warnings. |
| **countryfield.js** | ![screenshot](documentation/testing/validation/val-js-countryfield.png) | Warnings about: 'const', 'let in ES6', 'arrow function syntax', 'template literal syntax in ES6'. I ignored these warnings. |

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

| Page | Screenshot |
| --- | --- | 
| **about** | ![screenshot](documentation/testing/lighthouse/sesp-lh-about.png) | 
| **accounts login** | ![screenshot](documentation/testing/lighthouse/sesp-lh-accounts_login.png) | 
| **accounts logout** | ![screenshot](documentation/testing/lighthouse/sesp-lh-accounts_logout.png) | 
| **accounts signup** | ![screenshot](documentation/testing/lighthouse/sesp-lh-accounts_signup.png) | 
| **bag** | ![screenshot](documentation/testing/lighthouse/sesp-lh-bag.png) | 
| **checkout_success** | ![screenshot](documentation/testing/lighthouse/sesp-lh-checkout_success.png) |
| **checkout** | ![screenshot](documentation/testing/lighthouse/sesp-lh-checkout.png) |
| **faqs_add** | ![screenshot](documentation/testing/lighthouse/sesp-lh-faqs_add.png) |
| **faqs_delete** | ![screenshot](documentation/testing/lighthouse/sesp-lh-faqs_delete.png) |
| **faqs_edit** | ![screenshot](documentation/testing/lighthouse/sesp-lh-faqs_edit.png) |
| **faqs** | ![screenshot](documentation/testing/lighthouse/sesp-lh-faqs.png) |
| **home** | ![screenshot](documentation/testing/lighthouse/sesp-lh-home.png) |
| **newsletter_signup.png** | ![screenshot](documentation/testing/lighthouse/sesp-lh-newsletter_signup.png) |
| **products_add** | ![screenshot](documentation/testing/lighthouse/sesp-lh-products_add.png) |
| **products_delete** | ![screenshot](documentation/testing/lighthouse/sesp-lh-products_delete.png) |
| **products_detail** | ![screenshot](documentation/testing/lighthouse/sesp-lh-products_detail.png) |
| **products_edit** | ![screenshot](documentation/testing/lighthouse/sesp-lh-products_edit.png) |
| **products** | ![screenshot](documentation/testing/lighthouse/sesp-lh-products.png) |
| **profile** | ![screenshot](documentation/testing/lighthouse/sesp-lh-profile.png) |

- - -

### Responsiveness
- I have tested my deployed project on multiple devices to check for responsiveness issues. No issues were found.
- Apart from the Chrome Devtools, I've used [this site](https://techsini.com/multi-mockup/index.php) to quickly check responsiveness on different devices and get screenshots for the testing.md file.

`Home Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-home.png)| Works as expected |

`Products Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-products.png)| Works as expected |

`Products detail Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-products_detail.png)| Works as expected |

`Faqs Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-faqs.png)| Works as expected |

`About Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-about.png)| Works as expected |

`Newsletter Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-newsletter.png)| Works as expected |

`Login Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-login.png)| Works as expected |

`Sign up Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-signup.png)| Works as expected |

`404 Page`
| Screenshot | Notes |
| --- | --- |
| ![screenshot](documentation/testing/responsiveness/val-resp-404.png)| Works as expected |

- For the pages that are profile and authentication safe, I needed to take the screenshots myself as the links would not appear on techsini site.
- I took fullsize screenshots on small and medium screens.

`Bag Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-bag-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-bag-ipad.png)
</details>

`Checkout Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-checkout-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-checkout-ipad.png)
</details>

`Checkout Success Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-checkout_success-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-checkout_success-ipad.png)
</details>

`Product Add Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-products_add-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-products_add-ipad.png)
</details>

`Product Edit Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-products_edit-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-products_edit-ipad.png)
</details>

`Product Delete Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-products_delete-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-products_delete-ipad.png)
</details>

`Faqs Add Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![faqs add page](documentation/testing/responsiveness/val-resp-faqs_add-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-faqs_add-ipad.png)
</details>

`Faqs Edit Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-faqs_edit-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-faqs_edit-ipad.png)
</details>

`Faqs Edit Confirm Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-faqs_edit_confirm-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-faqs_edit_confirm-ipad.png)
</details>

`Faqs Delete Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-faqs_delete-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-faqs_delete-ipad.png)
</details>

`Profile Page`
<details>
<summary>Small (IPhone 12 Pro)</summary>

![post detail page](documentation/testing/responsiveness/val-resp-profile-mob.png)
</details>

<details>
<summary>Medium (IPad Air)</summary>
    
![post detail page](documentation/testing/responsiveness/val-resp-profile-ipad.png)
</details>

- - -

### Browser Compatibility

I have tested my deployed project on two different browsers to check for compatibility issues. I could not find any issues.

|  Browser | Links  | Pages  | Responsivnes  | Form fields  |
| --- | --- | --- | --- | --- |
|  Chrome | Works as expected  |  Loading pages no issue | Responsivness works as expected  | Works as expected  |
|  Edge |  Works as expected | Loading pages no issue  | Responsivness works as expected  |  Works as expected |

- - -

## MANUAL TESTING

### Testing Purchase Procedure
Action |  Expected result | Pass
--- | --- | :---:
Click on 'All Products' |  All products are displayed on the page | &check;
Choose product, click on image or 'More Info' button |  Single product is displayed on the page with description & specifications | &check;
Click + on quantity |  Quantity of product increases | &check;
Click - on quantity |  Quantity of product decreases | &check;
Click 'add to bag' |  Product is added to shopping bag, success message is shown to the user | &check;
Click on the 'basket' icon in the navigation menu|  Redirected to shopping bag template, with products in it | &check;
Click + on quantity |  Quantity of product increases | &check;
Click - on quantity |  Quantity of product decreases | &check;
Click 'refresh' icon |  Quantity of products have been updated | &check;
To remove product, click 'remove'|  Product is removed from shopping bag| &check;
Click 'checkout'|  Redirected to checkout page | &check;
Fill in all form details |  No errors displayed on the form | &check;
In payment section input 4242 4242 4242 4242 and random date, cvc, zip & click complete order button | Payment went through, preview of purchase is displayed | &check;
Check email |  Email comfirmation has been sent | &check;
<details>
<summary>Order comfirmation</summary>
    
![order comfirmation](documentation/testing/purchase/sesp-order_conf.png)
</details>

<details>
<summary>Stripe</summary>
    
![order comfirmation](documentation/testing/purchase/sesp-stripe_conf.png)
</details>

<details>
<summary>Email comfirmation</summary>
    
![order comfirmation](documentation/testing/purchase/sesp-email_conf.png)
</details>


### Testing User Stories
Here's a table for testing the various user stories of the project. The aim is to follow up the functionality implementation.

| Title | User Story | Response | 
| --- | --- | --- |
| View a list of products | As a **shopper**  I want to be able to **view a list of products** so that I can **select some to purchase** |![screenshot](documentation/testing/userstories/sesp-ustest-01.png) |
| View individual product details | As a **shopper**  I want to be able to **view individual product details** so that I can **identify the price, description, product rating & product image** |![screenshot](documentation/testing/userstories/sesp-ustest-02.png) |
| View total of my purchase | As a **shopper**  I want to be able to **easily view the total of my purchases at any time** so that I can **avoid spending too much** |![screenshot](documentation/testing/userstories/sesp-ustest-03.png) |
| View specific category of products | As a **shopper**  I want to be able to **view a specific category of products** so that I can **quickly find products I'm interested in without having to search through all products** |![screenshot](documentation/testing/userstories/sesp-ustest-04.png) |
| Register for an account | As a **site user**  I want to be able to **easily register for an account** so that I can **have a personal account & be able to view my profile** |![screenshot](documentation/testing/userstories/sesp-ustest-05.png) |
| Login & logout | As a **site user**  I want to be able to **easily login & logout** so that I can **access my personal account information** |![screenshot](documentation/testing/userstories/sesp-ustest-06.png) |
| Recover password | As a **site user**  I want to be able to **easily recover my password in case I forget it** so that I can **recover access to my account** |![screenshot](documentation/testing/userstories/sesp-ustest-07.png) |
| Email confirmation | As a **site user**  I want to be able to **receive an email confirmation after registering** so that I can **verify that my account registration was successful** |![screenshot](documentation/testing/userstories/sesp-ustest-08.png) |
| User profile | As a **site user**  I want to be able to **have a personalized user profile** so that I can **view my personal order history, order confirmations & save my payment information** |![screenshot](documentation/testing/userstories/sesp-ustest-09.png) |
| Sort available products | As a **shopper**  I want to be able to **sort the list of available products** so that I can **easily identify the best rated & best priced sorted products** |![screenshot](documentation/testing/userstories/sesp-ustest-10.png) |
| Sort specific category | As a **shopper**  I want to be able to **sort a specific category** so that I can **find the best-priced or best-rated product in a specific category or sort the products in that category by name** |![screenshot](documentation/testing/userstories/sesp-ustest-11.png) |
| Sort multiple categories | As a **shopper**  I want to be able to **sort multiple product categories simultaneously** so that I can **find the best-priced or best-rated products across broad categories** | ![screenshot](documentation/testing/userstories/sesp-ustest-12.png) |
| Search by name or description | As a **shopper**  I want to be able to **search for a product by name or description** so that I can **find a specific product I'd like to purchase** |![screenshot](documentation/testing/userstories/sesp-ustest-13.png) |
| Search overview | As a **shopper**  I want to be able to **easily overview what I've searched for & the number of the results** so that I can **quickly decide whether the product I want is available** |![screenshot](documentation/testing/userstories/sesp-ustest-14.png) |
| Select quantity | As a **shopper**  I want to be able to **select the quantity of a product when purchasing it** so that I can **ensure I don't accidentally select the wrong product or quantity** |![screenshot](documentation/testing/userstories/sesp-ustest-15.png) |
| View bag items | As a **shopper**  I want to be able to **view my bag items** so that I can **identify the total cost of my purchase and all items I will receive** |![screenshot](documentation/testing/userstories/sesp-ustest-16.png) |
| Adjust quantity of specific items | As a **shopper**  I want to be able to **adjust the quantity of specific items in my bag** so that I can **easily make changes to my purchase before checkout** |![screenshot](documentation/testing/userstories/sesp-ustest-17.png) |
| Enter payment information | As a **shopper**  I want to be able to **easily enter my payment information** so that I can **checkout effectively** |![screenshot](documentation/testing/userstories/sesp-ustest-18.png) |
| Order confirmation | As a **shopper** I want to be able to **view an order confirmation after checkout** so that I can **verify that I haven't made mistakes** |![screenshot](documentation/testing/userstories/sesp-ustest-19.png) |
| Add a product | As a **store owner** I want to be able to **add a product** so that I can **add new items to my store** |![screenshot](documentation/testing/userstories/sesp-ustest-20.png) |
| Update a product | As a **store owner** I want to be able to **update a product** so that I can **change product prices, descriptions, images & other criteria** |![screenshot](documentation/testing/userstories/sesp-ustest-21.png) |
| Delete a product | As a **store owner** I want to be able to **delete a product** so that I can **remove items that are no longer for sale** |![screenshot](documentation/testing/userstories/sesp-ustest-22.png) |
| Subscribe to newsletter | As a **site user** I want to be able to **subscribe to a newsletter by providing my email address** so that I can **get updates about new products** |![screenshot](documentation/testing/userstories/sesp-ustest-23.png) |
| Manage subscriber list | As a **site admin** I want to be able to **view and manage the list of newsletter subscribers** so that I can **send newsletters periodically** |![screenshot](documentation/testing/userstories/sesp-ustest-24.png) |
| View FAQs list | As a **site user** I want to be able to **view a list of FAQs grouped by categories** so that I can **more easily find answers to my questions** |![screenshot](documentation/testing/userstories/sesp-ustest-25.png) |
| Add FAQs list | As a **site admin** I want to be able to **add new FAQs** so that I can **follow up questions from customers** |![screenshot](documentation/testing/userstories/sesp-ustest-26.png) |
| Update FAQs list | As a **site admin** I want to be able to **edit existing FAQs** so that I can **keep the section up to date** |![screenshot](documentation/testing/userstories/sesp-ustest-27.png) |
| Delete FAQs list | As a **site admin** I want to be able to **delete FAQs** so that I can **remove questions that are no longer for relevant** |![screenshot](documentation/testing/userstories/sesp-ustest-28.png) |

- - -

### Defensive Programming

#### Navigation Menu
| Feature | Tested? | Action | Expected Outcome | Pass/Fail | Screenshots |
| --- | --- | --- | --- | --- | --- | 
| Sign In Link | Yes | Click on "Login" from the dropdown menu | User is redirected to the Sign In page, displaying the Sign In form & Home & Sign In buttons. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-003.png)|
| Sign Up Link | Yes | Click on "Register" from the dropdown menu | User is redirected to the Sign Up page, displaying the Sign Up form, Back to Login & Create Account Buttons. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-004.png)|
| Sign Out Link | Yes | Click on "Logout" from the dropdown menu | User is redirected to the Sign Out page, displaying the Sign Out & Cancel button. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-001.png)|
| My Profile | Yes | Click on "My Profile" from the dropdown menu | User is redirected to the Profile page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-002.png)|
| All Products Link | Yes | Click on "All Products" in the navigation bar | User is redirected to the main Products page, displaying the list of products. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-005.png)|
| All Products/By Price Link | Yes | Click on "All Products/By Price" in the navigation bar | User is redirected to the main Products page, displaying the list of products sorted by price. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-006.png)|
| All Products/By Rating Link | Yes | Click on "All Products/By Rating" in the navigation bar | User is redirected to the main Products page, displaying the list of products sorted by rating. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-007.png)|
| Vegetables Link | Yes | Click on "Vegetables/All Vegetable seeds" in the navigation bar | User is redirected to the main Products page, displaying only vegetable seed products. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-008.png)|
| Vegetables Link/By Name | Yes | Click on "Vegetables/By Name" in the navigation bar | User is redirected to the main Products page, displaying only vegetable seed products sorted by name. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-009.png)|
| Vegetables Link/By Sowing Season | Yes | Click on "Vegetables/By Sowing Season" in the navigation bar | User is redirected to the main Products page, displaying only vegetable seed products sorted by sowing Season. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-010.png)|
| Vegetables Link/By Harvest Season | Yes | Click on "Vegetables/By Harvest Season" in the navigation bar | User is redirected to the main Products page, displaying only vegetable seed products sorted by harvest Season. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-011.png)|
| Herbs Link | Yes | Click on "Herbs/All Herb seeds" in the navigation bar | User is redirected to the main Products page, displaying only herb seed products. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-012.png)|
| Herbs Link/By Name | Yes | Click on "Herbs/By Name" in the navigation bar | User is redirected to the main Products page, displaying only herb seed products sorted by name. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-013.png)|
| Herbs Link/By Lifespan | Yes | Click on "Herbs/By Lifespan" in the navigation bar | User is redirected to the main Products page, displaying only herb seed products sorted by lifespan. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-014.png)|
| Herbs Link/Sowing Season | Yes | Click on "Herbs/Sowing Season" in the navigation bar | User is redirected to the main Products page, displaying only herb seed products sorted by sowing Season. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-015.png)|
| Flowers Link | Yes | Click on "Flowers/All Flower seeds" in the navigation bar | User is redirected to the main Products page, displaying only flower seed products. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-016.png)|
| Flowers Link/By Name | Yes | Click on "Flowers/By Name" in the navigation bar | User is redirected to the main Products page, displaying only flower seed products sorted by name. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-017.png)|
| Flowers Link/By Lifespan | Yes | Click on "Flowers/By Lifespan" in the navigation bar | User is redirected to the main Products page, displaying only flower seed products sorted by lifespan. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-018.png)|
| Flowers Link/By Sowing Season | Yes | Click on "Flowers/By Sowing Season" in the navigation bar | User is redirected to the main Products page, displaying only flower seed products sorted by sowing Season. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-019.png)|
| Garden Supplies Link | Yes | Click on "Garden Supplies/All Garden Supplies" in the navigation bar | User is redirected to the main Products page, displaying only garden supplies products. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-020.png)|
| Garden Supplies Link/By Category | Yes | Click on "Garden Supplies/By Category" in the navigation bar | User is redirected to the main Products page, displaying only garden supplies products sorted by category. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-021.png)|
| FAQS Link | Yes | Click on "FAQS" in the navigation bar | User is redirected to the FAQS page. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-022.png)|
| About us Link | Yes | Click on "About us" in the navigation bar | User is redirected to the About page. | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-023.png)|

#### Products Page

*NOTE!* For the sorting feature I have taken screenshots of only 1 type of sorting, but have tested all 8 of them and they work as expected.

| Feature | Tested? | Action | Expected Outcome | Pass/Fail | Screenshots |
| --- | --- | --- | --- | --- | --- | 
| Sorting bar | Yes | Click on the various choices to sort accordignly | The products are sorted accordignly | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-024.png)|
| All Products link | Yes | Click on the All Products link | You are directed back to the main Products page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-025.png)|
| Showing nr or products | Yes | Click on a random link, e.g. Vegetables/ By Name | The number of products showing is refreshed accordingly | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-026.png)|
| Scroll-to-top button | Yes | Scroll further down the products page | Scroll-to-top button appears & by clicking you're directed back to the top of the page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-027.png)|
| More Info Button | Yes | Click the "More Info" button | You're directed to the Products Detail Page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-028.png)|

#### Products Detail Page

*NOTE!* The decrement button only starts working normally after entering a value manually. This is identified as a bug.

| Feature | Tested? | Action | Expected Outcome | Pass/Fail | Screenshots |
| --- | --- | --- | --- | --- | --- | 
| Increment button | Yes | Click on the increment button | The quantity increases | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-029.png)|
| Decrement button | Yes | Click on the decrement button | The quantity decreases | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-030.png)|
| Keep Shopping button | Yes | Click on the "Keep Shopping" button | You get redirected back to the main Products page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-031.png)|
| Add To Bag button | Yes | Click on the "Add To Bag" button | You get directed to the Bag page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-032.png)|
| Success Message upon adding to bag | Yes | Click on the "Add To Bag" button | You get a Success Message with summed up info for your current basket | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-033.png)|
| Checkout link on success message | Yes | Click on the "Checkout" button | You get directed to the Bag Page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-034.png)|

#### Bag Page

| Feature | Tested? | Action | Expected Outcome | Pass/Fail | Screenshots |
| --- | --- | --- | --- | --- | --- | 
| Increment button | Yes | Click on the increment button | The quantity increases | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-035.png)|
| Decrement button | Yes | Click on the decrement button | The quantity decreases | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-036.png)|
| Update button | Yes | Click on the Update icon upon changing the quantity | The basket is refreshed accordingly & the relevant success message appears | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-037.png)|
| Remove button | Yes | Click on the Rubbish icon upon | The item is removed & the relevant success message appears | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-038.png)|
| Continue Shopping | Yes | Click on the "Continue Shopping" button after emptying the basket| You get redirected back to the main Products page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-039.png)|
| Totals | Yes | Add/Remove products or increase/decrease quantity of products | The Bag total, Deliver cost & Grand Total are updated accordingly | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-040.png)|
| Keep Shopping button | Yes | Click on the "Keep Shopping" button | You get redirected back to the main Products page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-041.png)|
| Checkout button  | Yes | Click on the "Checkout" button | You get directed to the Checkout Page | Pass |![screenshot](documentation/testing/fulltesting/sesp-ft-042.png)|


- - -

### Bugs
I am not sure if these can be identified as a bugs, but wanted to document them here in order to avoid confusion:
- On product detail page, the decrement button only starts working normally after entering a value manually. 
- Some of the fullsize screenshots for docmenting the features show the footer, or the free shipping banner where they shouldn't be. This is I guess a result of the fullsize screenshot function and should not be seen as mulfunctioning. The pages work as expexted.