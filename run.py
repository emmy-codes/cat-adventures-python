"""
    The tail of 2 curious kitties on a quest for endless fish
"""

CAT_ASCII = """
                               /^--^\     /^--^\ 
                               \____/     \____/
                              /      \   /      \ 
                             |        | |        |
                              \__  __/   \__  __/
 |^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|^|
 | | | | | | | | | | | | | | | | |\ \| | |/ /| | | | | | | | | | | | | | | | |
 #################################/ /#####\ \#################################
 | | | | | | | | | | | | | | | | |\/| | | |\/| | | | | | | | | | | | | | | | |
 |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
"""

game_text = {
        "step_1": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Our furry-tail begins in a small village with two curious cats named       $
$ Meowshmallow and Peppurrmint who heard tales of a legendary golden fish.   $
$ This magical fish was said to provide an endless supply of food            $
$ to whomever caught it. Intrigued by the story, they decide to embark       $
$ on an adventure to find this elusive fish.                                 $
$ -------------------------------------------------------------------------- $
$ As they set out on their journey, they come across two possible paths:     $
$ Option 1: Do they follow the river upstream?                               $
$ Option 2: Or do they venture into the dense forest?                        $
""",
            "option_1": "step_2",
            "option_2": "step_3",
            "end_game": False
        },
        "step_2": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Meowshmallow and Peppurrmint follow the river upstream,                    $
$ hoping it would lead them to the golden fish. Along the way,               $
$ they discover a wise old turtle who offers them advice.                    $
$ The turtle says to them: 'The golden fish lives in a hidden lake,          $
$ but the path is treacherous. You must choose wisely.'                      $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they ask the turtle for guidance?                             $
$ Option 2: Or do they continue without the turtle's help?                   $
""",
            "option_1": "step_4",
            "option_2": "step_5",
            "end_game": False
        },
        "step_3": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Meowshmallow and Peppurrmint venture into the dense forest,                $
$ relying on their keen senses to guide them.                                $
$ Soon, they stumble upon a chatty squirrel who claims to know               $
$ the whereabouts of the golden fish.                                        $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they trust the squirrel and follow its directions?            $
$ Option 2: Or do they doubt the squirrel and find their own way?            $
""",
            "option_1": "step_6",
            "option_2": "step_7",
            "end_game": False
        },
        "step_4": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ With the turtle's guidance, Meowshmallow and Peppurrmint manage            $
$ to find the hidden lake. As they approache, they notice two different      $
$ spots they could possibly catch the fish from:                             $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they pick the open spot near the water's edge?                $
$ Option 2: Or do they pick the secluded spot beneath the willow tree?       $
""",
            "option_1": "step_8",
            "option_2": "step_9",
            "end_game": False
        },
        "step_5": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Meowshmallow and Peppurrmint continue their journey without                $
$ the turtle's help. They soon find a lake that seems promising.             $
$ They notice two different spots they could possibly catch the fish from:   $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they pick the open spot near the water's edge?                $
$ Option 2: Or do they pick the secluded spot beneath the willow tree?       $
""",
            "option_1": "step_10",
            "option_2": "step_11",
            "end_game": False
        },
        "step_6": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Trusting the squirrel's directions, Meowshmallow and Peppurrmint arrive    $
$ at the hidden lake. Looking around, they see two possible fishing spots:   $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they pick the open spot near the water's edge?                $
$ Option 2: Or do they pick the secluded spot beneath the willow tree?       $
""",
            "option_1": "step_12",
            "option_2": "step_13",
            "end_game": False
        },
        "step_7": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Meowshmallow and Peppurrmint decide not to trust the squirrel and forge    $
$ their own path. Eventually, they stumble upon a lake. They notice two      $
$ different spots they could possibly catch the fish from:                   $
$ -------------------------------------------------------------------------- $
$ Option 1: Do they pick the open spot near the water's edge?                $
$ Option 2: Or do they pick the secluded spot beneath the willow tree?       $
""",
            "option_1": "step_14",
            "option_2": "step_15",
            "end_game": False
        },
        "step_8": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the open spot with the guidance of the turtle,                    $
$ Meowshmallow and Peppurrmint catch the golden fish!                        $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": True
        },
        "step_9": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the secluded spot, despite the turtle's guidance, leads to no     $
$ sign of the golden fish.                                                   $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": False
        },
        "step_10": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the open spot without the turtle's guidance turned out to be a    $
$ misstep, as they find no sign of the golden fish.                          $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": False
        },
        "step_11": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the secluded spot without the turtle's guidance turned out to be  $
$ the right choice! They found and caught the golden fish!                   $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": True
        },
        "step_12": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the open spot with the squirrel's guidance,                       $
$ they caught the golden fish!                                               $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": True
        },
        "step_13": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the secluded spot, despite the squirrel's guidance,               $
$ led to no sign of the golden fish.                                         $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": False
        },
        "step_14": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the open spot without the squirrel's guidance                     $
$ led to no sign of the golden fish.                                         $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": False
        },
        "step_15": {
            "step_text":
                """
