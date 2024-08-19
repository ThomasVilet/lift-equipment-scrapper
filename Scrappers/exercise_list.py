# Clean both files and create objects for every single workout imaginable
from .general_exercises import Lift
from .general_machines import Equipment
from itertools import islice

class Exercise:
    exercises = []

    def __init__(self, name, type_, category, muscle):
        self.name = name # exercise name
        self.type_ = type_ # (Free/Machine/Cable)
        self.category = category # (Stength/Cardio/Core)
        self.muscle = muscle # (targeted muscle/Cardio/Misc)

    def __repr__(self):
        return f"Exercise(name='{self.name}', type_='{self.type_}', category='{self.category}', muscle='{self.muscle}')"
    
    def __eq__(self, other):
        # Consider two exercises equal if they have the same name
        return self.name == other.name

    def __hash__(self):
        # Hash based only on the name
        return hash(self.name)

    @staticmethod
    def get_exercises():
        return exercises
    
def assign_type_and_category(exercise):
    # compare other values and decide the type
    name_to_type = {
        'Machine' : 'Machine',
        'Cable' : 'Cable',
        'With' : 'Cable',
        'Bike' : 'Machine'
    } # else is is free weight
    muscle_to_category = {
        'Cardio' : 'Cardio',
        'Forearm Extensor' : 'Strength',
        'Forearm Flexors / Grip' : 'Strength',
        'Calves' : 'Strength',
        'Abs' : 'Core',
        'Glute' : 'Strength',
        'Back' : 'Strength',
        'Legs' : 'Strength',
        'Tricep' : 'Strength',
        'Bicep' : 'Strength',
        'Chest' : 'Strength',
    }
    for key, type_val in name_to_type.items():
        if key.lower() in exercise.name.lower():
            exercise.type_ = type_val
            break
        else:
            exercise.type_ = 'Free-weight'
    
    for key, category_val in muscle_to_category.items():
        if key.lower() in exercise.muscle.lower():
            exercise.category = category_val
            break
        else:
            exercise.category = 'Other'
    return exercise

def assign_muscle(equipment):
    # fix first vals
    name_to_muscle = {
        'Calf' : 'Calves',
        'Abs' : 'Abs',
        'Core' : 'Abs',
        'Abdominal' : 'Abs',
        'Crunch' : 'Abs',
        'Glute' : 'Glute',
        'Pull' : 'Back',
        'Row' : 'Back',
        'Lat' : 'Back',
        'T-Bar' : 'Back',
        'Leg' : 'Legs',
        'Deadlift' : 'Legs',
        'Hips' : 'Legs',
        'Sled Push' : 'Legs',
        'Leg Curl' : 'Legs',
        'Squat' : 'Legs',
        'Tricep' : 'Tricep',
        'Curl' : 'Bicep',
        'Press' : 'Chest',
        'Pec' : 'Chest',
        'fly' : 'Chest',
        'Chest' : 'Chest',
        'Dip' : 'Chest',
        'Dips' : 'Chest',
        'Crossover' : 'Chest',
        'Bench' : 'Misc'
    }
    for key, muscle_val in name_to_muscle.items():
        if key.lower() in equipment.name.lower():
            equipment.muscle = muscle_val
            break
        elif equipment.muscle == None:
            equipment.muscle = "Misc"
    return equipment

# def add_to_database(exercise):


# lets find duplicates within the two
gen_equipment = Equipment.get_equipment()
gen_exercises = Lift.get_exercise()

exercises = []

for equip in gen_equipment:
    equip = Exercise(name=equip.name, type_=equip.type, category=equip.category, muscle=equip.muscle)
    exercises.append(assign_muscle(equip))

for lift in gen_exercises:
    exer = Exercise(name=lift.name, type_=None, category=None, muscle=lift.body_part)
    exercises.append(assign_type_and_category(exer))

unique_exercises = list(set(exercises))
exercises = unique_exercises

