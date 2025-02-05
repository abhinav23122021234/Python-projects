# Coffee Machine Project

## Overview
This is a Python-based **Coffee Machine Simulator** that mimics the functionality of a real-world coffee machine. The program allows users to select from a menu of drinks, processes payments, checks for ingredient sufficiency, and dispenses coffee if all conditions are met. It follows **Object-Oriented Programming (OOP)** principles, making it modular and scalable.

## Features
✅ Supports three drink options: **Latte, Espresso, and Cappuccino** ☕
✅ Maintains an ingredient inventory (water, milk, coffee)
✅ Handles transactions using a virtual money system
✅ Provides an option to check the machine’s report (ingredient levels & earnings)
✅ Allows the user to **turn off** the machine
✅ Checks for sufficient ingredients before preparing a drink
✅ Processes coin-based payments and gives change if applicable
✅ Refunds money if payment is insufficient

## Project Structure
The project consists of **four Python files**, each handling a separate aspect of the coffee machine:

### 1️⃣ **main.py** (Driver Code)
- Runs the coffee machine loop.
- Takes user input for drink selection.
- Calls the necessary methods from other classes to process orders, check ingredients, and handle payments.

### 2️⃣ **menu.py** (Handles Menu Items)
- Stores available drinks and their ingredients.
- Provides options to retrieve drink names.
- Searches for a drink in the menu.

### 3️⃣ **coffee_maker.py** (Manages Ingredients)
- Tracks available resources (water, milk, coffee).
- Checks if ingredients are sufficient for a selected drink.
- Deducts ingredients when a coffee is made.

### 4️⃣ **money_machine.py** (Handles Transactions)
- Simulates a payment system using coin denominations.
- Calculates and validates payments.
- Issues change and refunds if needed.
- Tracks the total money earned by the machine.

## How It Works
1️⃣ The user selects a drink from the menu.

2️⃣ The machine checks if enough ingredients are available.

3️⃣ If sufficient, the user inserts coins for payment.

4️⃣ The machine processes the payment:
   - If the payment is sufficient, the drink is prepared and served. ☕
   - If insufficient, the money is refunded.
   - 
5️⃣ The user can type **'report'** to view ingredient levels and total earnings.

6️⃣ Typing **'off'** turns off the machine.

## Technologies Used
- **Python** (Object-Oriented Programming)
- **Class & Object Implementation**
- **Dictionary-based Data Storage**

## How to Run the Project
1️⃣ Clone or download the repository.

2️⃣ Ensure Python is installed on your system.

3️⃣ Run `python main.py` in the terminal.

4️⃣ Follow on-screen instructions to interact with the coffee machine.

## Future Enhancements
🔹 Add more coffee options ☕

🔹 Implement a GUI using Tkinter or PyQt 🎨

🔹 Integrate an API for a real payment system 💳

Enjoy your **virtual coffee experience!** 🚀

