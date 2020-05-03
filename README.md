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

git clone https://github.com/plotly/dash-sample-apps
cd dash-sample-apps/apps/dash-financial-report
pip install -r requirements.txt

```

Setup the mongodb with a collection like the collection in the example_project_json.json


Run the app

```

python app.py

```

default Username and Password is 'root' and 'root'

## About the app

This is an interactive, multi-page app.


