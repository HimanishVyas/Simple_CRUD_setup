#Importing JSON Package in Python

import json

#creatig a dictionary which can be converted into JSON string

my_details = {

    "Name" : "Lalit Salunkhe",

    "Age" : 28,

    "Job" : True,

    "Married" : False,

    "Bikes" : [

        {"Model1": "Jupiter 120", "price": 62000},

        {"Model2": "Yamaha YZF-R15", "price": 150000}

        ]

    }
res = json.dumps(my_details)
print(res)
print(type(res))