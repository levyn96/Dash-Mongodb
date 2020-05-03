# Dash MongoDB Integration

This is a small demo web application writen in python with the amazing Plotly Dash.
The app uses pymongo and pandas to integrate with a mongodb data base running on the same machine.
the Dash is used as a web framework, the main component is the DataTable.

## Getting Started

### Running the app locally

First create a virtual environment with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```

Clone the git repo, then install the requirements with pip

```

git clone https://github.com/levyn96/Dash-Mongodb.git

the requirements need to be updated.
pip install -r requirements.txt 

```

<p>Setup the mongodb with a collection like in the example_project_json.json.<br>
Make sure the db name is projects_db and the collection name is ProjectsCollection.<br>
Or change the db and collection name to anything you like, <br>
just make sure to change it also in the ProjectsMainScreen.py layout function.<br>
If you wish to use you own collection you may, but you will have to make some changes,<br> 
mainly in the Add modal that adds a new object to the db.<br>
see the - submit_new_project function in ProjectsMainScreen.py</p>


Run the app

```

python app.py

```

default Username and Password is 'root' and 'root'

## About the app

This is an interactive, multi-page app.


