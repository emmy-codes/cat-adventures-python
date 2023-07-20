# The adventures of Meowshmallow and Peppurrmint

Visit the deployed site: https://cat-adventures-05cb08857483.herokuapp.com/

Follow Meowshmallow and Peppurrmint, two inquisitive cats on a quest for the fabled golden fish!

I really wanted to make a text based game for this project, being old enough to hark from the era of text based MUDs and other old geekery. My dream is to make a fully interactive game, with items to pick up and use, and squares that the user can navigate around much like the games of yonder year.

## CONTENTS

* [User Stories](#user-stories)
   * [MVP](#mvp)
   * [Add-ons](#add-ons)

* [Design](#design)
  * [Flowchart](#flowchart)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)
  
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

- - -

## Technologies Used

### Languages Used

Python

### Frameworks, Libraries & Programs Used


- - -

## Deployment & Local Development

### Deployment


### Local Development

#### How to Fork


#### How to Clone


- - -

## Testing

Please refer to [TESTING.md]() file for all testing carried out.

- - -

## Credits

To my classmate [Ben](https://github.com/caketaster/PP3--CYOA/blob/main/run.py) who shared his code for review on Slack, and upon reading it gave me the idea to use just number 1 or 2 as input to help simplify and speed up my MVP.

### Code Used

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
