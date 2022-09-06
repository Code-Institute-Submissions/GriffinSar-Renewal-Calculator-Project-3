# Table of Contents

- [Purpose](#purpose)
    - [Target Audience](#target-audience)
- [User-Stories](#user-stories)
    - [First-Time-Visitor-Goals](#first-time-visitor-goals)
    - [Returning-Visitor-Goals](#returning-visitor-goals)
    - [Frequent-Visitor-Goals](#frequent-visitor-goals)
    - [Owner-Goals](#owner-goals)
- [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Imagery](#imagery)
- [Flow-Chart](#flow-chart)
- [Features](#features)
    - [Existing-Features](#existing-features)
    - [Features-left-to-Implement](#features-left-to-implement)
- [Testing](#testing)
    - [Manual-Testing](#manual-testing)
    - [Issues-and-Resolutions](#issues-and-resolutions-found-during-testing)
    - [Validator-Testing](#validator-testing)
    - [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Technologies](#technologies)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)


# Sales Calculator

### Purpose
The purpose of this site is to provide the user with pricing for their renewal quotes. It has specifically created for renewal representitives who work for Quest Software. They input some details: the price, level and product and the system will provide them with the new pricing for this years quote. They can also choose to get the pricing for a 2 year and 3 year quote so they can easily provide all options to the customer.
This program also stores the customer data so that the user can access previous quote prices for their reference. 
The purpose of this site is to streamline the renewal process for these sales representitives. Many of thier quotes need to be manually priced so this site can help them to work out the pricing of a quote in a more efficient way.

# Target Audience
The Target Audience for this website is sales reps specifically the sales reps who work for my current employer Quest software. These reps have a number of manual calculatitons that needs to be done to prepare a quote for their customer, this has to be done for thousands of quotes every three months. Part of my role in the past was to price these quotes for the reps. There is a definate need here for something that makes the process easier and more streamlined. This app is designed to take away some of this manual work so that the sales rep can concentrate on selling the products to the customer rather than focusing so much time on administration work.
This is the sort of functionality that many CRM systems implement to streamline quoting for customers. 

# User Stories

### First Time Visitor Goals
As a first time visitor I want to be able to choose what product I am working with and the support level so I can get an accurate calculation for my renewal quote. 
I also wants to be able to get the price for a 2 or 3 year renewal so I can present the three options to my customer.
I want to be able to input the customer name and spcific data of this quote and have it stored by the system in a google sheet so I can access this data again at a later stage. 
As a first time visitor (Or Returning/ Frequent) I want the program to be simple and easy to use. 
As a first time visitor (Or Returning/ Frequent) I want the system to work even if I input the wrong type of data.

### Returning Visitor Goals
A returning visitor wants to be able to use the app to price a quote just as the first time visitor. But this user also wants to be able to access previous quote data for users so they can see a list of previous priced quotes for this customer.

### Frequent Visitor Goals
A frequent Visitor wants to be able to price new quotes and also get previous pricing for a specific customer if there is any.

# Owner Goals
- As the owner, I want to provide a program that fulfils the users’ needs.
- As the owner, I want to make it immediately obvious what the program is for.
- As the owner, I want to provide clear and accurate information.
- As the owner, I want to create an experience that is pleasant for users.
- As the owner, I want the program to continue without crashing due to an error caused by user input.

# Design

### Colour scheme

As this is a terminal based application the level of detail for colour in page are a little limited. 
I have imported colours from the Python library colorama and also the Python Libary Rich. I have tried to use the colours consistently throughout the program.
- Purple - The introduction message on the home page is in purple 
- Green - All input messages are green to make then stand out to the user.
- Yellow - confirmation messages to the user are yellow
- Red - Error Messages are in Red, this colour is used as Red would be familiar to the user as the colour commonly used for an error.

### Imagery

I have used an image of a calculator, it is just a simple image but draws the users eye. It also helps to make the purpose of the site clear right from the initial page.

![calculator](assets/images/calculator.png)

# Flow Chart

![flowChart](assets/images/chart.png)

# Features 

## Existing Features

### Into Page
When the program loads the user is Greated with text welcoming them to the Renewal Calculator and an image of a calculator. There is a description of what the program does. It then gives the user two options they can either choose to start a new calculation or they can get access to historical data for their customer. 
They are then prompted to enter which option they would like to go for by inputting 1 for new calculation or 2 for historical data.

![intro](assets/images/intro-page.png)

### New Calculation
If the user selects to start a new calculation they are then prompted to enter their customer's name. There is a message outlining the format the customer name must take. If the customer name fits the convention then a message is printed telling the user that the customer name is accepted. If the user enters a format that is not accepted they will recieve and error message telling them the name they have entered is not valid and they will be prompted to re-enter the user name. 

### Product Select
Once the user has entered a customer name that is accepted by the system they will then be prompted to select the product their quote is for, either Toad or Kace. 
If the enter anything other than Toad or Kace they will get an error stating Invalid input and they will be prompted to try again. 

### Level Select
 Once they have entered the amount the user is then asked to select the level of support on the quote, is it standard, mid or premier. The product type and support level determine the pricing that is applied to the quote.

### Enter Amount
The user is then prompted to enter the amount for last years renewal quote.


### Print Calculation
The program then checks the price the user has entered against a price book I have created in a google sheet. 

![pricebook](assets/images/pricebook.png)

 If the price is below what is in the google sheet an uplift is applied but if the user has entered a price that matches or is above the price that is in the price book the system will inform them that the  calculation can not be done as their quote had already reached list  price. 
 If the price is below the list price then the applicable uplift will be applied and the price will be printed.

 ![uplift]()

### PPM Calculation 

The user can also have the system calculate the price for a second and third year. This is calculated at 90% of the 1 year price for the second year and 85% of the one year price for the third year. This is following the pricing guidelines that the reps in my company follow, the discount is applied to incentivies customers to renew for more than one year. So this calculator quickly presents the pricing for all three years.

 ![ppm]()

### Save 
The usesr is then prompted to either save their details or exit. If they choose the save the details are saved to a google sheet. They can then be accessed by the user at a later date by entering the customer name.

### Access stored data
The user can enter the customer  name and any saved details for this customer will be printed to the terminal. It gives the customer name, product, supporot level and the pricing for One, Two and three years. 

 ![saved](assets/images/saved%20details.png)

 ### Note on Features

 - I have chosen to store all input from the user as lower case. This way when they user is accessing their saved details if they used capital letters or not wont matter, it will convert their input to lower case and match the name to the saved lower case details in the google sheet.

 - When the user enters details, if their details are accepted by the program a message will be printed in yellow telling the user it has been accepted. This is good for the user as it lets them know that what they have entered is accepted and the program is running as expected.


 ### Features Left to Implement
Currency converter. I hope in future to implement a currency converter as part of this renewal calculator.

# Testing

### Calculation Testing
The first thing I tested was that the calculations done in the app were actually correct. I built a calculator in Google sheets and gave the input of 30 euro for each support level and type to check what the output was. I then did the same in the calculator I input 30 for each of the types and support level and saved each to the google sheets. All the prices for the uplift and the two and three years matched my google sheet calculation so I know it was working correctly.

As you can see in the two images below the output is the same from the google sheets and the app itself. 

![GoogleSheetsTest](assets/images/google-sheets-test.png)
![AppSavedData](assets/images/app-test.png)

### Manual Testing

### Validator Testing

The Python code was run through the PEP8 online:
![PEP8ERRORS](assets/images/pep8-errors.png)

I initially obtained a large amount of "unexpected space around keyword/parameters equals". I had not realised that I should not put a space between the word style and the equal sign and the parameter for Rich. I removed these spaces across the program and this resolved most of the erros. 

I also recieved some errors for lines being to long. So I spent time making sure that my lines were not longer than 80 characters and that follow on lines were properly indented. 

Once I fixed these issues the code then passed successfully.

![PEP8](assets/images/pep8-pass.png)

# Bugs

## Current Bugs

To the best of my knowledge there are no bugs currently in this program.

## Resolved Bugs

- I had an issue when the user went through and did a new calculation when they went back to the start page and selected to exit the calculator, it wouldnt exit but instead displayed the menu from the save function. I realised I needed to enter break points so that this part of the save function would not keep running when the user exited to the home page. Once I entered them it fixed this bug.

- I was encountering a bug when the user entered anything that wasnt a number. It was causing the program to crash. I implemented a try except block. This handled the exception if the user enters something that isnt a number and instead of crashing the program prints and error and directs the user back to the start of the function.

# Deployment

### Gitpod and GitHub
The Code Institute Python Essentials Template on GitHub was used to develop this project. This template was designed by Code Institute to provide a terminal that can be viewed in the browser.

Steps:

From the link above, click "use this template". You will be taken to a screen to create a new repository from this template.
Give your repository a name.
Click "create repository from template" and your repository will be created.
In the new repository, click the green "Gitpod" button to open the workspace in Gitpod.

### Google Sheets

You must generate credential and provide them to your program to allow your project to access Google Sheets.

Steps to generate the credentials:

- Navigate to the Google Cloud Platform
- Click "select a project".
- Click "new project".
- Give the project a name.
- Click "create".
- From the project's dashboard, select 'APIs and services' and then 'Library'.
- Search for Google Drive API and enable it.
- Select "create credentials".
- From the "Which API are you using?" dropdown menu, choose "Google Drive API".
- For the "What data will you be accessing?" question, select "Application Data".
- For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" question, select "No, I'm not using them".
- Enter a Service Account name.
- In the Role Dropdown box choose Basic > Editor then press Continue.
- Click "Done".
- On the next page, click on the Service Account that has been created.
- On the next page, click on the Keys tab.
- Click on the Add Key dropdown and select Create New Key
- Select JSON and then click Create. This will trigger the json file with your API credentials in it to download to your machine.

Steps to allow the program access using the credentials:

- Drag and drop the downloaded json file containing the credentials into your Gitpod workspace.
- Rename the file to creds.json for ease of use.
- In the creds.json file, find the "client_email" value and copy the email address (without the surrounding quotes).
- In the Google Sheet, click the green "share" button in the top right.
- Paste in the email, make sure "Editor" is selected, untick "Notify People", and then click "Share".

Steps to ensure that the credentials file is stored securely and details are not shared with GitHub:

- Open the "gitignore" file in Gitpod.
- Add "creds.json" (without the quotes) to the gitignore file and save the file.