
# Functional Testing

## Epic - Home App

### US#3 - View the home page
| Expected                                           | When                                               | Result |
|----------------------------------------------------|----------------------------------------------------|--------|
| Display home page content                          | Navigate to home page                              | Pass   |
| Display 'Page not found' - 404 page                | Navigate to a non-existent page                    | Pass   |
| Display 'Forbidden'- 403 page                      | Attempt to access unauthorized page/view           | Pass   |
| Navigates to 'All Products' page                   | Click on 'Shop Now' button from homepage jumbotron | Pass   |
| Navigate to 'Privacy Policy' site in a new tab     | Click on 'Privacy Policy' link in the footer       | Pass   |
| Navigate to 'Developer's github' page in a new tab | Click on 'Petru Chelban 2023' link in the footer   | Pass   |


### US#4 - Navigate the site
| Expected                                                                                    | When                                                               | Result |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| Navigates to 'All Products' page                                                            | Click on 'All Products' from 'All Products' from navigation menu   | Pass   |
| Navigates to 'Products' page listing all products sorted by **price**                       | Click on 'By Price' from 'All Products' from navigation menu       | Pass   |
| Navigates to 'Products' page listing all products sorted by **rating**                      | Click on 'By Rating' from 'All Products' from navigation menu      | Pass   |
| Navigates to 'Products' page listing all products sorted by **category**                    | Click on 'By Category' from 'All Products' from navigation menu    | Pass   |
| Navigates to 'Products' page listing products filtered by brewing method **coffee beans**   | Click on 'Coffee Beans' from 'All Products' from navigation menu   | Pass   |
| Navigates to 'Products' page listing products filtered by brewing method **ground coffee**  | Click on 'Ground Coffee' from 'All Products' from navigation menu  | Pass   |
| Navigates to 'Products' page listing products filtered by brewing method **instant coffee** | Click on 'Instant Coffee' from 'All Products' from navigation menu | Pass   |
| Navigates to 'Products' page listing products filtered by brewing method **cappuccino**     | Click on 'Cappuccino' from 'All Products' from navigation menu     | Pass   |
| Navigates to 'Products' page listing products filtered by intensity **mild**                | Click on 'Mild' from 'All Products' from navigation menu           | Pass   |
| Navigates to 'Products' page listing products filtered by intensity **medium**              | Click on 'Medium' from 'All Products'  from navigation menu        | Pass   |
| Navigates to 'Products' page listing products filtered by intensity **strong**              | Click on 'Strong' from 'All Products' from navigation menu         | Pass   |
| Navigates to 'Products' page listing products filtered by intensity **intense**             | Click on 'Intense' from 'All Products' from navigation menu        | Pass   |
| Navigates to 'Products' page listing products filtered by **new arrivals**                  | Click on 'New Arrivals' from 'Deals' navigation menu               | Pass   |
| Navigates to 'Products' page listing products filtered by **deals**                         | Click on 'Deals' from 'Deals' navigation menu                      | Pass   |
| Navigates to 'Products' page listing products filtered by **clearance**                     | Click on 'Clearance' from 'Deals' navigation menu                  | Pass   |
| Navigates to 'Products' page listing products filtered by **all specials**                  | Click on 'All Specials' from 'Deals' navigation menu               | Pass   |
| Navigates to 'Blog' page                                                                    | Click on 'Blog' from  navigation menu                              | Pass   |
| Navigates to 'Testimonials' page                                                            | Click on 'Testimonials' from  navigation menu                      | Pass   |
| Navigates to 'Contact' page                                                                 | Click on 'Contact' from navigation menu                            | Pass   |
| Navigates to 'Register' page                                                                | Click on 'Register' from 'My Account' navigation menu              | Pass   |
| Navigates to 'Basket' page                                                                  | Click on basket icon from top-right corner of the page             | Pass   |


### US#5 - Search
| Expected                                                                                    | When                                                                            | Result |
|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------|
| Navigates to 'Search results' page showing all search results containing **azera**          | Type 'azera' in the search box at the top of the page and click on Search icon  | Pass   |


### US#6 - Testimonial section
| Expected                                                   | When                                                              | Result |
|------------------------------------------------------------|-------------------------------------------------------------------|--------|
| Displays recent testimonials from previous customers/users | Navigate to home page and scroll down to 'Customer testimonials'  | Pass   |