$ -------------------------------------------------------------------------- $
$ Choosing the secluded spot without the squirrel's guidance turned out to   $
$ be the right choice! They found and caught the golden fish.                $
$ -------------------------------------------------------------------------- $
""",
            "end_game": True,
            "success": True
        }
    }

# End text for success
ENDING_1 = """
$ -------------------------------------------------------------------------- $
$ Meowshmallow and Peppurrmint return home with the golden fish.             $
$ True to the legend, it provides them with an endless supply of food,       $
$ and they live happily ever after.                                          $
$ -------------------------------------------------------------------------- $
"""
# End text for failure
ENDING_2 = """
$ -------------------------------------------------------------------------- $
$ Despite their best efforts, Meowshmallow and Peppurrmint never find        $
$ the golden fish. They return to the farm, but the legend                   $
$ of the golden fish live on in their hearts.                                $
$ -------------------------------------------------------------------------- $
"""


def get_user_name():
    """
        gets user input username
    """
    name = input("Name: ")
    return name


def preserve_game_screen_size():
    """
        checks the length of the name variable and adjusts
        the game screen length
    """
    game_screen_start = "$ Welcome, "
    name = get_user_name()
    middle_text = ", to the adventures of"
    calculating = 76 - (len(name)+len(game_screen_start)+len(middle_text))
    white_space = [" " for _ in range(calculating)]
    adjust_game_screen_end = "".join(white_space)
    adjust_game_screen_end += " $"
    game_screen_with_name = f"""
{game_screen_start}{name}{middle_text}{adjust_game_screen_end}"""

    if len(name) == 0:
        print("Please tell us your name, brave hero!")
        preserve_game_screen_size()
    elif len(name) <= 32:
        print(f"""
$ -------------------------------------------------------------------------- $
        {game_screen_with_name}
$ Meowshmallow and Peppurrmint,                                              $
$ two very curious cats that are on a mission!                               $
$ -------------------------------------------------------------------------- $
$ Are you ready to start the game?                                           $
$ -------------------------------------------------------------------------- $
""")
    elif len(name) > 32:
        print("""Oh dear, your name seems to be a bit long! Do you have
a shorter nickname you could try?""")
        preserve_game_screen_size()
    return preserve_game_screen_size


def start_game():
    """
        starting the game
    """
    print(CAT_ASCII) # prints cat art to the top of the game screen
    print("""
$ -------------------------------------------------------------------------- $
$ Hello dear cat wrangler, to your feline text adventure!                    $
$ And who might be guiding our furry protagonists on their quest today?      $
$ -------------------------------------------------------------------------- $
""")
    preserve_game_screen_size()
    game_time = input("Type 1 for yes, or 2 for no: ")
    if game_time == "1":
        show_step(game_text["step_1"])
    elif game_time == "2":
        while game_time != "1":
            print("""
$ -------------------------------------------------------------------------- $
$ Are you sure? Let's take the kitties on an adventure!                      $
$ -------------------------------------------------------------------------- $
""")
            game_time = input("Type 1 for yes, or 2 for no: ")
        show_step(game_text["step_1"])
    else:
        print("""
That's not a valid command,
please enter number 1 or 2 to continue""")


def restart_game():
    """
        Regardless of success or failure, offer the user an
        option to restart the game
    """
    restart = input("Would you like to play again? 1 for yes, 2 for no: ")
    if restart == "1":
        start_game()
    elif restart == "2":
        print("Thank mew for playing! =^_^=")


def show_step(step):
    """
        Initial function to show step 1 with options and receive input from
        the user. Depending on the input, there will be different outcomes.
    """
    if step["end_game"]:
        if step["success"]:
            print(step["step_text"], ENDING_1)
            restart_game()
        else:
            print(step["step_text"], ENDING_2)
            restart_game()
        return
    # exit out of the show_step fn

    print(step["step_text"])
    user_input = input("Write your choice (either 1 or 2): ")

    if user_input == "1":
        show_step(game_text[step["option_1"]])
    elif user_input == "2":
        show_step(game_text[step["option_2"]])
    else:
        print("The cats look around, wondering what to do next")


start_game()
