# Seed & Sprout

Link to live website: [CLICK HERE!](https://seedandsprout-ab1eae7ba537.herokuapp.com/)

![Am I Responsive Image](documentation/sesp-mockup.png)

Welcome to **Seed & Sprout** a fictional e-commerce website. It is a B2C platform, where the user can purchase seeds and gardening supplies.
This project was built by mainly using Django and it incorporates Stripe payments. The site enables user roles, authentication, and Full CRUD for products, allowing interaction with a central dataset securely.

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
Here are some wireframes that I created using [Balsamiq](https://balsamiq.com/). As the project was developing I tried to follow the agile method of adjusting the elements, so for that reason some details shown in the wireframes may not match the final result.

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