### US#7 - Social media
| Expected                                      | When                                                                       | Result |
|-----------------------------------------------|----------------------------------------------------------------------------|--------|
| Displays social media icons/links             | Navigate to any page of the site and scroll down to the bottom of the page | Pass   |
| Navigate to social media site in a new tab    | Clicking on any of social media sites                                      | Pass   |


### US#8 - Subscribe to newsletter
| Expected                                          | When                                                                                                                                                               | Result |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Displays a subscription confirmation notification | Navigate to home page and scroll down to the bottom of the page. <br/>Enter a valid email address in the 'Email Address' text field and click 'Subscribe' button   | Pass   |


### US#24 - Notifications
| Expected                                      | When                                                                                                                               | Result |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------|
| Displays a notification about success/errors  | Perform authorised/unauthorised actions on the Home, Products, Basket, Checkout, Blog, Testimonials, Contact, Login, Register apps | Pass   |




## Epic - Profile App

### US#9 - Account Registration
| Expected                                                     | When                                                                                                                                                               | Result |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Displays a registration confirmation notification            | On the 'Registration' page enter valid values for all fields and click on 'Sign Up' button                                                                         | Pass   |
| Display an error that an user with such email already exists | On the 'Registration' page enter valid values for all fields <br/>and use an email that was previously registered on the site <br/>and click on 'Sign Up' button   | Pass   |


### US#10 - Confirmation email
| Expected                                                     | When                                                                                                                                                               | Result |
|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| An email is received to the registered email                 | On the 'Registration' page enter valid values for all fields and click on 'Sign Up' button                                                                         | Pass   |


### US#11 - Login/Logout
| Expected                                    | When                                                                                    | Result |
|---------------------------------------------|-----------------------------------------------------------------------------------------|--------|
| Login to my account     | On the 'Login' page enter valid username and password and click on 'Sign In' button                         | Pass   |
| Log out from my account | On any page of the site click on the 'Logout' from 'My Account' navigation item from top-right of the page  | Pass   |


### US#12 - Password recovery
| Expected                                                                    | When                                                                                                                                            | Result |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| An email is received on the entered email with a link to reset the password | On the 'Password Reset' page enter already registered user's email in the email address text field <br/>and click on 'Reset My Password' button | Pass   |


### US#13 - User profile
| Expected                                                                         | When                                                                                                                                                                                                          | Result |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Displays user profile information (phone number, post address) and Order History | On any page of the site click on the 'My Profile' from 'My Account' navigation item from top-right of the page                                                                                                | Pass   |
| Updates user profile information (phone number, post address...)                 | While on 'My Profile' page  <br/>  press 'Update information' with correctly filled out form                                                                                                                  | Pass   |
| Saves/Updates user profile information (phone number, post address...)           | While on 'Checkout' page  <br/>  tick 'Save this delivery information to my profile' checkbox <br/> with correctly filled out form <br/> and press 'Complete order' button at the bottom on the Checkout page | Pass   |
| Displays Order confirmation screen for the selected order                        | While on 'My Profile' page  <br/>  press any individual 'Order number' in the 'Order History'                                                                                                                 | Pass   |



## Epic - Products App

### US#14 - Products
| Expected                                                                               | When                                                                                  | Result |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|--------|
| Displays Products page with a different list of products depending on the link clicked | Click on links of the 'All Products' or 'Deals' from navigation menu                  | Pass   |
| Display the Products from the selected Category                                        | Click on the 'Category name' from any individual product's description                | Pass   |
| Display All Products                                                                   | Click on the 'Products Home' from above and left of Products                          | Pass   |
| Display the Products from the selected Category or Deals                               | Click on the 'Category name' or 'Deals name' from the links below of the page heading | Pass   |


### US#15 - Sort
| Expected                                        | When                                                                                 | Result |
|-------------------------------------------------|--------------------------------------------------------------------------------------|--------|
| Sorts the Products by selected criteria         | Click on the 'Sort by' and click on any of the sorting options from sorting box menu | Pass   |


