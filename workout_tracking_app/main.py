#workout tracking in Google Sheets
# Day 38 of 100 Days of Code Angela Yu Python Course
# app_d5fe62aa65b74b3d86c5cf6c
# nix_live_32zPV0GvoajSHIWWvYsPao4YlkVlzS0
# these will be used for header info
import requests

GENDER = 'male'
WEIGHT_KG = 89
HEIGHT_CM = 170
AGE = 56

API_ID= 'app_d5fe62aa65b74b3d86c5cf6c'
API_KEY= 'nix_live_32zPV0GvoajSHIWWvYsPao4YlkVlzS0D'

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)