# Item Catalog Application

#About

The Item Catalog Application provides a list of items within a variety of categories as well as provides a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.You will learn how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. You will then learn when to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

## Set Up

1. Install Vagrant and VirtualBox
2. Clone the Item Catalog Application
3. Launch the Vagrant VM (vagrant up)
4. Write your Flask application locally in the vagrant/catalog directory.
5. Run your application within the VM (python /vagrant/catalog/application.py)
6. Access and test your application by visiting http://localhost:8000 locally

## Google Login

For setting up google authentication follow the steps below:

1.  Go to console.developers.google.com
2.  Sign in with your google accont
3.  Create a new apllication
4.  Go to credentials and select web application
5.  Authorized javascript origin type "http://localhost:5000"
6.  Authorized redirect URIs type "http://localhost/login" and "http://localhost/gconnect"
7.  Create the application.
8.  Download the JSON file and rename it to client_secrets.json and save it to catalog directory.
9.  In login.html type your google client ID in data-clientid. 
10. Run your application within the VM (python /vagrant/catalog/application.py) 
11. Access and test your application by visiting http://localhost:8000 locally

