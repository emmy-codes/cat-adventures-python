# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Step 1.

print(
    "Once upon a time, in a small village, two curious cats named Peppurrmint and Meowshmallow heard tales of the legendary golden fish. This magical fish was said to provide an endless supply of food to whoever caught it.\n Intrigued by the story, Whiskers and Paws decided to embark on an adventure to find this elusive fish.\n As they set out on their journey, they came across two possible paths:"
)

""" Step 1 options 1 and 2:
Follow the river upstream (go to Step 2)
Venture into the dense forest (go to Step 3) """

# Step 2:

print(
    "Meowshmallow and Peppurrmint followed the river upstream, hoping it would lead them to the golden fish.\n Along the way, they discovered a wise old turtle who offered them advice. The turtle said, 'The golden fish lives in a hidden lake, but the path is treacherous. You must choose wisely.'"
)

""" Step 2 options 1 and 2:
Ask the turtle for guidance (go to Step 4)
Continue without the turtle's help (go to Step 5) """

# Step 3:

print(
    "Meowshmallow and Peppurrmint ventured into the dense forest, relying on their keen senses to guide them.\n Soon, they stumbled upon a chatty squirrel who claimed to know the whereabouts of the golden fish."
)

""" Step 3 options 1 and 2:
Trust the squirrel and follow its directions (go to Step 6)
Doubt the squirrel and find their own way (go to Step 7) """

# Step 4 with guidance:

print(
    "With the turtle's guidance, Meowshmallow and Peppurrmint managed to find the hidden lake.\n As they approached, they noticed two different spots they could possibly catch the fish from:"
)

""" Step 4 options 1 and 2:
An open spot near the water's edge (go to Step 8)
A secluded spot beneath a willow tree (go to Step 9) """

# Step 5 no guidance:

print(
    "Meowshmallow and Peppurrmint continued their journey without the turtle's help.\n They soon found a lake that seemed promising. They noticed two different spots they could possibly catch the fish from:"
)

""" Step 5 options 1 and 2:
An open spot near the water's edge (go to Step 10)
A secluded spot beneath a willow tree (go to Step 11) """

# Step 6 trusting the squirrel:

print(
    "Trusting the squirrel's directions, Meowshmallow and Peppurrmint arrived at the hidden lake.\n Looking around, they spotted two possible fishing spots:"
)

""" An open spot near the water's edge (go to Step 12)
A secluded spot beneath a willow tree (go to Step 13) """

# Step 7 doubting the squirrel:

print(
    "Meowshmallow and Peppurrmint decided not to trust the squirrel and forged their own path.\n Eventually, they stumbled upon a lake. They noticed two different spots they could possibly catch the fish from:"
)

""" An open spot near the water's edge (go to Step 14)
A secluded spot beneath a willow tree (go to Step 15) """

# Step 8 - Open Spot with Guidance
print(
    "Choosing the open spot with the guidance of the turtle, Meowshmallow and Peppurrmint caught the golden fish!"
)

ending_1 = "Success: Meowshmallow and Peppurrmint returned home with the golden fish. True to the legend, it provided them with an endless supply of food, and they lived happily ever after."
print(ending_1)
# Step 9 - Secluded Spot with Guidance
print(
    "Choosing the secluded spot, despite the turtle's guidance, led to no sign of the golden fish."
)

ending_2 = "Failure: Despite their best efforts, Meowshmallow and Peppurrmint never found the golden fish. They returned to the farm, but the legend of the golden fish lived on in their hearts."
print(ending_2)
# Step 10 - Open Spot without Guidance
print(
    "Choosing the open spot without any guidance turned out to be a misstep, they found no sign of the golden fish."
)
print(ending_2)
# Step 11 - Secluded Spot without Guidance
print(
    "Choosing the secluded spot without any guidance turned out to be the right choice! They found and caught the golden fish."
)
print(ending_1)
# Step 12 - Open Spot with Squirrel's Guidance
print(
    "Choosing the open spot with the squirrel's guidance, they caught the golden fish!"
)
print(ending_1)
# Step 13 - Secluded Spot with Squirrel's Guidance
print(
    "Choosing the secluded spot, despite the squirrel's guidance, led to no sign of the golden fish."
)
print(ending_2)
# Step 14 - Open Spot without Squirrel's Guidance
print(
    "Choosing the open spot without the squirrel's guidance led to no sign of the golden fish."
)
print(ending_2)
# Step 15 - Secluded Spot without Squirrel's Guidance
print(
    "Choosing the secluded spot without the squirrel's guidance turned out to be the right choice! They found and caught the golden fish."
)
print(ending_1)
