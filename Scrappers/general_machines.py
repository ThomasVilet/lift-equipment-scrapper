from bs4 import BeautifulSoup
from difflib import SequenceMatcher
import requests
import re

class Equipment:
    def __init__(self, name, category, type_, muscle):
        self.name = name
        self.category = category
        self.type = type_
        self.muscle = muscle
    def __repr__(self):
        return f"Equipment(name='{self.name}', category='{self.category}', type='{self.type}', muscle='{self.muscle}')"
    def get_equipment():
        return equipment_objects

# Function to clean and filter h3 tags
def clean_h3(tag):
    text = re.sub(r'^\d+\.?\s*', '', tag.text).strip()
    exclude_keywords = [
        'related', 'tips', 'record', 'review', 'latest', 'mr. olympia', 'exercise', 
        'strength', 'build', 'technique', 'method', 'glutes', 'discusses', 'comeback',
        'total protein', 'topic', 'news', 'tricks', 'how to', 'vidur', 'more', 'home gym'
    ]
    if any(keyword in text.lower() for keyword in exclude_keywords) or len(text.split()) > 5:
        return None
    return text

# Function to clean and filter trs tags
def clean_trs(tr):
    text = re.sub(r'^\d+\.?\s*', '', tr.text).strip()
    exclude_keywords = ['home']
    if any(keyword in text.lower() for keyword in exclude_keywords) or len(text.split()) > 5:
        return None
    return text

# Funtion to remove duplicates that are similar - takes in two values and compares similarity - removes if too similar (excludes machines vs free-weight)
def remove_similar_duplicates(equipment):
    unique_equipment = []
    for i, eq in enumerate(equipment):
        is_duplicate = False
        for unique_eq in unique_equipment:
            # Compare only if both items are either machines or free-weight, not between them
            if ('machine' in eq.lower() and 'machine' in unique_eq.lower()) or \
               ('machine' not in eq.lower() and 'machine' not in unique_eq.lower()):
                similarity_ratio = SequenceMatcher(None, eq.lower(), unique_eq.lower()).ratio()
                if similarity_ratio > 0.8:  # Threshold for considering two items too similar
                    is_duplicate = True
                    break
        if not is_duplicate:
            unique_equipment.append(eq)
    return unique_equipment

def categorize_equipment(name):
    name_lower = name.lower()
    if 'machine' in name_lower:
        return "Strength", "Machine", None
    elif any(weight in name_lower for weight in ["dumbbell", "lat", "barbell", "kettlebell", "pull up", "pull-up", "t-bar", "bench", "curl", "press", "fly", "row", "dip", "dips"]):
        return "Strength", "Free-weight", None
    elif any(weight in name_lower for weight in ["cable"]):
        return "Strength", "Cable", None
    elif any(cardio in name_lower for cardio in ["treadmill", "bike", "elliptical", "stairmaster", "vertical climber", "rowing machine"]):
        return "Cardio", "Machine" if "machine" in name_lower else "Machine", "Cardio"
    elif any(cardio in name_lower for cardio in ["running"]):
        return "Cardio", "Free-weight", "Cardio"
    elif any(core in name_lower for core in ["ab", "roller", "ball"]):
        return "Core", "Free-weight", "Abs"
    else:
        return "Other", "Free-weight", "Misc"


# Extract and clean data from fitnessvolt.com
url_2 = "https://fitnessvolt.com/gym-equipments/"
result2 = requests.get(url_2).text
doc2 = BeautifulSoup(result2, "html.parser")

h3_tags = doc2.find_all('h3')
cleaned_tags = [clean_h3(h3) for h3 in h3_tags if clean_h3(h3)]

# Extract and clean data from gymperson.com
# url_1 = "https://gymperson.com/gym-equipment-names-with-pictures-videos/"
# result1 = requests.get(url_1).text
# doc1 = BeautifulSoup(result1, "html.parser")

# print(doc1)
# tbody = doc1.tbody
# trs = tbody.contents

# cleaned_trs = []
# for tr in trs:
#     for td in tr.contents:
#         equipment = clean_trs(td)
#         if equipment:
#             cleaned_trs.append(equipment)

# Combine both lists and remove duplicates
# combined_list = list(set(cleaned_tags + cleaned_trs))
combined_list = list(set(cleaned_tags))

# Sort the combined list alphabetically (optional)
combined_list.sort()

# Clean list again for similar duplicates
cleaned_list = remove_similar_duplicates(combined_list)

# Create equipment objects
equipment_objects = []
for equipment in cleaned_list:
    category, type_, muscle = categorize_equipment(equipment)
    equipment_objects.append(Equipment(name=equipment, category=category, type_=type_, muscle=muscle))