### US#16 - Product details
| Expected                                            | When                                                                                   | Result |
|-----------------------------------------------------|----------------------------------------------------------------------------------------|--------|
| Displays Products details page                      | Click on any individual product's picture from the Products page                       | Pass   |
| Display the Products from the selected Category     | Click on the 'Category name' from any individual product's description                 | Pass   |
| Changes the quantity of products in the input field | Click on any '+' and '-' buttons around input field on the Product details page        | Pass   |
| Adds the Product to the Basket                      | Click on the 'Add to basket' button bellow the input field on the Product details page | Pass   |
| Navigates to 'All Products' page                    | Click on the 'Keep shopping' button bellow the input field on the Product details page | Pass   |


### US#17 - Product CRUD functionality
| Expected                            | When                                                                                                                                    | Result |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------|
| Displays Product CRUD functionality | On the Products page, Products detail page and My Account menu when logged in as a administrator                                        | Pass   |
| Displays Add Product page           | On any page of the site click on the 'Product Management' from 'My Account' navigation item from top-right of the page                  | Pass   |
| Display All Products page           | Click on the 'Cancel' button bellow the form on the 'Product Management' page                                                           | Pass   |
| Adds a new product to the database  | Click on the 'Add Product' button bellow the form on the 'Product Management' page with at least required fields filled out in the form | Pass   |
| Displays Edit a Product page        | On the Products page, Products detail page when pressing 'Edit' in the any individual product's description                             | Pass   |
| Display All Products page           | Click on the 'Cancel' button bellow the form on the 'Edit a Product' page                                                               | Pass   |
| Updates the product                 | Click on the 'Update Product' button bellow the form on the 'Edit a Product' page with at least required fields filled out in the form  | Pass   |
| Deletes the product                 | On the Products page, Products detail page when pressing 'Delete' in the any individual product's description                           | Pass   |

## Epic - Basket App 

### US#18 - Add to basket
| Expected                                     | When                                                                                     | Result |
|----------------------------------------------|------------------------------------------------------------------------------------------|--------|
| Adds the Product to the Basket               | Click on the 'Add to basket' button bellow the input field on the Product details page   | Pass   |


### US#19 - View shopping basket
| Expected                                                   | When                                                                                                                | Result |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------|
| Displays the Basket page                                   | Click on basket icon from top-right corner of the page                                                              | Pass   |
| Displays the Basket page                                   | Click on basket 'Go to secure checkout' button in the mini basket notification after adding a product to the basket | Pass   |
| Display All Products page                                  | Click on the 'Keep shopping' button at the bottom on the Basket page                                                | Pass   |
| Display Checkout page                                      | Click on the 'Secure checkout' button at the bottom on the Basket page                                              | Pass   |
| Display Free delivery threshold bellow the navigation menu | Navigate to any page                                                                                                | Pass   |


### US#20 - Update shopping basket
| Expected                                            | When                                                                       | Result |
|-----------------------------------------------------|----------------------------------------------------------------------------|--------|
| Changes the quantity of products in the input field | Click on any '+' and '-' buttons around input field on the Basket page     | Pass   |
| Updates the product quantity in the basket          | Click on the 'Update' button bellow the input field on the Basket page     | Pass   |


### US#21 - Remove from basket
| Expected                                            | When                                                                       | Result |
|-----------------------------------------------------|----------------------------------------------------------------------------|--------|
| Removes the product from the basket                 | Click on the 'Remove' button bellow the input field on the Basket page     | Pass   |


### US#22 - Shopping basket total
| Expected                         | When                    | Result |
|----------------------------------|-------------------------|--------|
| Displays Grand total to be payed | While on to Basket page | Pass   |


### US#23 - Basket notification
| Expected                                                  | When                                                   | Result |
|-----------------------------------------------------------|--------------------------------------------------------|--------|
| Displays mini basket notification with the current basket | Adding, updating, removing products to/from the basket | Pass   |


## Epic - Checkout App 

### US#25 - Contact details and delivery address
| Expected                 | When                                                                    | Result |
|--------------------------|-------------------------------------------------------------------------|--------|
| Display Checkout page    | Click on the 'Secure checkout' button at the bottom on the Basket page  | Pass   |


### US#26 - Checkout/pay
| Expected                                   | When                                                                                                     | Result |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------|--------|
| Checkout/pay for the products in my basket | Click on the 'Complete order' button, with correctly filled out form, at the bottom on the Checkout page | Pass   |


