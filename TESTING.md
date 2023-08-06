# Testing Documentation

## CONTENTS

* [CI Pep8 Validator](#ci-pep8-validator)
* [User Testing](#user-testing)
* [Manual Testing](#manual-testing)

### CI Pep8 Validator

I chose not to include the ASCII art into the linter as that has inconsistencies, but as it has no effect on the game, as well as being within the 80 character length limit I have omitted it from the validator. Otherwise, all comes back fine!

![ci-python-linter](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/42b476bd-eeeb-41e6-9ed1-dd2052b7bb73)


### User Testing

I asked my friends and family on Facebook to try my game and received some points to fix, and good feedback!

![facebook-user-testing](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/2abca620-f339-4d69-8cb2-132e2e044e23)


### Manual testing:

For testing purposes, one of the paths for succeeding is simply by inputting 1 for each option. In order to get to the unsucessful ending, input 1, 1, 2 in that order.

| Feature | Expectation | Testing | Result |
| ------- |:-----------:|:-------:| ------:|
| 1. Run program | Game ASCII, welcome message and input prompt show | Ran program | All showing correctly |
| 1a. Game visual | Text window should look a little more fun than pure text by the use of spacing, positioning, hyphenation and use of $ sign | Checked each flow and added/adjusted as necessary | Looking good after adjustments | 
| 2. Enter no name | Add nothing to name input when prompted, receive an error message | Hit enter instead of writing anything | Received error message and a prompt to input a name again |
| 3. Enter a very long name | Enter a name that is too long to fit the game text and stay below 80 characters and receive an error message | Added a name I had hoped to copy paste but ended up stubbornly typing anyway 😂 | Received error message and prompt to input another name |
| 4. Enter a name correctly | Enter chosen name and it will be printed back to the user along with a message and another input to trigger the start of the game | Input a name when prompted | Name was printed along with a message to start the game |
| 5. Start game (incorrectly) | Typing incorrect input into start game prompt will show a message and prompt the user to try again | Input a word, an input longer than 80 characters, and no input | All return the prompt to input 1 to start the game |
| 6. Start game (correctly) | Input 1 will start the game and print the first of the game texts with a prompt for user input | Input 1 when prompted | Game begins and correctly shows the first text and input option |
| 7. Game input steps | Each step of the game, inputting nothing should prompt the user to try again and provide input box | Hit enter on input box for every step | User is prompted to try again |
| 8. Game input steps incorrectly | Each step of the game, inputting something longer than 80 characters should prompt the user to try again and provide an input box | Entered a long character string on each step | User is prompted to try again |
| 9. Game input steps correctly | Writing 1 or 2 on each step of the game correctly takes the user to the next step of the game which prints a new game message and provides an input box | Try both 1 and 2 on each step to ensure game is following the flow on lucid charts correctly | Inputting 1 or 2 for every step of the game correctly takes the user to the next step |
| 10. Game input steps nothing | Hitting enter without any input will prompt the user to try again | Hit enter on each step of the game through to the end | Input line correctly repeats itsself until correct input is given |
| 11. End game (success) | Winning the game shows the winning message along with a prompt to restart the game or not | Followed the game through to a successful ending | Winning message shows and prompts the user to start the game again if they wish |
| 12. End game (no success) | Not succeeding with the game story shows a different message along with a prompt to restart the game or not | Followed the game through to an unsuccessful ending | Unsucessful message shows 


1: Run program: 

![test1](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/e40a16ae-c5ba-43fe-9d19-26512abb898e)

2,3,4: Enter no name, then a long name, then a correct name:

![test234](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/eba772d3-f071-4805-8854-efbbddafaf11)

5: Start game: 

![test5](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/26c923b5-e7f0-47a0-87c3-d591751b36e3)

6: Start game correctly:

![test6](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/a5e72f19-ee44-4fde-b0c5-a24a9825eb4d)

7,8,9: Input nothing, then a long character string, then the correct input of 1 or 2:

![test789](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/5a7ed353-e188-420e-a89c-721efc3669da)

10: Game input steps nothing:

![test10](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/409e1f38-26a5-4784-9c58-4ac8f226b7cd)

11: End game success:

![test11](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/801c5b50-f3a0-4bcf-b462-33a03f28d252)

12: End game no sucess:

![test12](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/c3825307-f09b-40a4-98d1-944e01d5d528)
