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
| products/views.py | ![screenshot](documentation/testing/validation/val-pl-about-views.png) | Passed. No warnings or errors |
| products/widgets.py | ![screenshot](documentation/testing/validation/val-pl-about-views.png) | Passed. No warnings or errors |

**`profiles app`**
File | Screenshot | Notes |
| --- | --- | --- | 
| profiles/admin.py | ![screenshot](documentation/testing/validation/val-pl-about-admin.png) | Passed. No warnings or errors |
| profiles/apps.py | ![screenshot](documentation/testing/validation/val-pl-about-apps.png) | Passed. No warnings or errors |
| profiles/forms.py | ![screenshot](documentation/testing/validation/val-pl-about-forms.png) | Passed. No warnings or errors |
| profiles/models.py | ![screenshot](documentation/testing/validation/val-pl-about-models.png) | Passed. No warnings or errors |
| profiles/urls.py | ![screenshot](documentation/testing/validation/val-pl-about-urls.png) | Passed. No warnings or errors |
| profiles/views.py | ![screenshot](documentation/testing/validation/val-pl-about-views.png) | Passed. No warnings or errors |

**`seed_and_sprout`**
File | Screenshot | Notes |
| --- | --- | --- | 
| settings.py | ![screenshot](documentation/testing/validation/val-pl-settings.png) | Passed. No warnings or errors |
| urls.py | ![screenshot](documentation/testing/validation/val-pl-urls.png) | Passed. No warnings or errors |
| views.py | ![screenshot](documentation/testing/validation/val-pl-urls.png) | Passed. No warnings or errors |
| wsgi.py | ![screenshot](documentation/testing/validation/val-pl-wsgi.png) | Passed. No warnings or errors |

#### W3C HTML Validator

Page | Screenshot | Notes |
| --- | --- | --- |
| **Homepage** | ![screenshot](#) | Passed. No warnings or errors |
| **Products page** | ![screenshot](#) | Passed. No warnings or errors |
| **Products add page** | ![screenshot](#) | Passed. No warnings or errors |
| **Products edit page** | ![screenshot](#) | Passed. No warnings or errors |
| **Products delete page** | ![screenshot](#) | Passed. No warnings or errors |
| **Products detail page** | ![screenshot](#) | Passed. No warnings or errors |
| **Bag page** | ![screenshot](#) | Passed. No warnings or errors |
| **Checkout page** | ![screenshot](#) | Passed. No warnings or errors |
| **Checkout success page** | ![screenshot](#) | Passed. No warnings or errors |
| **Faqs page** | ![screenshot](#) | Passed. No warnings or errors |
| **Faqs add page** | ![screenshot](#) | Passed. No warnings or errors |
| **Faqs edit page** | ![screenshot](#) | Passed. No warnings or errors |
| **Faqs delete page** | ![screenshot](#) | Passed. No warnings or errors |
| **About page** | ![screenshot](#) | Passed. No warnings or errors |
| **Profile page** | ![screenshot](#) | Passed. No warnings or errors |
| **Signup page** | ![screenshot](#) | Passed. No warnings or errors |
| **Signin page** | ![screenshot](#) | Passed. No warnings or errors |
| **Signout page** | ![screenshot](#) | Passed. No warnings or errors |

#### W3C CSS Validator

File | Screenshot | Notes |
| --- | --- | --- |
| **base.css** | ![screenshot](#) | Passed. No warnings or errors |
| **bag.css** | ![screenshot](#) | Passed. No warnings or errors |
| **checkout.css** | ![screenshot](#) | Passed. No warnings or errors |
| **faqs.css** | ![screenshot](#) | Passed. No warnings or errors |
| **home.css** | ![screenshot](#) | Passed. No warnings or errors |
| **products.css** | ![screenshot](#) | Passed. No warnings or errors |
| **product_detail.css** | ![screenshot](#) | Passed. No warnings or errors |
| **profile.css** | ![screenshot](#) | Passed. No warnings or errors |

#### JSHint Javascript Validator

File | Screenshot | Notes |
| --- | --- | --- |
| **stripe_elements.js** | ![screenshot](#) | Passed. No warnings or errors |
| **accordion.js** | ![screenshot](#) | Passed. No warnings or errors |
| **countryfield.js** | ![screenshot](#) | Passed. No warnings or errors |

- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

| Page | Screenshot |
| --- | --- | 

- - -

### Responsiveness

- - -

### Browser Compatibility

I have tested my deployed project on two different browsers to check for compatibility issues. I could not find any issues.

| Browser | Main page |
| --- | --- |
| Chrome | ![screenshot](documentation/testing/browsercomp/browser-chrome.png) | 
| Edge | ![screenshot](documentation/testing/browsercomp/browser-edge.png) | 

- - -

## MANUAL TESTING

### Testing User Stories
Here's a table for testing the various user stories of the project. The aim is to follow up the functionality implementation.

| Title | User Story | Response | 
| --- | --- | --- |

- - -

### Defensive Programming


- - -

### Bugs