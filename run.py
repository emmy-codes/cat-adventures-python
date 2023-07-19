# follow the story of Meowshmallow and Peppurrmint!

print(
    """
    Our furry-tail begins in a small village with two curious cats named
    Meowshmallow and Peppurrmint who heard tales of the legendary golden fish.
    This magical fish was said to provide an endless supply of food
    to whomever caught it. Intrigued by the story,
    Meowshmallow and Peppurrmint decide to embark on an adventure
    to find this elusive fish.
    As they set out on their journey, they come across two possible paths:
    """
)

"""
Step 1 options 1 and 2:
Follow the river upstream (go to Step 2)
Venture into the dense forest (go to Step 3)
"""

# Step 2:

print(
    """
    Meowshmallow and Peppurrmint follow the river upstream,
    hoping it would lead them to the golden fish. Along the way,
    they discover a wise old turtle who offers them advice.
    The turtle says to them: 'The golden fish lives in a hidden lake,
    but the path is treacherous. You must choose wisely.'
    """
)

"""
Step 2 options 1 and 2:
Ask the turtle for guidance (go to Step 4)
Continue without the turtle's help (go to Step 5)
"""

# Step 3:

print(
    """
    Meowshmallow and Peppurrmint venture into the dense forest,
    relying on their keen senses to guide them.
    Soon, they stumble upon a chatty squirrel who claims to know
    the whereabouts of the golden fish.
    """
)

"""
Step 3 options 1 and 2:
Trust the squirrel and follow its directions (go to Step 6)
Doubt the squirrel and find their own way (go to Step 7)
"""

# Step 4 with guidance:

print(
    """
    With the turtle's guidance, Meowshmallow and Peppurrmint manage
    to find the hidden lake. As they approache, they notice two different
    spots they could possibly catch the fish from:
    """
)

"""
Step 4 options 1 and 2:
An open spot near the water's edge (go to Step 8)
A secluded spot beneath a willow tree (go to Step 9)
"""

# Step 5 no guidance:

print(
    """
    Meowshmallow and Peppurrmint continue their journey without
    the turtle's help. They soon find a lake that seems promising.
    They notice two different spots they could possibly catch the fish from:
    """
)

"""
Step 5 options 1 and 2:
An open spot near the water's edge (go to Step 10)
A secluded spot beneath a willow tree (go to Step 11)
"""

# Step 6 trusting the squirrel:

print(
    """
    Trusting the squirrel's directions, Meowshmallow and Peppurrmint arrive
    at the hidden lake. Looking around, they see two possible fishing spots:
    """
)

"""
An open spot near the water's edge (go to Step 12)
A secluded spot beneath a willow tree (go to Step 13)
"""

# Step 7 doubting the squirrel:

print(
    """
    Meowshmallow and Peppurrmint decide not to trust the squirrel and forge
    their own path. Eventually, they stumble upon a lake. They notice two
    different spots they could possibly catch the fish from:
    """
)

"""
An open spot near the water's edge (go to Step 14)
A secluded spot beneath a willow tree (go to Step 15)
"""

# Step 8 - Open Spot with Guidance
print(
    """
    Choosing the open spot with the guidance of the turtle, Meowshmallow
    and Peppurrmint catch the golden fish!
    """
)

ENDING_1 = """
Success: Meowshmallow and Peppurrmint return home with the golden fish.
True to the legend, it provides them with an endless supply of food, and they
live happily ever after.
"""
print(ENDING_1)

# Step 9 - Secluded Spot with Guidance
print(
    """
    Choosing the secluded spot, despite the turtle's guidance, leads to no
    sign of the golden fish.
    """
)

ENDING_2 = """
Failure: Despite their best efforts, Meowshmallow and Peppurrmint never find
the golden fish. They return to the farm, but the legend of the golden fish
live on in their hearts.
"""
print(ENDING_2)

# Step 10 - Open Spot without Guidance
print(
    """
    Choosing the open spot without any guidance turned out to be a misstep,
    they find no sign of the golden fish.
    """
)
print(ENDING_2)

# Step 11 - Secluded Spot without Guidance
print(
    """
    Choosing the secluded spot without any guidance turned out to be the right
    choice! They found and caught the golden fish.
    """
)
print(ENDING_1)

# Step 12 - Open Spot with Squirrel's Guidance
print(
    """
    Choosing the open spot with the squirrel's guidance, they caught the
    golden fish!
    """
)
print(ENDING_1)

# Step 13 - Secluded Spot with Squirrel's Guidance
print(
    """
    Choosing the secluded spot, despite the squirrel's guidance, led to no
    sign of the golden fish.
    """
)
print(ENDING_2)

# Step 14 - Open Spot without Squirrel's Guidance
print(
    """
    Choosing the open spot without the squirrel's guidance led to no sign of
    the golden fish.
    """
)
print(ENDING_2)

# Step 15 - Secluded Spot without Squirrel's Guidance
print(
    """
    Choosing the secluded spot without the squirrel's guidance turned out to
    be the right choice! They found and caught the golden fish.
    """
)
print(ENDING_1)
