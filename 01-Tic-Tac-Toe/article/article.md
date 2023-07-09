# Learning Python by Creating Games

**Learning Python by Creating Games** is a hands-on article series designed to make your coding journey both fun and productive. Through building engaging games, you'll master Python and key programming concepts, laying a strong foundation for your future coding projects. You won't just learn - you'll create, bringing ideas to life one line of code at a time. Get ready to dive into Python, craft your own games, and unlock new programming skills!

**Keep an eye open for extra details:** <details><summary> I am an extra details section - Click me ! 
</summary>
Extra detail sections are here to deliver extra content that you might already know (beginner level) or that you don't need in order to understand the main content, but deepens it.  
</details>

**Resources:**
- Code on Github (coming soon)
- Jupyter Notebooks with exercises (coming soon)
- Youtube video (coming soon)

# Lesson #01 - Tic Tac Toe 
In this first article of our series, we're taking on the challenge of creating a classic - Tic Tac Toe! Here's what we'll be doing: 

- Setting up a Virtual Environment
- Learning about variables and types.
- Using Python's input and output functions.
- Building a game board with lists.
- Controlling game flow with loops and conditionals.
- Organizing code with functions.
- Handling errors.
- End Result == A Functioning Tic Tac Toe game.

## Table of Contents

- **1 Setting up a Virtual Environment**
  - **1.1** How to create a virtual environment
- **2 Game Basics: Player Names & Symbols**
  - **2.1** Understanding variables: storing our players' information.
  - **2.2** Exploring Python's data types: dealing with strings and characters.
  - **2.3** Exercise: Create variables for player names and symbols (X, O).
- **3 Interacting with Players: Input and Output**
  - **3.1** Introducing output with the print function: communicating with players.
  - **3.2** Gathering input using the input function: interacting with players.
  - **3.3** Exercise: Ask for players' names and greet them.
- **Crafting the Game Board: Working with Lists**
  - **3.4** Unpacking lists: the building blocks of our game board.
  - **3.5** Exercise: Create a list to represent the Tic Tac Toe game board.
  - **3.6** Visualizing the Game Board: Looping Concepts
- **4 The power of loops: repeating actions with for and while loops.**
  - Exercise: Create a loop to display the game board.
  - Making Moves: Control Flow
- **Control flow: directing the game's progression with conditionals.**
  - Exercise: Check if a player's move is valid and if they've won.
- **Streamlining the Process: Functions**
  - Learning about functions: simplifying our code and avoiding repetition.
  - Exercise: Break down the game logic into manageable functions.
- **Catching Mistakes: Error Handling**
  - Handling errors: making our game foolproof with try and except statements.
  - Exercise: Improve the game's user experience by handling invalid inputs.
- **Assembling the Game: Applying What We've Learned**
  - Review and apply all concepts learned to complete our Tic Tac Toe game.
- **Bonus Round: AI Concepts (Optional)**
  - Introduction to basic AI concepts: understanding how AI could play Tic Tac Toe.
  - Exercise: Spice up the game by implementing a basic AI opponent.

## 1 Environment Setup


Before we start coding, we'll create a Python virtual environment for our project. A virtual environment is an isolated space where Python can run, keeping any dependencies you install separate from other projects. This is best practice & essential for avoiding package conflicts between projects.

### 1.1 How to create a virtual environment
Here are the quick steps to set one up:

 - Open your terminal or command prompt.
Navigate to your desired project directory using `cd path_to_your_directory`.
 - Create the virtual environment using `python3 -m venv .venv`, where `.venv` is your chosen environment name.
 - Activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Unix or MacOS.
  
You should in your terminal now see `.venv`  at the beginning of your command line. This means that your virtual environment is active.

![venv activated in Terminal](https://raw.githubusercontent.com/RMagician/LearnPythonGames/master/01-Tic-Tac-Toe/article/images/i1_venv_activation.png)

</details>

## Game Basics: Player Names & Symbols

Now that we've set up our Python environment, let's dive into the first step of creating our Tic Tac Toe game. The game is usually played between two players, so we'll need to store some information about them - their names and chosen symbols (X or O). This is where variables come into play in Python.  
<br>

<details><summary> What is a Variable</summary>

A variable in Python is like a container that holds a value. You can think of it as a box that stores something for us. We can give this box a name, and then Python will remember what we put in it, ready for when we need to use it later. To create a variable, we just need to pick a name for it and then use the equals sign (=) to assign it a value.

For instance, if we want to create a variable named player1, we could do so like this:

```
player1 = "Alice"
```
In this example, player1 is our variable, and "Alice" is the value we've stored in it.  
</details>

<details><summary>What are Variable Types</summary>
Exploring Python's Data Types

In Python, we have different types of data that we can work with. For our game, we're going to focus on strings. A string is a sequence of characters and is created by placing the characters between quotation marks. In the player1 example above, "Alice" is a string.

We also use strings to represent our player's symbols. In Tic Tac Toe, the two symbols used are "X" and "O".
</details><br>



let's create these variables:

```
player1_name = "Alice"
player1_symbol = "X"

player2_name = "Bob"
player2_symbol = "O"
```
You can follow along in the jupyter notebook provided, or in your own environment ! 