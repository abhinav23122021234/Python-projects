# Blackjack Project

## Overview
This is a simple Blackjack game implemented in Python. The game allows a user to play against the computer with standard Blackjack rules. The project consists of two files:

1. `art.py` - Contains the ASCII logo for the game.
2. `main.py` - The main game logic.

## How to Play
- The player is asked if they want to play a game of Blackjack.
- Each player (the user and the computer) is dealt two random cards.
- The player can choose to draw more cards or pass.
- The computer will keep drawing cards until its total sum is at least 16.
- The game evaluates the final scores and determines the winner.

## Game Rules
- The game follows standard Blackjack rules.
- Aces (`11`) are converted to `1` if the total sum exceeds `21`.
- If the player's total exceeds `21`, they lose immediately.
- If the computer's total exceeds `21`, the player wins.
- The highest score under `21` wins the game.

## Files in the Project
### `art.py`
Contains the ASCII art logo used in the game:
```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
```

### `blackjack.py`
Contains the complete game logic, including:
- Card dealing
- Score calculation
- Winner evaluation
- Recursive game restart functionality

## How to Run
1. Clone this repository or download the files.
2. Ensure you have Python installed.
3. Run the game using the following command:
   ```sh
   python blackjack.py
   ```
4. Follow the on-screen prompts to play the game.

## Dependencies
This project only requires Python's built-in libraries (`random` for card selection).

## Author
Created by Abhinav Sharma

