# Quiz Game

This is a simple quiz game built using Python. The game presents multiple-choice questions to the user, evaluates their answers, and keeps track of their score.

## Project Structure

The project consists of the following files:

1. **main.py** - The entry point of the program. It initializes the quiz and runs the game loop.
2. **question_model.py** - Defines the `Question` class used to represent quiz questions.
3. **quiz_brain.py** - Contains the `QuizBrain` class that manages the quiz logic.
4. **data.py** - Stores the quiz questions in a dictionary format.

## How It Works

1. The `data.py` file contains a list of questions and answers.
2. `main.py` reads this data, converts it into `Question` objects, and initializes a `QuizBrain` instance.
3. The game then presents questions to the user and evaluates their answers.
4. The final score is displayed at the end of the quiz.

## Example Output

```
Q.1 Ada Lovelace is often considered the first computer programmer? (True/False) True
You got it right!
The correct answer was: True
Your current score is: 1/1

...

You've completed the quiz!
Your final score was: 7/10
```

## Requirements

- Python 3.x installed

## Future Enhancements

- Add support for multiple question types.
- Fetch questions from an external API.
- Implement a graphical user interface (GUI).

## Manually Updating Questions

For now, questions can be manually replaced using API-generated data from [Trivia Database](https://opentdb.com/).

