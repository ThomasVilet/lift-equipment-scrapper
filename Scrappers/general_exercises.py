
from bs4 import BeautifulSoup
import requests

class Lift:
    def __init__(self, name, body_part):
        self.name = name
        self.body_part = body_part
    def __repr__(self):
        return f"Lift(name='{self.name}', body part='{self.body_part}')"
    def get_exercise():
        return exercise_objects

def assign_exercises(body_parts, exercises):
    exercise_objects = []
    # Iterate over body parts and their corresponding exercise lists
    for i in range(len(body_parts)):
        body_part = body_parts[i]
        exercise_list = exercises[i]

        # Create Exercise objects for each exercise in the current list
        for exercise in exercise_list:
            exercise_objects.append(Lift(name=exercise, body_part=body_part))

    return exercise_objects
    
    
url_exercises = "https://www.strengthlog.com/exercise-directory/"
result = requests.get(url_exercises).text
doc = BeautifulSoup(result, "html.parser")

body_part_list = []
exercise_list = []

ol_block = doc.find_all('ol', class_='wp-block-list')
for ol in ol_block:
    temp_list = []
    li_tags = ol.find_all('li')
    for li in li_tags:
        a_tag = li.find('a')
        if a_tag:
            temp_list.append(a_tag.text)
    exercise_list.append(temp_list)

body_part_list = ["Chest", "Shoulder", "Bicep", "Tricep", "Legs", "Back", "Glute", "Abs", "Calves", "Forearm Flexors / Grip", "Forearm Extensor", "Cardio"]

exercise_objects = assign_exercises(body_part_list, exercise_list)

