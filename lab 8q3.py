def automatic_door_agent(person_detected, time_of_day, authorized_person=False):
    if time_of_day == "night" and not authorized_person:
        return "Door stays closed for security reasons."
    return "Door opens" if person_detected else "Door closes"
print(automatic_door_agent(True, "day"))
print(automatic_door_agent(False, "day"))
print(automatic_door_agent(True, "night", authorized_person=False))
print(automatic_door_agent(True, "night", authorized_person=True)) 
