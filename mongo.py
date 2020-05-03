import pandas as pd
from pymongo import MongoClient

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

def get_projects_documents():
    client = MongoClient()
    db = client["Kaveret"]
    projects_collection = db["ProjectsCollection"]
    print("came from mongo: {}".format(projects_collection.find()))
    exclude_col = {'_id': False}  # we are ignoring '_id' column.
    data = list(projects_collection.find({}, projection=exclude_col))  # data is in json format
    # print(data.to_string())
    return data

def get_projects_json():
    data = []
    client = MongoClient()
    db = client["Kaveret"]
    projects_collection = db["ProjectsCollection"]
    print("came from mongo: {}".format(projects_collection.find()))
    for p in projects_collection.find():
        data.append(p)

    print(data)
    return data

'''
THE EXAMPLE BELOW CONTAINS THE INITIAL MONGODB DATA STRUCTURE 
'''
"""
project_initial_document = [{"ID": 1,  # mispar
    "worker": "אנדרי",  # oved metapel
    "status": "לטיפול",
    # סימוכין
    "name": "רוטשילד 22",
    "address": "רוטשילד 22 תל אביב",
    "RealEstateDeveloper": "תדהר",  # yazam
    "ReportNumber": 1,  # mispar doch
    # סטטוס פיור
    "notifications": 5
                                  },
         {"ID": 2,  # mispar
        "worker": "לאון",  # oved metapel
        "status": "לטיפול",
        # סימוכין
        "name": "קניון ראשון",
        "address": "טרומפלדור 44 ראשון",
        "RealEstateDeveloper": "יזם מדהים",  # yazam
        "ReportNumber": 1,  # mispar doch
        # סטטוס פיור
        "notifications": 5
    },
{"ID": 3,  # mispar
        "worker": "אלי",  # oved metapel
        "status": "נשלח",
        # סימוכין
        "name": "תיכון עמית עמל",
        "address": "עמית עמל ראשון",
        "RealEstateDeveloper": "סהר טלמור",  # yazam
        "ReportNumber": 1,  # mispar doch
        # סטטוס פיור
        "notifications": 21
    },
{"ID": 4,  # mispar
        "worker": "אסי",  # oved metapel
        "status": "המתנה",
        # סימוכין
        "name": "ערד החדשה",
        "address": "ים המלח 11 ערד",
        "RealEstateDeveloper": "שריקי",  # yazam
        "ReportNumber": 1,  # mispar doch
        # סטטוס פיור
        "notifications": 3
    }
]"""

if __name__ == '__main__':
    get_projects_json()