### US#27 - Checkout/pay
| Expected                           | When                                                                                                                                                  | Result |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Display Checkout confirmation page | Click on the 'Complete order' button, with correctly filled out form, at the bottom on the Checkout page <br> & Stripe successfully charging the card | Pass   |


### US#28 - Checkout confirmation email
| Expected                            | When                                                                                                                                                  | Result |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Receive Checkout confirmation email | Click on the 'Complete order' button, with correctly filled out form, at the bottom on the Checkout page <br> & Stripe successfully charging the card | Pass   |


### US#29 - Admin view placed orders
| Expected                   | When                                                                                                                                          | Result |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Admin view placed orders   | Navigate to 'https://petrugio-s-coffee.herokuapp.com/admin/' <br> login with admin credentials <br> press 'Orders' link in the 'Checkout' app | Pass   |


### US#30 - Admin edit placed orders
| Expected                               | When                                                                                                                                                                                     | Result |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Admin successfully edit a placed order | While on the 'Orders' page in Django admin <br> press on any individual order from the list <br> change any of the order details <br> and press 'Save' button at the bottom of the order | Pass   |

### US#32 - Admin delete placed orders
| Expected                                 | When                                                                                                                                                                                                                                   | Result |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Admin successfully delete a placed order | While on the 'Orders' page in Django admin <br> press on any individual order from the list <br> and press 'Delete' button at the bottom of the order <br> & confirm on the next page                                                  | Pass   |
| Admin successfully delete a placed order | While on the 'Orders' page in Django admin <br> tick the checkbox beside any individual order from the list <br> in the 'Actions' above the orders <br> select 'Delete selected Orders' and press 'Go' <br> & confirm on the next page | Pass   |


## Epic - Blog app

### US#33 - View blogs
| Expected          | When                                            | Result |
|-------------------|-------------------------------------------------|--------|
| Display Blog page | Click on 'Blog' from  navigation menu           | Pass   |
| Display Blog page | Click on 'Back to blogs' from  Blog detail page | Pass   |


### US#34 - View blog details
| Expected                 | When                                                      | Result |
|--------------------------|-----------------------------------------------------------|--------|
| Display Blog detail page | Click on  any individual 'Blog image' from the Blog page  | Pass   |


### US#35 - Like a blog post
| Expected                           | When                                                                                            | Result |
|------------------------------------|-------------------------------------------------------------------------------------------------|--------|
| Likes/unlikes any individual Blog  | While logged in & on the 'Blog detail' page click on 'Heart image button' bellow the blog image | Pass   |


### US#36 - Admin CRUD blog post
| Expected                         | When                                                                                                                                                                                                                               | Result |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Admin view Blogs                 | Navigate to 'https://petrugio-s-coffee.herokuapp.com/admin/' <br> login with admin credentials <br> press 'Blogs' link in the 'Blog' app                                                                                           | Pass   |
| Admin successfully add a Blog    | While on the 'Blogs' page in Django admin <br> press on '+ Add Blog' button <br> fill out the form <br> and press 'Save' button at the bottom of the blog                                                                          | Pass   |
| Admin successfully edit a Blog   | While on the 'Blogs' page in Django admin <br> press press on any individual Blog from the list <br> edit the form <br> and press 'Save' button at the bottom of the blog                                                          | Pass   |
| Admin successfully delete a Blog | While on the 'Blogs' page in Django admin <br> press on any individual Blog from the list <br> and press 'Delete' button at the bottom of the Blog <br> & confirm on the next page                                                 | Pass   |
| Admin successfully delete a Blog | While on the 'Blogs' page in Django admin <br> tick the checkbox beside any individual Blog from the list <br> in the 'Actions' above the Blogs <br> select 'Delete selected blogs' and press 'Go' <br> & confirm on the next page | Pass   |

## Epic - Testimonials app

### US#37 - View Testimonials
| Expected                         | When                                                                                                                          | Result |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------|
| Display Testimonials page        | Click on 'Testimonials' from  navigation menu                                                                                 | Pass   |
| Display Testimonials page        | Click on 'Back to Testimonials' from  Testimonial detail page                                                                 | Pass   |
| Display Testimonials page        | While logged in & made at least one order & on the 'Add Testimonial' page <br> press 'Cancel' button below the form           | Pass   |
| Display Testimonials page        | While logged in & written at least one Testimonial & on the 'Edit Testimonial' page <br> press 'Cancel' button below the form | Pass   |
| Display Testimonial detail page  | Click on  any individual 'Testimonial card' from the Testimonials page                                                        | Pass   |


