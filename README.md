# Seed & Sprout

Link to live website: [CLICK HERE!](https://seedandsprout-ab1eae7ba537.herokuapp.com/)

![Am I Responsive Image](documentation/sesp-mockup.png)

Welcome to **Seed & Sprout** a fictional e-commerce website. It is a B2C platform, where the user can purchase seeds and gardening supplies.
This project was built by mainly using Django and it incorporates Stripe payments. The site enables user roles, authentication, and full CRUD for products and faqs, allowing interaction with a central dataset securely.
- - -
## Testing the payment process
Please note that this project does not process real payments or fulfill shipments. You are welcome to test the payment functionality by using the provided card details when prompted:
- Card number for payment testing: 4242 4242 4242 4242
- Enter any future date for card expiry.
- Enter any 3-digit number for CVC.
- - -
## UX
The theme of the project is seeds and gardening supplies, so I wanted to use a color palette that gives an eco-friendly and sustainable vibe.

### Colour Scheme
I used [coolors.co](https://coolors.co/2d2a1b-99a885-eec782-e9995c-f6f5ef) to generate my colour palette.
![screenshot](documentation/readme/sesp-colorpalette.png)

I've also used CSS `:root` variables to easily update the global colour scheme.

```css
:root {
    --primary-black: #2D2A1B;
    --primary-offwhite: #F6F5EF;
    --primary-orange: #E9995C;
    --primary-yellow: #EEC782;
    --primary-green: #99A885;
    --color-white: #FFFEFA;
    --color-grey: #b4b4b1;
    
    --box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    --btn-box-shadow: box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;

    --toast-success: #A8B99C;
    --toast-info: #95b0b4;
    --toast-warning: #E6B87D;
    --toast-error: #da664c;
}
```
### Typography
I used [Reddit Mono](https://fonts.google.com/specimen/Reddit+Mono) for all text in various font-sizes and weights. 
Reasons why I chose Reddit Mono:
- *Readability*: 
Reddit Mono is a monospaced font, which means that each character occupies the same amount of horizontal space. This uniformity enhances readability, especially for product descriptions and specifications, making it easier for customers to scan through information quickly.
- *Modern Aesthetic*:
Reddit Mono has a clean and modern appearance, which contributes to a professional image for this e-commerce site. A contemporary font can attract users and create a positive first impression, essential for online retail.
- *Versatility*:
Monospaced fonts, as Reddit Mono, are versatile and can be effectively used for various text elements, including headings and body text. This flexibility allows for a cohesive design throughout the website.

- - -
## Wireframes
Here are some wireframes that I created using [Balsamiq](https://balsamiq.com/). Note that some details shown in the wireframes may not match the final result. These wireframes act as a primary guide though, and the main structure and elements are depticted as shown here.

> **Homepage**
<details>
<summary>Homepage Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_homepage_desktop.png)
</details>

> **Products page**
<details>
<summary>Products Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_products_desktop.png)
</details>

> **Products detail page**
<details>
<summary>Products Detail Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_products_detail_desktop.png)
</details>

> **Add to cart page**
<details>
<summary>Add to cart Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_add_to_cart_desktop.png)
</details>

> **Shopping bag page**
<details>
<summary>Shopping bag Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_shopping_bag_desktop.png)
</details>

> **Checkout page**
<details>
<summary>Checkout Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_checkout_desktop.png)
</details>

> **FAQ page**
<details>
<summary>FAQ Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_faq_desktop.png)
</details>

> **About page**
<details>
<summary>About Desktop</summary>
    
![post detail page](documentation/readme/wireframes/sesp_wf_about_desktop.png)
</details>

- - -

## Agile Development Process

