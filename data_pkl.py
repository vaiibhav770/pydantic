import pickle

records=[
    {"age": 25, "weight": 70, "height": 1.75, "income_lpa": 5, "smoker": False, "city": "Bangalore", "occupation": "teacher"},
    {"age": 35, "weight": 80, "height": 1.80, "income_lpa": 10, "smoker": True, "city": "Chennai", "occupation": "doctor"},
    {"age": 45, "weight": 90, "height": 1.85, "income_lpa": 15, "smoker": False, "city": "Hyderabad", "occupation": "army"},
    {"age": 55, "weight": 100, "height": 1.90, "income_lpa": 20, "smoker": True, "city": "Pune", "occupation": "police"},
    {"age": 65, "weight": 110, "height": 1.95, "income_lpa": 25, "smoker": False, "city": "Mumbai", "occupation": "teacher"},
    {"age": 75, "weight": 120, "height": 2.00, "income_lpa": 30, "smoker": True, "city": "Kolkata", "occupation": "doctor"},
    {"age": 85, "weight": 130, "height": 2.05, "income_lpa": 35, "smoker": False, "city": "Delhi", "occupation": "army"},
    {"age": 95, "weight": 140, "height": 2.10, "income_lpa": 40, "smoker": True, "city": "Jaipur", "occupation": "police"},
    {"age": 105, "weight": 150, "height": 2.15, "income_lpa": 45, "smoker": False, "city": "Lucknow", "occupation": "teacher"},
    {"age": 115, "weight": 160, "height": 2.20, "income_lpa": 50, "smoker": True, "city": "Ahmedabad", "occupation": "doctor"}
]

with open("gg.pkl", "wb") as f:
    pickle.dump(records, f)