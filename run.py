"""
    The tail of 2 curious kitties on a quest for endless fish
"""

game_text = {
        "step_1": {
            "step_text":
    """
    Our furry-tail begins in a small village with two curious cats named
    Meowshmallow and Peppurrmint who heard tales of the legendary golden fish.
    This magical fish was said to provide an endless supply of food
    to whomever caught it. Intrigued by the story,
    Meowshmallow and Peppurrmint decide to embark on an adventure
    to find this elusive fish.
    As they set out on their journey, they come across two possible paths:
    Option 1: Do they follow the river upstream?
    Option 2: Or do they venture into the dense forest?
    """,
            "option_1": "step_2", 
            "option_2": "step_3"
        },
        "step_2": {
            "step_text": 
    """
    Meowshmallow and Peppurrmint follow the river upstream,
    hoping it would lead them to the golden fish. Along the way,
    they discover a wise old turtle who offers them advice.
    The turtle says to them: 'The golden fish lives in a hidden lake,
    but the path is treacherous. You must choose wisely.'
    Option 1: Do they ask the turtle for guidance?
    Option 2: Or do they continue without the turtle's help?
    """,
            "option_1": "step_4", 
            "option_2": "step_5"
        },
        "step_3": {
            "step_text":
    """
    Meowshmallow and Peppurrmint venture into the dense forest,
    relying on their keen senses to guide them.
    Soon, they stumble upon a chatty squirrel who claims to know
    the whereabouts of the golden fish.
    Option 1: Do they trust the squirrel and follow its directions?
    Option 2: Or do they doubt the squirrel and find their own way?
    """,
            "option_1": "step_6",
            "option_2": "step_7"
        },
        "step_4": {
            "step_text":
    """
    With the turtle's guidance, Meowshmallow and Peppurrmint manage
    to find the hidden lake. As they approache, they notice two different
    spots they could possibly catch the fish from:
    Option 1: Do they pick the open spot near the water's edge?
    Option 2: Or do they pick the secluded spot beneath the willow tree?
    """,
            "option_1": "step_8",
            "option_2": "step_9"
        },
        "step_5": {
            "step_text":
    """
    Meowshmallow and Peppurrmint continue their journey without
    the turtle's help. They soon find a lake that seems promising.
    They notice two different spots they could possibly catch the fish from:
    Option 1: Do they pick the open spot near the water's edge?
    Option 2: Or do they pick the secluded spot beneath the willow tree?
    """,
            "option_1": "step_10",
            "option_2": "step_11"
        },
        "step_6": {
            "step_text":
    """
    Trusting the squirrel's directions, Meowshmallow and Peppurrmint arrive
    at the hidden lake. Looking around, they see two possible fishing spots:
    Option 1: Do they pick the open spot near the water's edge?
    Option 2: Or do they pick the secluded spot beneath the willow tree?
    """,
            "option_1": "step_12",
            "option_2": "step_13"
        },
        "step_7": {
            "step_text":
    """
    Meowshmallow and Peppurrmint decide not to trust the squirrel and forge
    their own path. Eventually, they stumble upon a lake. They notice two
    different spots they could possibly catch the fish from:
    Option 1: Do they pick the open spot near the water's edge?
    Option 2: Or do they pick the secluded spot beneath the willow tree?
    """,
            "option_1": "step_14",
            "option_2": "step_15"
        },
        "step_8": {
            "step_text":
    """
    Choosing the open spot with the guidance of the turtle, 
    Meowshmallow and Peppurrmint catch the golden fish!
    """
        },
        "step_9": {
            "step_text":
    """
    Choosing the secluded spot, despite the turtle's guidance, leads to no
    sign of the golden fish.
    """
        },
        "step_10":{
            "step_text":
    """
    Choosing the open spot without the turtle's guidance turned out to be a misstep,
    they find no sign of the golden fish.
    """
        },
        "step_11": {
            "step_text":
    """
    Choosing the secluded spot without the turtle's guidance turned out to be the right
    choice! They found and caught the golden fish!
    """
        },
        "step_12": {
            "step_text":
    """
    Choosing the open spot with the squirrel's guidance, 
    they caught the golden fish!
    """
        },
        "step_13": {
            "step_text":
    """
    Choosing the secluded spot, despite the squirrel's guidance, led to no
    sign of the golden fish.
    """
        },
        "step_14": {
            "step_text":
    """
    Choosing the open spot without the squirrel's guidance led to no sign of
    the golden fish.
    """
        },
        "step_15": {
            "step_text": 
    """
    Choosing the secluded spot without the squirrel's guidance turned out to
    be the right choice! They found and caught the golden fish.
    """
        }
    }

def show_step(step):
    """
        Initial function to show step 1 with options and receive input from
        the user. Depending on the input, there will be different outcomes.
    """
    print(step["step_text"])
    user_input = input("""Write your choice (either 1 or 2):""")
    if user_input == "1":
        show_step(game_text[step["option_1"]])
    else:
        print("They go into the forest (and go to step 3)")

show_step(game_text["step_1"])


# End text for success
ENDING_1 = """
Success: Meowshmallow and Peppurrmint return home with the golden fish.
True to the legend, it provides them with an endless supply of food, and they
live happily ever after.
"""

# End text for failure
ENDING_2 = """
Failure: Despite their best efforts, Meowshmallow and Peppurrmint never find
the golden fish. They return to the farm, but the legend of the golden fish
live on in their hearts.
"""
