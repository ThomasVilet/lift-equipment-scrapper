# model of the database
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
from Scrappers.exercise_list import Exercise

printer = pprint.PrettyPrinter()
all_exercises = Exercise.get_exercises()

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://tvilet3:{password}@exerciseinformation.1gntk.mongodb.net/?retryWrites=true&w=majority&appName=ExerciseInformation"
client = MongoClient(connection_string)

dbs = client.list_database_names()
db_exercises = client.Exercises
exer_collection = db_exercises.Exercises

def insert_exercise_docs(exer_list):
    exercise_docs = []
    for doc in exer_list:
        doc = {
            'name': doc.name,
            'type': doc.type_,
            'category': doc.category,
            'muscle': doc.muscle
        }
        exercise_docs.append(doc)
    exer_collection.insert_many(exercise_docs)

def find_all_exercises():
    exercises = exer_collection.find()
    for exercise in exercises:
        printer.pprint(exercise)
