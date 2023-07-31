# Testing Documentation

## CONTENTS

* [CI Pep8 Validator](#ci-pep8-validator)
* [Manual Testing](#manual-testing)

### CI Pep8 Validator

Screenshot of validator after final deployment to come.

### Manual testing:

| Feature | Expectation | Testing | Result |
| ------- |:-----------:|:-------:| ------:|
| 1. Run program | Game ASCII, welcome message and input prompt show | Ran program | All showing correctly |
| 2. Enter no name | Add nothing to name input when prompted, receive an error message | Hit enter instead of writing anything | Received error message and a prompt to input a name again |
| 3. Enter a very long name | Enter a name that is too long to fit the game text and stay below 80 characters and receive an error message | Added a name I had hoped to copy paste but ended up stubbornly typing anyway 😂 | Received error message and prompt to input another name |
| 4. Enter a name correctly | Enter chosen name and it will be printed back to the user along with a message and another input to trigger the start of the game | Input a name when prompted | Name was printed along with a message to start the game |



| Story flow | All story steps flow correctly (can get to the end of the game, either succeding or failing, by taking the options available) | I trialled every single option using my flow diagram, checking each option led to the right next step and correctly reached the end of the game by succeeding or failing. | All steps flow as planned |
| Game visual | Text window should look a little more fun than pure text by the use of spacing, positioning, hyphenation and use of $ sign | Checked each flow and added/adjusted as necessary | Looking good after adjustments | 
|  |  |  |  |

1: Run program: 

![test1](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/e40a16ae-c5ba-43fe-9d19-26512abb898e)

2,3,4: Enter no name, then a long name, then a correct name:

![test234](https://github.com/emmy-codes/cat-adventures-python/assets/70635859/eba772d3-f071-4805-8854-efbbddafaf11)

