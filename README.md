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
## Web Marketing

### Ecommerce Business Model

#### Products models

#### Contact Form Model

#### About Us Model

#### FAQ Model

#### Resources Model


### Marketing strategies

#### Social Media & Newsletter Marketing

### Search Engine Optimization (SEO)

#### Keywords

#### Keywords Implementation

#### Sitemap

#### Robots.txt

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
    + [Fontawesome](https://fontawesome.com/) for icons
    + [Google Fonts](https://fonts.google.com/) for the website fonts
    + [Coolors](https://coolors.co) to generate my colour palette

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

- - -

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

- - -

## Deployment
The live deployed application can be found deployed on [Heroku](https://seedandsprout-ab1eae7ba537.herokuapp.com/)

### PostgreSQL (Code Institute)
This project uses [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) for the PostgreSQL Database.
These are database systems provided by Code Institute for storing and managing application data during the development and deployment process.

To connect to the database:
- Go to the [Code Institute Database Maker](https://dbs.ci-dbs.net/)
- Create a database using the email address used to sign up for the Code Institute LMS.
- The Database URL is sent to the email address.
- Add the database URL as a variable to the project and make sure to keep it secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code.

### Set up hosting of static and media files with AWS

1.  Sign in or create an account with [Amazon Web Server](https://aws.amazon.com/)

2.  Navigate to the AWS Console home

3.  Search for "s3" in the search bar

4.  Click on "Create bucket"

5.  In the Create bucket page add the following information:

- A name for the bucket. It is recomeneded to use the same name you gave your Heroku app.

- A region closest to you.

- Select ACLs enabled

- Uncheck the "Block all public access" checkbox

- Check the box beside "I acknowledge that the current settings might result in this bucket and the objects within becoming public."

Scroll to the bottom of the page and select "Create bucket"

6.  Click on the new bucket you just created.

7.  In the "Properties" tab scroll to the bottom of the page and in Static website hosting
click "Edit".

8.  Select "Enable" and paste the following in the the "Redirection rules – optional" at
the bottom of the page:

```
[
    {
        "AllowedHeaders": [
            "Authorization"
    ],
    "AllowedMethods": [
        "GET"
    ],
    "AllowedOrigins": [
        "*"
    ],
        "ExposeHeaders": []
    }
]
```

9.  In the "Permissions" tab click on the "Edit" button underneath Bucket policy

10.  Copy the "Bucket ARN" and click on "Policy generator"

11.  On the next page:

- Select "S3 Bucket Policy"

- Add * (an asterisk) as the "Principal" value

- Select "GetObject" in the "Actions" dropdown

- Paste the "Bucket ARN" (from step 10 above) as the Amazon Resource Name (ARN)

- Click "Add Statement" then "Generate Policy"

- Copy the policy shown in the pop-up box

12.  Back in the AWS "Edit bucket policy" paste the policy just copied.

13.  At the end of the resource key but before the closing quotation mark add: 
```
/*
```

and click "Save"

14. On the next page click "Edit" in the "Access control list (ACL)" section.

- Enable "List" for "Everyone (public access)"

- Accept the warning

#### In AWS services menu:
1. Select "IAM" from the AWS menu and then "User groups" from the menu on the left 
hand side.

2.  Click the "Create group" button

3.  Give the group a name and click "Next step", then on the next page "Next step" agin.

4.  Click the "Create group" button

5.  Select "Polices" from the menu, then "Create policy" button.

6.  In the JSON tab select "Import managed policy" link

7.  Add "s3" into the search bar, select "AmazonS3FullAccess" and click "Import"

8.  Paste in the Bucket ARN and the Bucket ARN followed by /* as the Resource values

9.  Click "Review policy" and add a name and description and click "Create policy"

10.  Select "Groups" from the menu and select the group you made in Step 3.

11.  Click "Attach policy", search and select the policy just created.

12.  Click "Attach policy"

#### Add a user 

1.  Select "Users" in the menu, then click "Add user"

2.  Add a user name and check the "Programatic access" checkbox for Access type

3.  Select "Next: Permissions"

4.  On the following page check the name of your added user group

5.  Click through the next pages until you can click the "Create user" button

6.  Navigate on user page to 'security credentials'

7. Click on 'Create access key'

8. After they are created click on 'download.csv' file

### Wire up Django

1. Install boto3 and django-storages:

```
pip3 install boto3
pip3 install django-storages
```

2.  Add above to requirements.tct:
```
pip3 freeze > requirements.txt
```

3.  Add "storages", to INSTALLED_APPS in seetings.py

4.  Paste the following in settings.py:
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # bucket config
    AWS_STORAGE_BUCKET_NAME = 'seedandsprout'
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

5.  Paste the following in settings.py:
```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}'
```

### Google Mail (Gmail) API

This project uses [Gmail](https://mail.google.com/) to handle email communication with users for account verification and order confirmations.

To connect to Gmail API:
- Create a Gmail (Google) account obtain the API key and connect your project.
- Log into or sign up for a Google Gmail account.
- Navigate to "Account Settings" (cog icon) in the top-right corner of Gmail.
- Select "Accounts and Import".
- Within the section called "Change account settings", click on the link for Other Google Account settings.
- From this new page, select "Security" on the left.
- Select 2-Step Verification to activate and follow the instructions to verify your password and account.
- Once verified, select "Turn On" 2-factor authentication (2FA).
- Navigate back to the "Security" page and select "App passwords".
- This might prompt you once again to confirm your password and account.
- Select "Mail" as "App Type".
- Select "Other (Custom name) " for the "device type".
- Add custom name,  e.g. project’s name.
- You'll be provided with a 16-character password (API key).
  - Tip: store this key safely, as you cannot access this key again!
  - EMAIL_HOST_PASS = user's 16-character API key.
  - EMAIL_HOST_USER = user's own personal Gmail email address.
- Add the pass and the host as variables to the project and make sure to keep them secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code. 

### Stripe

This project uses [Stripe](https://docs.stripe.com/) to handle the secure payment process in test mode.

To connect to Stripe API:
- Log into or sign up for a stripe account.
- Navigate to "Developers" on the top page menu.
- In the section "API keys", select "Get your test API keys".
- You will find two keys necessary to connect your project: 
  - STRIPE_PUBLIC_KEY = Publishable Key (starts with pk)
  - STRIPE_SECRET_KEY = Secret Key (starts with sk)
- In case users prematurely close the purchase-order page or internet connection fails during payment processing, it is important include Stripe Webhooks.
- Navigate to "Developers" on the top page menu.
- In the section "Webhooks", select "Add Endpoint".
  - Add the webhook URL.
  - Select "Receive All Events".
  - Click the button "Add Endpoint" to complete the process.
  - You will find one key under signing secret.
    - STRIPE_WH_SECRET = Signing Secret (Wehbook) Key (starts with wh)
- Install the stripe package and integrate to the Django project by configuring it in the settings.py file.
- Add the link to [stripe's JavaScript](https://docs.stripe.com/js) in your base html template to make security features from stripe available throughout the website for maximum security.
- Add core JavaScript from the stripe documentation necessary to [accept a payment](https://docs.stripe.com/payments/accept-a-payment).
- Stripe elements style is customizable to adhere to the ovarall [style of the website](https://docs.stripe.com/elements/appearance-api).
- Add the keys as variables to the project and make sure to keep the secret keys secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code.

### Heroku

Sign in or create an account with [Heroku](https://www.heroku.com/)

- In the Heroku dashboard use the New tab to create a new app.

- Name the app and choose a region.

- Click on the settings tab and select "Reveal Congig Vars".

  - Add DATABASE_URL with the value of the database URL copied from ElephantSQL

- Enter the following command in to your terminal to install dj_database and psycopg2. These are needed to connect to the database.

```pip3 install dj_database_url==0.5.0 psycopg2```

Followed by ```pip freeze > requirements.txt``` to update requirements.txt.

Add ``` import dj_database_url``` below import os in settings.py

In the DATABASES section of the settings comment out the initial settings and place the following underneath:

```
DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```

Migrate the models to the database using
```
 python3 manage.py migrate
```

Create a superuser and supply a username and password:
```
 python3 manage.py createsuperuser
```

Within the Django admin confirm the email address

Change the DATABSE settings to the following:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
```

Install [Gunicorn](https://gunicorn.org/) webserver:

```
pip3 install gunicorn
```

Create a file named Procfile in the root of the project and add:
```
web: gunicorn 'name-of-your-project'.wsgi:application
```

Add the required dependencies to requirements.tc with:
```
pip3 feeze > requirements
```

Add the following to settings:
```
ALLOWED_HOSTS = ["'name-of-the-website'.herokuapp.com", "localhost"]
```

Add changes, commit and push to GitHub and Heroku
```
git add . 
git commit -m "Deployment"
git push
git push heroku main
```
#### Configure your variables in Heroku
- Click on "Add a new Config Var" and add the necessary keys and values.    
    - AWS_ACCESS_KEY_ID = with the value of the access key.
    - AWS_SECRET_ACCESS_KEY with the value of the secret key.
    - DATABASE_URL with the value of the database URL.
    - EMAIL_HOST_PASS with the value of the API key.
    - EMAIL_HOST_USER with the value of the email address.
    - SECRET_KEY with the value of the secret key.
    - STRIPE_PUBLIC_KEY with the value of the public key.
    - STRIPE_SECRET_KEY with the value of the secret key.    
    - STRIPE_WH_SECRET with the value of the webhook handler secret key.
    - USE_AWS: this should be set to True

> [!IMPORTANT]
> Note that all these keys shoul also exist in your env.py file, which in its turn should exist inside the .gitignore file.

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

> [!IMPORTANT]
> Crucial when working with DEBUG=True during development.
    
### Local Deployment
This project can be cloned or forked in order to make a local copy on your own system.
For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.


#### Steps to clone project
- Click on the code tab under the repository name.
- Then click on "Code" button to the right above the files listed.
- Click on the clipboard icon to copy the URL.
- Open Git Bash in gitpod or your preferred IDE.
- Change the working directory to where you want your cloned directory.
- Type git clone and then paste the URL that you copied.
- Press enter and clone is complete.
- In the terminal install the requirements by using the following: `pip3 install -r requirements.txt`
- Next create the env.py file which tells our project which variables to use.
- Add the file to a .gitignore to prevent it from being pushed to github
- Make migrations by running : python manage.py makemigrations
- Then migrate those changes with python manage.py migrate
- To run the project type `python manage.py runserver` into the terminal and open port 8000.
- This will open the project locally for you to work on.

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking repository on GitHub
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:
1. Log in to GitHub and locate the [GitHub Repository](https://github.com/KikiBerg/urban-biodiversity-platform)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Code used
- I looked back to "Boutique Ado" walkthrough material from Code Institute to get help constructing my initial project.
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Django Docs](https://www.djangoproject.com/)
- Stripe Official documentation for code snippets necessary for implementing the Stripe payment process:
  - [Core JavaScript functunalities from stripe](https://stripe.com/docs/payments/accept-a-payment).
  - [Core CSS style from stripe](https://stripe.com/docs/stripe-js)

### Content
- Details about the seeds are taken from: [Runåbergs Fröer](https://en.runabergsfroer.se/)
- Rest of the content, e.g the About and FAQ page, was written by myself.

### Media
I used these sites for the photographic media:
- [Pexels](https://www.pexels.com/)
- [Amazon](https://www.amazon.se/)
- [Ubuy](https://www.ubuy.dk/)

### Acknowledgements
- My mentors, Sheryl Goldberg & Tim Nelson, for their guidance.
- The Code Institute Tutor support, for all the help.
- Thanks to Kristyna Wach, my Cohort facilitator for making sure I had all the material & information needed as well as for her encouragement.
- The Slack community, for the good advice.
- My fellow co-student [Gudrun](https://github.com/g-omarsdottir) for her support and willingness to help!