# The adventures of Meowshmallow and Peppurrmint

![Python-Terminal-by-Code-Institute](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/5b01d5f2-c582-4cb2-a5e3-6edf03325638)


Visit the deployed site: https://cat-adventures-05cb08857483.herokuapp.com/

Follow Meowshmallow and Peppurrmint, two inquisitive cats on a quest for the fabled golden fish!

I really wanted to make a text-based game for this project, being old enough to hark from the era of text-based MUDs and other old geekery. My dream is to make a fully interactive game, with items to pick up and use, and squares that the user can navigate around much like the games of yonder year.

## CONTENTS

* [Happy Path Through Game](#happy-path-through-game)

* [User Stories](#user-stories)
   * [MVP](#mvp)
   * [Add-ons](#add-ons)

* [Design](#design)
  * [Flowchart](#flowchart)
  * [Features](#features)

* [Technologies Used](#technologies-used)
  * [Language Used](#language-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Iteration over starting code](#iteration-over-starting-code)

* [Deployment & Local Development](#deployment--local-development)
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

## Happy Path Through Game

For testing purposes, one of the paths for succeeding is simply by inputting 1 for each option.
To get to the unsuccessful ending, input 1, 1, 2 in that order.

## User Stories

#### MVP

The users should be able to:

* Start the game when typing "Start".
* Not have to worry about capitalizing or lowercase when typing.
* Receive the next part in the story depending on the input choices.
* Reach the end of the game through one of the paths chosen, by either succeeding or failing in the quest.

#### Add-ons

After the essentials are covered I would like the user to be able to:

* Have more options/alternate endings to the game.
* Have in-game items to interact with.
* Print out the choices made onto a Google doc/sheet (so the user can see which choices they took and choose differently next time((but really it would just be to show that I understand how to populate input data to a sheet))).
* Enjoy a more visually exciting experience by adding some styling and imagery/ASCII.

- - -

## Design

The design is structural in nature as opposed to visual, as although I know the Python terminal can be styled, the time I have to implement this project requires full focus on the functionality only.

### Flowchart

Since the game changes depending on the users' choices, I wanted to lay out the step-by-step logic needed to reach each ending of the game. Although there are only two outcomes there are multiple ways to get there.

**Input/step check**

For each step, the user receives a prompt, writes their input, and the input is cross-checked against the code for validation. If the user input is invalid, they are prompted again to input on the same step. Once valid input is received, the user goes on to the next step.

The flow of the game has 8 possible outcomes, 4 successful adventures, and 4 unsuccessful. Below is a basic map of the journey which can be followed to see all alternatives and their outcomes. A link to the Lucidchart can be found [here](https://lucid.app/lucidchart/61e9461d-0d8e-4266-89c2-d76eccc03e25/edit?viewport_loc=-1550%2C-1746%2C2200%2C2270%2C0_0&invitationId=inv_bbcdbbb9-6f50-4cc3-8962-d0253276f94b) The screenshot is below:

![pp3_game_step_flow_3](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/be5ac518-3cec-4104-a6e9-7347905b45e2)

### Features

The user can add a name of their choosing to give them a personalised welcome to the game:

![game screenshot](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/39dfd09b-d13b-4ff4-8320-9aa58cab3630)

The user is then taken through a journey with explanation texts and requests for the user to choose which path they want to take. Choosing different paths can lead to different outcomes.

![game choices](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/358dd113-b1b4-45cc-b483-6e7e4597239d)

At the end of the user's journey, they are presented with a final text depending on their success or not in catching the required object to "win".

At the end of the game, the users are offered to run through the game from the start if they choose.

Not succeeding:

![game not successful](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/a32df8e2-7ff2-40da-99f6-88bb2277aefe)

Succeeding:

![game successful](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/b4e8e1c9-8944-4158-8c20-869d387e0f66)


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

## Iteration over starting code

Coming from a background that is more familiar with JavaScript, I found it challenging to try to remember Python semantics. For my first function, I tried writing some pseudo code purely to see what I wanted my function to do (show text, take input etc). This helped me to visualise what I needed to write:

![pseudo_code_trial](https://github.com/emmy-codes/python-text-game/assets/70635859/07d3ba22-4451-40b9-8b75-8e5dc6c98bec)

I then trialled a short JS array and a function and practised the difference between hard coding which property will be shown (in this case, game.name is hard-coded and thus the result will always show the name property from the array). The second console log is programmatically calling whatever _value_ the property from inside the game array has and thus is interchangeable.

![js-logic](https://github.com/emmy-codes/python-text-game/assets/70635859/5723c4dd-1c9c-4daa-a5de-736e3a3ef72e)

"But this is Python, Emma" I hear you inwardly sigh to yourself. "Get to the point!" So here it is: I _then_ moved on to try and create the basics of the Python function using only string data. Again, assigning the strings is the first step for me to be able to see how to later change them to a more DRY method of function writing since it is clearer what each part of the code does thanks to the text visualization.

Here is the commit from my trialling of the function:

![practice-fn-python](https://github.com/emmy-codes/python-text-game/assets/70635859/0acf0b49-b2b2-4fa1-87b1-dc87483b6d7f)

This process of iteration worked best for my brain to see what steps I need to take and solidify my understanding of not passing immutable data


- - -

## Deployment & Local Development

### Deployment

This project was deployed at [Heroku](https://heroku.com/)

The numbers on the screenshots represent the numbers on the steps of my deployment process.

To deploy this project after creating my account, I:

1. Went to my dashboard and clicked on the New App dropdown menu
2. Clicked Create new app from the options

![heroku_deployment_step_1-2](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/f5810840-3399-48aa-8944-384850e2f6d9)

3. Named my app in the App name box
4. Chose a region from the dropdown menu (and accidentally chose the United States for this one)
5. Clicked Create app

![heroku_deployment_step_2-5](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/be20a348-416c-446c-8876-2a33ccb883bb)

Once the app was made I went to my dashboard where I can see my apps. 

6. Clicked on the relevant app

![heroku_deployment_step_6](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/ebe871b8-64df-4c9d-b99a-70055232481b)

7-8. From here, I went to settings, then to the Config Vars. I added the PORT key and a value of 8000. This was a requirement by Code Institute to ensure there were no issues caused by _not_ having it.

9. I then went to Buildpacks and added Python, and then NodeJS.

![heroku_deployment_step_7-9](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/239b3b7c-432c-4f16-8437-ef5965079b3e)

10. Then I clicked the Deploy tab. Here I connected my GitHub account with the repository the deployment is to select.
11. After that, I chose to manually deploy my project as needed, but it's possible to set up automatic deployments if preferred.

![heroku_deployment_step_10-11](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/4632f3e9-ed0a-428b-aee0-b7c1f42eef55)



### Local Development

#### How to Fork

Should you wish to fork this repo, here is a guide on how to do that:

Firstly, go to https://github.com/emmy-codes/cat-adventures-python

1. On the main repo page, click the Fork button near the top right corner

![fork-cat-adventures](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/de5cbb89-8713-4b0d-b8d5-4a03c788a41e)

2. On the create a fork page, check the Owner of the repo is set to the GitHub org you wish to use, and change the name of the repo if you wish.
2a: Add a description if you want to
3. Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default)
4. Create the fork

* Screenshot from an old project as I cannot fork my Python project due to not having any organizations connected to my account, and presumably because this repo is already a fork of the CI template

![fork-screenshot](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/5980e69e-843a-4f08-ba14-e9c250838d58)


#### How to Clone

For cloning the repo you will need:

* The [repo](https://github.com/emmy-codes/cat-adventures-python) open
* Your IDE of choice

1. On the repo page, click on the green "Code" button
2. On the dropdown from the Code button, click on your chosen key (pictured here is SSH)
3. Click the copy button (shown as two squares on top of one another)

![clone_step](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/0b2408dd-1228-4d23-94c7-167328ec5e9d)

4. Open your IDE of choice and open the Terminal, or in my case, open the Terminal on your computer (I run Linux on Windows so may be slightly different for Mac/Windows users)
5. Check that you're in the right folder (shown here by checking my current folder by using the input: ls
6. Change as needed to reach your desired folder.
7. Type (without quotation marks): "git clone" followed by your copied link from GitHub.
8. You can now access the repo in your IDE if cloned directly there, or by typing (without quotation marks) "code ." in your Terminal.
9. Have fun!

![git_clone_pp3](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/0fc252e4-5983-4c39-9aef-902d12f25c88)


- - -

## Testing

Please refer to the [TESTING.md](https://github.com/emmy-codes/cat-adventures-python/blob/main/TESTING.md) file for all testing carried out.

## Bug Fixes

The majority of the issues in my code have been due to my not completing the logic adequately. For example, when I created the start_game function I added the usual input requests and set an else to print an error message requesting the user input 1 or 2 to continue, but did not set the game to run again. I solved this by offering the input field again after printing a message to the user.

I had a huge challenge after adding user input to my game due to having a "game window" with a $ on char 79. I was trying to put together an if statement to cover all name-length eventualities without impacting the position of the final game window char. After many, many iterations my first breakthrough was getting the print to show the start of the game screen (game_screen_start) followed by the name that the user input.

![error_solving_progress](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/1cad713f-5609-4eab-8c76-5886fd47e591)

The next iteration turned on its head: I was having too hard of a time removing spaces from the end of the string, so I decided to add space up to 77 characters and added the $ to the beginning and end.

I checked the length of the name input, the length of the game screen start text, and the length of the middle text. I then deducted that length from the allowed length of 77. Or so I thought. Upon printing the alignment was completely off and I had way more white space than intended. To find out what went wrong, I printed the "calculating" variable which was over 100! I then printed "len(name)+len(game_screen_start)+len(middle_text))" and it returned around 53. The issue was _precedence_ . I had set the calculating variable to follow the code step by step, which was throwing the result off. 

I solved the issue by adding extra parentheses around the calculation to gather the total length of characters to print, which could then be deducted from the allotted 77 characters.

![error_solving_step_3](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/a527a0a7-9861-435a-b244-42e746a8bf7f)

- - -

## Credits

To my classmate [Ben](https://github.com/caketaster/PP3--CYOA/blob/main/run.py) who shared his code for review on Slack, and upon reading it gave me the idea to use just number 1 or 2 as input to help simplify and speed up my MVP.

### Code Used

ASCII art is taken from [ASCII art](https://www.asciiart.eu/animals/cats) but it's unclear who the actual owner is as it's displayed identically on multiple sites. I adjusted it to have two cats for the purpose of my story.

### Content

I have used [OpenAI](https://chat.openai.com/) to create most of the text for me so I can focus my time on practising with the code. "We" had a little chat and went over some iterations and I'm happy that it was able to work out the structure for continuing the game, and then I was able to build the flow chart and thus work on the code structure from there.

### Acknowledgments

I would like to acknowledge the following people:

* My partner for his extra help looking after our little one so I could focus on getting as much learning in as possible, and for providing his insight into logical thinking and good practices for breaking down a problem into manageable chunks. 🥰

* Family and friends on Facebook for user testing my game and providing feedback!
