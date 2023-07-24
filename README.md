# The adventures of Meowshmallow and Peppurrmint

![catart](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/810854eb-1641-40e1-a9c4-bec9cb6cbcf2)

Visit the deployed site: https://cat-adventures-05cb08857483.herokuapp.com/

Follow Meowshmallow and Peppurrmint, two inquisitive cats on a quest for the fabled golden fish!

I really wanted to make a text based game for this project, being old enough to hark from the era of text based MUDs and other old geekery. My dream is to make a fully interactive game, with items to pick up and use, and squares that the user can navigate around much like the games of yonder year.

## CONTENTS

* [User Stories](#user-stories)
   * [MVP](#mvp)
   * [Add-ons](#add-ons)

* [Design](#design)
  * [Flowchart](#flowchart)
  * [Features](#features)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Iteration over starting code](#iteration-over-starting-code)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
* [Bug Fixes](#bug-fixes)
  
* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Acknowledgments](#acknowledgments)

- - -

## User Stories

#### MVP

The users should to be able to:

* Start the game when typing "Start".
* Not have to worry about capitalizing or lower case when typing.
* Receive the next part in the story depending on the input choices.
* Reach the end of the game through one of the paths chosen, by either succeeding or failing in the quest.

#### Add-ons

After the essentials are covered I would like the user to be able to:

* Have more options/alternate endings to the game.
* Have in-game items to interact with.
* Print out the choices made onto a Google doc/sheet (so the user can see which choices they took and choose differently next time((but really just to show that I understand how to populate input data to a sheet))).
* Enjoy a more visually exciting experience by adding some styling and imagery/ascii.

- - -

## Design

The design is structural in nature as opposed to visual, as although I know the Python terminal can be style, the time I have to implement this project requires full focus on the functionality only.

### Flowchart

Since the game changes depending on the users' choices, I wanted to lay out the step by step logic needed to reach each ending of the game. Although there are only two outcomes there are multiple ways to get there.

![rsz_11blank_diagram](https://github.com/emmy-codes/python-text-game/assets/70635859/23e3c5e3-951d-4083-af31-c40eeb56e421)

### Features

![game-screenshot](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/3ed5b87f-e8a2-48e8-97e2-2db287d2d230)



- - -

## Technologies Used

### Language Used

Python

### Frameworks, Libraries & Programs Used

[Github](https://github.com/) - For online storage of code and deployment.

[Picresize](https://picresize.com/) - Used to resize images for Readme/Testing docs.

[VS Code](https://code.visualstudio.com/) - For writing my code.

[Heroku](https://dashboard.heroku.com/apps) - For deploying my program.

- - -

## Deployment & Local Development

#### Iteration over starting code

Coming from a background that is more familiar with JavaScript, I found it challenging to try to remember the Python semantics. For my  first function I tried writing some pseudo code purely to see what I wanted my function to do (show text, take input etc). This helped me to visualise what I needed to write:

![pseudo_code_trial](https://github.com/emmy-codes/python-text-game/assets/70635859/07d3ba22-4451-40b9-8b75-8e5dc6c98bec)

I then trialled a short JS array and a function and practiced the difference between hard coding which property will be shown (in this case, game.name is hard coded and thus the result will always show the name property from the array). The second console log is programmatically calling whatever _value_ the property from inside the game array has, and thus is interchangable.

![js-logic](https://github.com/emmy-codes/python-text-game/assets/70635859/5723c4dd-1c9c-4daa-a5de-736e3a3ef72e)

"But this is Python, Emma" I hear you inwardly sigh to yourself. "Get to the point!" So here it is: I _then_ moved on to try and create the basics of the Python function using only string data. Again, assigning the strings is the first step for me to be able to see how to later change them to a more DRY method of function writing, since it is clearer what each part of the code does thanks to the text visualization.

Here is the commit from my trialling the function:

![practice-fn-python](https://github.com/emmy-codes/python-text-game/assets/70635859/0acf0b49-b2b2-4fa1-87b1-dc87483b6d7f)

This process of iteration worked best for my brain to see what steps I need to take, and solidify my understanding of not passing immutable data

### Deployment


### Local Development

#### How to Fork


#### How to Clone


- - -

## Testing

Please refer to [TESTING.md](https://github.com/emmy-codes/cat-adventures-python/blob/main/TESTING.md) file for all testing carried out.

## Bug Fixes

So far the majority of issues in my code have been my not completing the logic adequately. For example, when I created the start_game function I added the usual input requests and set an else to print an error message requesting the user input 1 or 2 to continue, but did not set the game to run again. I solved this by offering the input field again after printing a message to the user.

I had a huge challenge after adding a user input to my game due to having a "game window" with a $ on char 79. I was trying to put together an if statement to cover all name length eventualities without impacting the position of the final game window char. After many, many iterations my first breakthrough was getting the print to show the start of the game screen (game_screen_start) followed by the name that the user input.

![error_solving_progress](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/1cad713f-5609-4eab-8c76-5886fd47e591)

The next iteration turned on its head: I was having too hard of a time removing spaces from the end of the string, so I decided to add space up to 77 characters and added the $ to the beginning and end.

I checked the length of the name input, the length of the game screen start text, and the length of the middle text. I then deducted that length from the allowed length of 77. Or so I thought. Upon printing the alignment was completely off and I had way more white space than intended. To find out what went wrong, I printed the "calculating" variable which was over 100! I then printed "len(name)+len(game_screen_start)+len(middle_text))" and it returned around 53. The issue was _precedence_ . I had set the calculating variable to follow the code literally step by step, which was throwing the result off. 

I solved the issue by adding an extra parentheses around the calculation in order to gather the total length of characters to print, which could then be deducted from the allotted 77 characters.

![error_solving_step_3](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/a527a0a7-9861-435a-b244-42e746a8bf7f)

- - -

## Credits

To my classmate [Ben](https://github.com/caketaster/PP3--CYOA/blob/main/run.py) who shared his code for review on Slack, and upon reading it gave me the idea to use just number 1 or 2 as input to help simplify and speed up my MVP.

### Code Used

ASCII art taken from [ASCII art](https://www.asciiart.eu/animals/cats) but it's unclear who the actual owner is as it's displayed identically on multiple sites. I adjusted it to have two cats for the purpose of my story.

### Content

I have used [OpenAI](https://chat.openai.com/) to create most of the text for me so I can focus my time on practicing with the code. "We" had a little chat and went over some iterations and I'm happy that it was able to work out the structure for continuing the game, and then I was able to build the flow chart and thus work on the code structure from there.

### Acknowledgments

I would like to acknowledge the following people:

* My partner for his extra help looking after our little one so I could focus on getting as much learning in as possible, and for providing his insight into logical thinking and good practices to breaking down a problem into manageable chunks. 🥰

// Keeping the text below until completion to ensure I cover all bases!
## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
