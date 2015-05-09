#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_count = 0

for person in enron_data:
    if enron_data[person]["poi"]:
        poi_count = poi_count + 1

print poi_count

salary_count = 0
for person in enron_data:
    if not math.isnan(float(enron_data[person]["salary"])):
        salary_count = salary_count + 1

print salary_count

email_count = 0
for person in enron_data:
    if enron_data[person]["email_address"] != "NaN":
        email_count = email_count + 1

print email_count

no_total_payment_count = 0
no_total_payment_poi_count = 0
for person in enron_data:
    if enron_data[person]["total_payments"] == "NaN":
        no_total_payment_count = no_total_payment_count + 1

        if enron_data[person]["poi"]:
            no_total_payment_poi_count = no_total_payment_poi_count + 1

print no_total_payment_count
print no_total_payment_poi_count