# Generate 50 rows and 4 columns of data
import numpy as np

new_data = np.random.random((50,4))
np.savetxt("main.csv", new_data, fmt = "%.2f", delimiter=",", header = "H1, H2, H3, H4")


# Read CSV File
reading_csv = np.loadtxt("main.csv", delimiter=",")
reading_csv[:4, :]


# Pickle
import pickle

#Write to Pickle File
ordering = {"First":1, "Second":2, "Third":3}
pickle.dump(ordering, open("new.pkl", "wb"))

#Read from Pickle File
reading_pickle = pickle.load(open("new.pkl", "rb"))1


reading_pickle


import json

college = {
"college": "Engineering College",
"objectives": "Mastering Electrical and Computer Engineering",
"departments": {
"dep1": "Electical",
"dep2": "Computer"
},
"years":[
"year 1",
"year 2",
"year 3",
"year 4"
],
"numbers":[1, 2, 3, 4],
"ID":[10, 20, 30, 40]
}

json.dump(college, open("college.json", "w"))

new_college = json.load(open("college.json", "r"))
new_college