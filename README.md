# <div align="center">VINYL</div>

Vinyl is a fictional online record store selling new and exclusive records with in a variety of different Genres. Users can select the record they want to purchase, click to view more details, pick the quantity and format size (7', 10' or 12') and add to basket to be purchased through PayPal on checkout.
___

## User Experience (UX)
The User should be able to browse records based on the category of their choice, they should be able to view individual products and add as many products as they want to the cart.


##### User Research:
The targeted users for this project were people with a passion for music, probably "hipsters" aged between 25-35 who own a record player. I tried to keep the design modern and basic in keeping with the design of most sites targeting this particular audience. 



* ### Design
    * ###### Imagery
        The images of the spinning vinyls on the products list page were all modified on [place.it](https://placeit.net/) using the basic vinyl mockup. The images the record sleeve and record were made using [Figma](https://www.figma.com/file/JExtXK6x28W1jp5nz1teED/VINYL?node-id=0%3A1).
    * ###### Typography
        The font used throughout is [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed?query=roboto&preview.text=V%20I%20N%20Y%20L&preview.text_type=custom)
    * ###### Colour Scheme
        The main background colour is Aero Green:
       ![#F4FFF7](https://via.placeholder.com/300x50/F4FFF7/F4FFF7?text=+) `#F4FFF7`<br>

        The main font colour is Cod Gray:
        ![#141414](https://via.placeholder.com/300x50/141414/141414?text=+) `#141414`<br>

        The product display page is Sirocco Green with Aero Green lines:
        ![#676C69](https://via.placeholder.com/300x50/676C69/676C69?text=+) `#676C69`

* ### Wireframes
    Most of my design process was done in the browser, although i did design the products list and product display page in Figma.<br>

    You can view the Figma file for this project [here](https://www.figma.com/file/JExtXK6x28W1jp5nz1teED/VINYL?node-id=0%3A1).
    ___

### Features
* ##### [Main Page Features](https://db-vinylproject.herokuapp.com/)
   The main page has a small icon navbar that displays links to the Vinyl Store, Contact page, Sign in page and the Cart. When hovered, a materialize tool tip should display the link name.
   <img src="static\images\README_images\homepage.GIF" style="height: 200px;">

* ##### [Product List Page](https://db-vinylproject.herokuapp.com/cart/shop/)
    The product list page displays all of the available inventory, you can filter through the available records by clicking on the genre of your choice. CSS ```@keyframes``` were used to make the records rotate.

   <img src="static\images\README_images\categories.gif" style="height: 200px;">

* ##### [Product Detail Page](https://db-vinylproject.herokuapp.com/cart/shop/nature-always-wins/)

   Clicking on a record will display the individual product, along with the quantity amount and a choice of format. A new image of a record and sleeve will be displayed in the display view, here, you can add the item to the cart after choosing the quantity amount and format.
   <img src="static\images\README_images\display.gif"><br>

* ##### [Cart Page](https://db-vinylproject.herokuapp.com/cart/)

   Once the chosen product is added to the cart you will be taken to the Cart page which displays your products on the left, and on the right you can view the complete total of all products. You can add and delete products by using the "Remove" button at the top of the product, or decrementing to 0 to remove. From here you can either continue browsing or checkout.
   <img src="static\images\README_images\cart.gif"><br>

* ##### [Checkout](https://db-vinylproject.herokuapp.com/cart/checkout/) (Not signed in)

   If the User is not authenticated they will be taken to a page requesting they either sign in or register in order to checkout. To make it a bit more interesting I've added some small smiley face icons that rotate.
   <img src="static\images\README_images\checkoutnotsignedin.gif"><br>

* ##### [Checkout](https://db-vinylproject.herokuapp.com/cart/checkout/) (Signed in)

   If the User IS authenticated they will be taken to a form to complete detailing where to send the product(s). This information will be saved to the Users profile for a faster checkout on their next purchase. The "View Checkout Products" button on the right of the screen will reveal a footer modal showing the products the User has selected.
   <img src="static\images\README_images\checkoutsignedin.gif"><br>

* ##### [Payment](https://db-vinylproject.herokuapp.com/cart/payment/#!)

   Once the User has entered or selected their shipping address, they can click "Proceed To Payment" to access the payment page and also save the address they just entered. Here, the User can choose between PayPal or debit card payments.<br><br>
   <span style="opacity: 0.7;">Sandbox Email: `sb-lukix3568329@business.example.com`<br>
   Sandbox Password: `3eB%8e@-`</span><br>
   <img src="static\images\README_images\topaypal.gif"><br>

   Once the payment has been successfully processed the User will be directed to a "Thank You" page, where they can choose to go back to the home page or re-visit the store.
   <img src="static\images\README_images\thanks.gif"><br>

* ##### [Staff App](https://db-vinylproject.herokuapp.com/staff/)

   If the User is registered with a Staff account, they will see a new red exclamation icon appear on the homepage that will take them to the staff side portal for the store. In here the Staff User can view all availableinventory and also add/delete and update products.
   <img src="static\images\README_images\tostaff.gif"><br>


   Superuser Email: `superuser@super.com`<br>
   Superuser Password: `superuser55`<br>
   
   From the staff side app you can add/delete or update products and also view the complete order history of all users.<br>
   <img src="static\images\README_images\inventory.gif"><br>

* ##### [Update A Product](https://db-vinylproject.herokuapp.com/staff/products/)
  Updating a product is easy, just click on the update button for the product you wish to modify, this will bring you to a form page where you cn edit all details of the selected product.<br><br>
  The ```slug``` is used to generate a cleaner looking URL, in this instance i've chosen to manually input all slugs, although Django do provide the ```prepopulated_fields``` function to prepoulate the ```slug``` depending on the Users input. eg. ```prepopulated_fields = {"slug": ("album_title",)}``` this means the slug field will populate based on the Album's name. The slug must ALWAYS be unique. 
   
   <img src="static\images\README_images\updateproducts.gif"><br>

* ##### [Delete A Product](https://db-vinylproject.herokuapp.com/staff/create/)
  Deleting a product has 3 safeguards to make sure you do not delete a product on accident. Click the red "Destroy" button, this will ask "Are you sure?" using Popper.js, you will then be directed to a "Complete Destruction" page where you can finally delete the product for good.
   
   <img src="static\images\README_images\deleteproduct.gif"><br>
___

### <div align="center">Libraries & Frameworks</div>


##### CSS Libraries:
I used both [Bootstrap4](https://getbootstrap.com/) and [MaterializeCSS](https://materializecss.com/) for the layout of the site and to help with media query responsiveness.

##### Javascript Libraries:
* Some [JQuery](https://jquery.com/) was used to handle DOM elements and initiate things such as MaterializeCSS modals and tooltips.
* I used [Popper.js](https://popper.js.org/) for the tooltip popup that shows when deleting a product from the inventory.
* [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) is used to animate each screens ```fade-in``` and the ```fade-up```effect on the products list page


##### Python
The [Django](https://www.djangoproject.com/) framework was used for the entire project. I had a lot of diffulties at first, but now i love it!
___

### <div align="center">Testing & Bugs</div>

I used both [W3C Validator](https://jigsaw.w3.org/css-validator/) and [W3C Mark Up Validation](https://validator.w3.org/) to ensure the validity of he HTML and CSS code.

**Client Side Testing:**

<em>"I would like to purchase Vinyl Records based on a chosen Genre..."</em>

The main page icons, when hovered, reveal exactly where that link will take you. Clicking on the icon of the small vinyl you will be taken to the products list page where you can choose between genres and pick the recordof your choosing.<br>
<img src="static\images\README_images\desktopicons.PNG">
  

<em>"I would like to see the Artists name, Album i'm purchasing, price and format of each product before clicking the product..."</em>

Each product on the product list page is presented with the Vinyl image, Artists name, Album name and purchase details on the product card<br>
<img src="static\images\README_images\productlist.PNG">

<em>"I would like to pick the quantity and format of the recordI'm purchasing..."</em>

Once you click the record of your choice, you will be taken to the products detail page where you can select the quantity and see the format and price of the product.<br>
<img src="static\images\README_images\quantityformat.PNG">

<em>"Beore I purchase, I would like the ability to add or delete products..."</em>

Once the product is added to the cart, you wil be able to increment or decrement the quantity using the arrows on either side of the quantity box.<br>
<img src="static\images\README_images\quantity.PNG">


<em>"I want purchasing an item to be quick and simple..."</em>

When checking out, you will only be asked for your delivery address. Your address will then be saved to your account for future reference

<em>"I want to be able to see a list of my past orders..."</em>

On the Users profile page, you're able to see a list of all of your purchases.<br>
<img src="static\images\README_images\orders.PNG">


**Testing Page Elements:**

**1. Home Page:**
- All icons on the home page go to their respective links and appear according to user authentication.
- When hovering over an icon the correct tooltip title appears.  

**2. Products List Page:**
- All products display the correct vinyl image with the correct art displayed on the record itself.
- [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) only fades in the first line of records not the full inventory.
- Clicking on a product takes you to the products display page.
- All images rotate after 2 seconds.

**3. Product Detail Page:**
- Page displays the correct second image for the product.
- The dropdown to select the Format only displays the formats assigned to the product.
- The correct quantity and format adds to cart.

**4. Cart Page:**
- Quantity goes below 0 in to the minus numbers.

   FIXED:<em> Product could be dropped below 0 and did not remove the item. This was fixed with the following Python code:</em><br>

      if order_item.quantity <= 1:
            order_item.delete()
      else:
            order_item.quantity -= 1
            order_item.save()</em>

- Clicking on "Checkout" when not signed in takes you to the sign up request page instead of taking the User to the payment page.

**5. Contact Page:**
- Contact for sends to the correct address.
  FIXED: <em>Had some issues with Googles security, creating a seperate app password and disabling capture help</em>
___

### <div align="center">Deployment</div>
The project was developed using [Visual Studio Code](https://code.visualstudio.com/) then pushed to [Github](https://github.com/DelroyBrown28/VinylProject_2) and [Heroku](https://dashboard.heroku.com/apps) using the git CLI. I had some issues with my [original git repository](https://github.com/DelroyBrown28/VinylProject) so i had to copy everything from there in to a new one. 

When deploying this project to Github, i took the following steps:
1. Create a new Github Repository.
2. Create a repository name.
3. Copy/paste the following Command Line commands to create a repository in the CLI.
```
echo "# testing123" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/DelroyBrown28/testing123.git
git push -u origin main
                
``` 
4. Push code to Github using ```git add -A``` then ```git commit -m "Commit message here"``` and finally ```git push```
5. Once the code is up on Github, go to settings, scroll down to "Github Pages" and change "source" to "main".<br>
<img src="static\images\README_images\githubpages.PNG" style="height: 200px;"><br><br>
6. Refresh after a minute or so and a green banner displaying the URL for the deployed site will be visible.<img src="static\images\README_images\greenbanner.PNG">

When deploying to Heroku, I took the following steps:
1. Create a new Heroku app.
2. Go to the "Deploy" tab and connect to Github.
3. Once connected to the correct Github repository, make sure all code is pushed to github using ```git add -A``` then ```git commit -m "Commit message here"``` then ```git push``` and finally ```git push heroku main```
4. Once pushed to heroku, click the link in the terminal and the deployed project appears.
<img src="static\images\README_images\deployed.PNG">

**Running Project Locally:**

You can clone this project from Github by following these steps:
1. Visit the [Github repository](https://github.com/DelroyBrown28/VinylProject_2).
2. At the top click the dropdown labelled "Code".
3. Copy/paste the HTTPS URL
4. In the terminal type ```git clone https://github.com/DelroyBrown28/VinylProject_2.git```
5. Hit enter and the repository will be cloned to your machine.<br><br>

   You can run the project by simply following this link on Heroku to [db-vinylproject](https://db-vinylproject.herokuapp.com/)<br>
___

### <div align="center">Credits</div>

##### Media:
[Placeit.net](https://placeit.net/) - For vinyl image mockups.

[Photoshop](https://www.photoshop.com/en) - For editing vinyl sleeve art.

[Flaticon.com](https://www.flaticon.com/) - For all icons.

##### Code:
- [Bootstrap4](https://getbootstrap.com/)
- [MaterializeCSS](https://materializecss.com/)
- [JQuery](https://jquery.com/)
- [Django](https://www.djangoproject.com/) 
