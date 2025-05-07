
def traffic_light_agent(light_color):
    actions = {"red": "Stop", "yellow": "Slow down", "green": "Move"}
    return actions.get(light_color.lower(), "Invalid light color")

print(traffic_light_agent("Red"))
print(traffic_light_agent("Green"))
print(traffic_light_agent("Blue"))