### GitHub Projects
[GitHub Projects](https://github.com/users/KikiBerg/projects/8) was used as an Agile tool for this project.
There are probaply more ideal tools out there, but for now it served its purpose.
I used this tool for planning my user stories & issues, then followed up now and then using the Kanban board. 
![screenshot](documentation/readme/sesp-userstories-project.png)

### GitHub Issues
[GitHub Issues](https://github.com/KikiBerg/pp5-ecommerce/issues/) was also used as an Agile tool.
I created my own **User Story Template** in order to manage the user stories.

- [Open Issues](https://github.com/KikiBerg/pp5-ecommerce/issues?q=is%3Aopen):
I placed these to a **Backlog** column as they are features that were not prioritized and are seen as possible future implementations.

- [Closed Issues](https://github.com/KikiBerg/pp5-ecommerce/issues?q=is%3Aissue+is%3Aclosed) 

### MoSCoW Prioritization

I've prioritized my user stories using this method and used labels for my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered 
- **Should Have**: adds significant value, but not vital 
- **Could Have**: has small impact if left out 
- **Won't Have**: not a priority for this iteration

### User Stories

I created the user stories in the beginning of the project so that I could better organize the structure of the site. 
Some of the stories were adjusted during the working process, so as to better fit my final ideas.
| Title | User Story | Subcategory | MoSCoW Priority | 
| --- | --- | --- | --- |
| View a list of products | As a **shopper**  I want to be able to **view a list of products** so that I can **select some to purchase** | Viewing & Navigation | Must Have |
| View individual product details | As a **shopper**  I want to be able to **view individual product details** so that I can **identify the price, description, product rating & product image** | Viewing & Navigation | Must Have |
| View total of my purchase | As a **shopper**  I want to be able to **easily view the total of my purchases at any time** so that I can **avoid spending too much** | Viewing & Navigation | Must Have |
| View specific category of products | As a **shopper**  I want to be able to **view a specific category of products** so that I can **quickly find products I'm interested in without having to search through all products** | Viewing & Navigation | Must Have |
| Register for an account | As a **site user**  I want to be able to **easily register for an account** so that I can **have a personal account & be able to view my profile** | Registration & User Accounts | Should Have |
| Login & logout | As a **site user**  I want to be able to **easily login & logout** so that I can **access my personal account information** | Registration & User Accounts | Should Have |
| Recover password | As a **site user**  I want to be able to **easily recover my password in case I forget it** so that I can **recover access to my account** | Registration & User Accounts | Should Have |
| Email confirmation | As a **site user**  I want to be able to **receive an email confirmation after registering** so that I can **verify that my account registration was successful** | Registration & User Accounts | Should Have |
| User profile | As a **site user**  I want to be able to **have a personalized user profile** so that I can **view my personal order history, order confirmations & save my payment information** | Registration & User Accounts | Should Have |
| Sort available products | As a **shopper**  I want to be able to **sort the list of available products** so that I can **easily identify the best rated, best priced & categorically sorted products** | Sorting & Searching | Should Have |
| Sort specific category | As a **shopper**  I want to be able to **sort a specific category** so that I can **find the best-priced or best-rated product in a specific category or sort the products in that category by name** | Sorting & Searching | Should Have |
| Sort multiple categories | As a **shopper**  I want to be able to **sort multiple product categories simultaneously** so that I can **find the best-priced or best-rated products across broad categories, such as "Vegetable seeds" or "Organic seeds"** | Sorting & Searching | Should Have |
| Search by name or description | As a **shopper**  I want to be able to **search for a product by name or description** so that I can **find a specific product I'd like to purchase** | Sorting & Searching | Should Have |
| Search overview | As a **shopper**  I want to be able to **easily overview what I've searched for & the number of the results** so that I can **quickly decide whether the product I want is available** | Sorting & Searching | Should Have |
| Select quantity | As a **shopper**  I want to be able to **select the quantity of a product when purchasing it** so that I can **ensure I don't accidentally select the wrong product or quantity** | Purchasing & Checkout | Should Have |
| View bag items | As a **shopper**  I want to be able to **view my bag items** so that I can **identify the total cost of my purchase and all items I will receive** | Purchasing & Checkout | Should Have |
| Adjust quantity of specific items | As a **shopper**  I want to be able to **adjust the quantity of specific items in my bag** so that I can **easily make changes to my purchase before checkout** | Purchasing & Checkout | Should Have |
| Enter payment information | As a **shopper**  I want to be able to **easily enter my payment information** so that I can **checkout effectively** | Purchasing & Checkout | Should Have |
| Secure information | As a **shopper** I want to be able to **feel my personal & payment info is safe & secure** so that I can **confidently provide the information needed for the purchase** | Purchasing & Checkout | Should Have |
| Order confirmation | As a **shopper** I want to be able to **view an order confirmation after checkout** so that I can **verify that I haven't made mistakes** | Purchasing & Checkout | Should Have |
| Add a product | As a **store owner** I want to be able to **add a product** so that I can **add new items to my store** | Admin & Store Management | Must Have |
| Update a product | As a **store owner** I want to be able to **update a product** so that I can **change product prices, descriptions, images & other criteria** | Admin & Store Management | Must Have |
| Delete a product | As a **store owner** I want to be able to **delete a product** so that I can **remove items that are no longer for sale** | Admin & Store Management | Must Have |
| Delete a product | As a **store owner** I want to be able to **delete a product** so that I can **remove items that are no longer for sale** | Admin & Store Management | Must Have |
| Subscribe to newsletter | As a **site user** I want to be able to **subscribe to a newsletter by providing my email address** so that I can **get updates about new products** | Registration & User Accounts | Must Have |
| Manage subscriber list | As a **site admin** I want to be able to **view and manage the list of newsletter subscribers** so that I can **send newsletters periodically** | Registration & User Accounts | Must Have |
| View FAQs list | As a **site user** I want to be able to **view a list of FAQs grouped by categories** so that I can **more easily find answers to my questions** | Viewing & Navigation | Must Have |
| Add FAQs list | As a **site admin** I want to be able to **add new FAQs** so that I can **follow up questions from customers** | Viewing & Navigation | Must Have |
| Update FAQs list | As a **site admin** I want to be able to **edit existing FAQs** so that I can **keep the section up to date** | Viewing & Navigation | Must Have |
| Delete FAQs list | As a **site admin** I want to be able to **delete FAQs** so that I can **remove questions that are no longer for relevant** | Viewing & Navigation | Must Have |

- - -

## Features

### Existing Features

### Future Features
- - -

## Tools & Technologies
- ### Languages:
    
    + [Python](https://www.python.org/downloads/release/python-385/): used as the back-end programming language.
    + [JS](https://www.javascript.com/): used for user interaction on the site.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): used for the main site content.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): used for the main site design and layout.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [jQuery](https://jquery.com/): was used to control click events and sending AJAX requests.
    + [Bootstrap](https://getbootstrap.com): as the front-end CSS framework for modern responsiveness and pre-built components.

- ### Databases:

    + [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) was used as the relational database management.

- ### Version control, IDE & Deployment:
    + [Git](https://git-scm.com): for version control.
    + [Gitpod](https://gitpod.io): cloud-based IDE for development.
    + [Github](https://en.wikipedia.org/wiki/GitHub): was used to store the code.
    + [Heroku](https://www.heroku.com): for hosting the deployed back-end site.

- ### Other tools:    
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Psycopg2](https://www.psycopg.org/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Gunicorn](https://pypi.org/project/gunicorn/) - A Python Web Server Gateway Interface (WSGI) HTTP server.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
    - [Mermaid Live Editor](https://github.com/mermaid-js/mermaid-live-editor): was used for generating my final ERD.
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/): was used to validate Python code for the website.
    + [Stripe](https://stripe.com/): was used to create the payment system.
    + [AWS S3 and IAM](https://aws.amazon.com/): was used to host static and media files for this project and IAM for the permissions based roles for accessing the S3 buckets.
    + [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php): was used to quickly check responsiveness and generate mockup images.
    + [Diffchecker](https://www.diffchecker.com/): was used to quickly cross-check my template versions as I was developing them.
    + [Sitemap Generator](https://www.xml-sitemaps.com/) was used to create the sitemap.xml file.
    + [Balsamiq](https://balsamiq.com/) - Used to create wireframes and website structure map for the project.
    + [LightHouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used for testing performance.

- - -

## Database Design
Entity Relationship Diagrams (ERD) aid in conceptualizing the skeleton of a database prior to creating the models. 
- Identifying the connections among various tables at the initial stages contributes to time efficiency. 
- These diagrams offer a structured representation of the system's data tables, their respective fields, and the interactions among the tables.

Here's the diagram for the Seed & Sprout project:
```mermaid
erDiagram
    About {
        int id
        string title
        text content
    }

    Contact {
        int id
        string name
        string email
        text message
        datetime created_at
    }

    Order {
        int id
        string order_number
        int user_profile_id
        string full_name
        string email
        string phone_number
        string country
        string postcode
        string town_or_city
        string street_address1
        string street_address2
        string county
        datetime date
        decimal delivery_cost
        decimal order_total
        decimal grand_total
        text original_bag
        string stripe_pid
    }

    OrderLineItem {
        int id
        int order_id
        int product_id
        int quantity
        decimal lineitem_total
    }

    FAQ {
        int id
        string question
        text answer
        int category_id
        datetime created_at
        datetime updated_at
    }

    Newsletter {
        int id
        string email
        datetime subscribed_at
        bool is_active
    }

    Category {
        int id
        string name
        string friendly_name
    }

    Product {
        int id
        int category_id
        string sku
        string name
        text description
        decimal price
        decimal rating
        string image_url
        image image
        string botanical_name
        bool is_organic
        int days_to_maturity
        string lifespan
        string sowing_season
        string sowing_depth
        string germination_time
        string sunlight_requirement
        string water_requirement
        string plant_spacing
        string row_spacing
        string height
        string harvest_blooming
        int seed_count
        text instructions
        bool is_gardening_supply
        string dimensions
    }

    UserProfile {
        int id
        int user_id
        string default_phone_number
        string default_country
        string default_postcode
        string default_town_or_city
        string default_street_address1
        string default_street_address2
        string default_county
    }

    Order ||--o{ OrderLineItem: "has many"
    UserProfile ||--o{ Order: "places"
    Product ||--o{ OrderLineItem: "contains"
    FAQ }o--|| Category: "belongs to"
    Product }o--|| Category: "belongs to"
    User ||--o{ UserProfile: "has one"
```

**`about app`**
#### About model:

|Database Key|Field Type|Validation|
|---|---|---|
|title|CharField|max_length=200|
|content|TextField||

#### Contact model:

|Database Key|Field Type|Validation|
|---|---|---|
|name|CharField|max_length=100|
|email|EmailField||
|message|TextField||
|created_at|DateTimeField|auto_now_add=True|

**`bag app`**
- This app has no classes or models, as it primarily focuses on bag calculations

**`checkout app`**
#### Order model:

|Database Key|Field Type|Validation|
|---|---|---|
|order_number|CharField|max_length=32, null=False, editable=False|
|user_profile|ForeignKey|'UserProfile', null=True, blank=True, on_delete=models.SET_NULL, related_name='orders'|
|full_name|CharField|max_length=50, null=False, blank=False|
|email|EmailField|max_length=254, null=False, blank=False|
|phone_number|CharField|max_length=20, null=False, blank=False|
|country|CountryField|blank_label='Country *', null=False, blank=False|
|postcode|CharField|max_length=20, null=True, blank=True|
|town_or_city|CharField|max_length=40, null=False, blank=False|
|street_address1|CharField|max_length=80, null=False, blank=False|
|street_address2|CharField|max_length=80, null=True, blank=True|
|county|CharField|max_length=80, null=True, blank=True|
|date|DateTimeField|auto_now_add=True|
|delivery_cost|DecimalField|max_digits=6, decimal_places=2, null=False, default=0|
|order_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|grand_total|DecimalField|max_digits=10, decimal_places=2, null=False, default=0|
|original_bag|TextField|null=False, blank=False, default=''|
|stripe_pid|CharField|max_length=254, null=False, blank=False, default=''|

#### OrderLineItem model:
|Database Key|Field Type|Validation|
|---|---|---|
|order|ForeignKey|'Order', null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'|
|product|ForeignKey|'Product', null=False, blank=False, on_delete=models.CASCADE|
|quantity|IntegerField|null=False, blank=False, default=0|
|lineitem_total|DecimalField|max_digits=6, decimal_places=2, null=False, blank=False, editable=False|

**`faqs app`**
#### FAQ model:

|Database Key|Field Type|Validation|
|---|---|---|
|question|CharField|max_length=255|
|answer|TextField||
|category|ForeignKey|'Category', on_delete=models.CASCADE, related_name='faqs'|
|created_at|DateTimeField|auto_now_add=True|
|updated_at|DateTimeField|auto_now=True|

**`home app`**

- This app has no classes or models, as it primarily focuses on the index page display and function

**`newsletter app`**
#### Newsletter model:

|Database Key|Field Type|Validation|
|---|---|---|
|email|EmailField|unique=True|
|subscribed_at|DateTimeField|auto_now_add=True|
|is_active|BooleanField|default=True|

**`products app`**
#### Category model:

|Database Key|Field Type|Validation|
|---|---|---|
|name|CharField|max_length=254, null=True, blank=True|
|friendly_name|CharField|max_length=254, null=True, blank=True|

#### Product model:

|Database Key|Field Type|Validation|
|---|---|---|
|category|ForeignKey|'Category', null=True, blank=True, on_delete=models.SET_NULL|
|sku|CharField|max_length=254, null=True, blank=True|
|name|CharField|max_length=254|
|description|TextField||
|price|DecimalField|max_digits=6, decimal_places=2|
|rating|DecimalField|max_digits=6, decimal_places=2, null=True, blank=True|
|image_url|URLField|max_length=1024, null=True, blank=True|
|image|ImageField|null=True, blank=True|
|botanical_name|CharField|max_length=254, null=True, blank=True|
|is_organic|BooleanField|default=False|
|days_to_maturity|IntegerField|null=True, blank=True|
|lifespan|CharField|max_length=50, null=True, blank=True|
|sowing_season|CharField|max_length=100, null=True, blank=True|
|sowing_depth|CharField|max_length=50, null=True, blank=True|
|germination_time|CharField|max_length=100, null=True, blank=True|
|sunlight_requirement|CharField|max_length=100, null=True, blank=True|
|water_requirement|CharField|max_length=100, null=True, blank=True|
|plant_spacing|CharField|max_length=50, null=True, blank=True|
|row_spacing|CharField|max_length=50, null=True, blank=True|
|height|CharField|max_length=50, null=True, blank=True|
|harvest_blooming|CharField|max_length=100, null=True, blank=True|
|seed_count|IntegerField|null=True, blank=True|
|instructions|TextField|null=True, blank=True|
|is_gardening_supply|BooleanField|default=False|
|dimensions|CharField|max_length=100, null=True, blank=True|

**`profiles app`**
#### UserProfile model:

|Database Key|Field Type|Validation|
|---|---|---|
|user| OneToOneField|'User', on_delete=models.CASCADE|
|default_phone_number|CharField| max_length=20, null=True, blank=True |
|default_street_address1|CharField|max_length=80, null=True, blank=True |
|default_street_address2|CharField|max_length=80, null=True, blank=True |
|default_town_or_city|CharField|max_length=40, null=True, blank=True |
|default_county| CharField|max_length=80, null=True, blank=True |
|default_postcode| CharField|max_length=20, null=True, blank=True |
|default_country| CountryField|blank_label='Country', null=True, blank=True |