### US#38 - Users CRUD testimonials
| Expected                               | When                                                                                                                                                                                                                                       | Result |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Successfully Add a Testimonial         | While logged in & made at least one order & on the 'Testimonials' page <br> press 'Add Testimonial' button bellow the page title <br> correctly fill out the form and press 'Add Testimonial' button below the form                        | Pass   |
| Successfully Edit a Testimonial        | While logged in & written at least one Testimonial & on the 'Testimonials' or 'Testimonial detail' page <br> press 'Edit' in your own Testimonial's card <br> correctly edit the form and press 'Update Testimonial' button below the form | Pass   |
| Successfully Delete a Testimonial      | While logged in & written at least one Testimonial & on the 'Testimonials' or 'Testimonial detail' page <br> press 'Delete' in your own Testimonial's card                                                                                 | Pass   |


### US#39 - Admin delete testimonials
| Expected                                    | When                                                                                                                                                                                                                                                           | Result |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Successfully Delete a Testimonial (Website) | While logged in as admin &  on the 'Testimonials' or 'Testimonial detail' page <br> press 'Delete' on any Testimonial's card                                                                                                                                   | Pass   |
| Admin view Blogs                            | Navigate to 'https://petrugio-s-coffee.herokuapp.com/admin/' <br> login with admin credentials <br> press 'Testimonials' link in the 'Testimonials' app                                                                                                        | Pass   |
| Admin successfully add a Testimonial        | While on the 'Testimonials' page in Django admin <br> press on '+ Add Testimonials' button <br> fill out the form <br> and press 'Save' button at the bottom of the Testimonial                                                                                | Pass   |
| Admin successfully edit a Testimonial       | While on the 'Testimonials' page in Django admin <br> press on any individual Testimonial from the list <br> edit the form <br> and press 'Save' button at the bottom of the Testimonial                                                                 | Pass   |
| Admin successfully delete a Testimonial     | While on the 'Testimonials' page in Django admin <br> press on any individual Testimonial from the list <br> and press 'Delete' button at the bottom of the Testimonial <br> & confirm on the next page                                                        | Pass   |
| Admin successfully delete a Testimonial     | While on the 'Testimonials' page in Django admin <br> tick the checkbox beside any individual Testimonial from the list <br> in the 'Actions' above the Testimonials <br> select 'Delete selected Testimonials' and press 'Go' <br> & confirm on the next page | Pass   |

## Epic - Contact app

### US#40 - User submit message
| Expected                    | When                                                                                                                            | Result |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------|
| Successfully send a message | Either logged in or not & while on the 'Contact' page <br> correctly fill out the form and press 'Submit' button below the form | Pass   |
| Navigate to home page       | Either logged in or not & while on the 'Contact' page press 'Back to home' button below the form                                | Pass   |


### US#41 - Admin view messages
| Expected                                    | When                                                                                                                                                                                                                                                         | Result |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Admin view Contact messages                 | Navigate to 'https://petrugio-s-coffee.herokuapp.com/admin/' <br> login with admin credentials <br> press 'Contact' link in the 'Contact' app                                                                                                                | Pass   |
| Admin successfully add a Contact message    | While on the 'Contact' page in Django admin <br> press on '+ Add Contact' button <br> fill out the form <br> and press 'Save' button at the bottom of the Contact                                                                                            | Pass   |
| Admin successfully edit a Contact message   | While on the 'Contact' page in Django admin <br> press press on any individual Contact message from the list <br> edit the form <br> and press 'Save' button at the bottom of the Contact                                                                    | Pass   |
| Admin successfully delete a Contact message | While on the 'Contact' page in Django admin <br> press on any individual Contact message from the list <br> and press 'Delete' button at the bottom of the Contact <br> & confirm on the next page                                                           | Pass   |
| Admin successfully delete a Contact message | While on the 'Contact' page in Django admin <br> tick the checkbox beside any individual Contact message from the list <br> in the 'Actions' above the Contact messages <br> select 'Delete selected Contact' and press 'Go' <br> & confirm on the next page | Pass   |

Back to [README.md](README.md)