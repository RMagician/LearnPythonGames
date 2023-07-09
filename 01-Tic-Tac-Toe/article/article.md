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

# Table of Contents

- [Learning Python by Creating Games](#learning-python-by-creating-games)
- [Lesson #01 - Tic Tac Toe](#lesson-01---tic-tac-toe)
- [Table of Contents](#table-of-contents)
- [Part 1: Laying the Groundwork](#part-1-laying-the-groundwork)
  - [1.1 Setting up a Virtual Environment](#11-setting-up-a-virtual-environment)
    - [1.1.1 How to create a virtual environment](#111-how-to-create-a-virtual-environment)
  - [1.2 Game Basics - Player Names \& Symbols](#12-game-basics---player-names--symbols)
    - [1.2.1 What are variables \& how to use them](#121-what-are-variables--how-to-use-them)
    - [1.2.2 Creating some variables for our game](#122-creating-some-variables-for-our-game)
  - [1.3 Interacting with Players - Input \& Output](#13-interacting-with-players---input--output)
    - [1.3.1 Print \& Input Functions Explained](#131-print--input-functions-explained)
    - [1.3.2 Print \& Input in Action](#132-print--input-in-action)
  - [1.4 Crafting the Game Board](#14-crafting-the-game-board)
    - [1.4.1 What are Lists.](#141-what-are-lists)
    - [1.4.2 Multi-dimensional lists.](#142-multi-dimensional-lists)
    - [1.4.3 Building the Game Board](#143-building-the-game-board)
  - [1.5 The Code so far](#15-the-code-so-far)
- [Part 2: The Game Logic](#part-2-the-game-logic)
  - [2.1 Visualizing the Game Board: Looping Concepts](#21-visualizing-the-game-board-looping-concepts)
    - [2.1.1 The Power of Loops: For \& While](#211-the-power-of-loops-for--while)
    - [2.1.2 Displaying the Game Board](#212-displaying-the-game-board)
  - [2.2 Making Moves: Control Flow](#22-making-moves-control-flow)
    - [2.2.1 Control flow: directing the game's progression with conditionals.](#221-control-flow-directing-the-games-progression-with-conditionals)
    - [2.2.2 Exercise: Check if a player's move is valid and if they've won.](#222-exercise-check-if-a-players-move-is-valid-and-if-theyve-won)
  - [2.3 Streamlining the Process: Functions](#23-streamlining-the-process-functions)
    - [2.3.1 Learning about functions: simplifying our code and avoiding repetition.](#231-learning-about-functions-simplifying-our-code-and-avoiding-repetition)
    - [2.3.2 Exercise: Break down the game logic into manageable functions.](#232-exercise-break-down-the-game-logic-into-manageable-functions)
  - [2.4 Catching Mistakes: Error Handling](#24-catching-mistakes-error-handling)
    - [2.4.1 Handling errors: making our game foolproof with try and except statements.](#241-handling-errors-making-our-game-foolproof-with-try-and-except-statements)
    - [2.4.2 Exercise: Improve the game's user experience by handling invalid inputs.](#242-exercise-improve-the-games-user-experience-by-handling-invalid-inputs)
- [Part 3: Assembling the Game](#part-3-assembling-the-game)
  - [3.1 Applying What We've Learned](#31-applying-what-weve-learned)
    - [3.1.1 Review and apply all concepts learned to complete our Tic Tac Toe game.](#311-review-and-apply-all-concepts-learned-to-complete-our-tic-tac-toe-game)
  - [3.2 Bonus Round: AI Concepts (Optional)](#32-bonus-round-ai-concepts-optional)
    - [3.2.1 Introduction to basic AI concepts: understanding how AI could play Tic Tac Toe.](#321-introduction-to-basic-ai-concepts-understanding-how-ai-could-play-tic-tac-toe)
    - [3.2.2 Exercise: Spice up the game by implementing a basic AI opponent.](#322-exercise-spice-up-the-game-by-implementing-a-basic-ai-opponent)

# Part 1: Laying the Groundwork
----------- WRITE SOMETHING FOR ME ======================
## 1.1 Setting up a Virtual Environment


Before we start coding, we'll create a Python virtual environment for our project. A virtual environment is an isolated space where Python can run, keeping any dependencies you install separate from other projects. This is best practice & essential for avoiding package conflicts between projects.

### 1.1.1 How to create a virtual environment
Here are the quick steps to set one up:

 - Open your terminal or command prompt.
Navigate to your desired project directory using `cd path_to_your_directory`.
 - Create the virtual environment using `python3 -m venv .venv`, where `.venv` is your chosen environment name.
 - Activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Unix or MacOS.
  
You should in your terminal now see `.venv`  at the beginning of your command line. This means that your virtual environment is active.

![venv activated in Terminal](https://raw.githubusercontent.com/RMagician/LearnPythonGames/master/01-Tic-Tac-Toe/article/images/i1_venv_activation.png)

## 1.2 Game Basics - Player Names & Symbols
Now that we've set up our Python environment, let's dive into the first step of creating our Tic Tac Toe game. The game is usually played between two players, so we'll need to store some information about them - their names and chosen symbols (X or O).
### 1.2.1 What are variables & how to use them
In the context of programming, a variable is a symbolic name for a chunk of data that the programmer can manipulate. The variable is assigned a specific value, and this value can be changed over the course of the program execution. Variables can be used for various purposes like to hold user inputs, results of calculations, or as control flags for loops and conditionals.

**Example:**
```
player1_name = "David"
player1_symbol = "X"
```

<details><summary>The different Variable types</summary>
In Python, variables aren't just limited to storing single values like numbers or strings. They can contain different types of data, each with its unique characteristics.  

**Integers:** 
- These are whole numbers, without a decimal point. They can be of any length, and can be positive, negative, or zero.
- `my_number: int = 5`

**Floats:** 
- These are real numbers with a floating decimal point. They can also be scientific numbers with an "e" to indicate the power of 10.
- `my_float: float = 5.0`

**Strings:** 
- Strings are sequences of characters, typically used to represent words or text. They are created by enclosing characters in quotes.
- `my_string: str = "Hello World"`

**Booleans:** 
- These represent one of two values: True or False. In Python, booleans are generally produced by a comparison operation.
- `my_bool: bool = True`

**Lists:** 
- Lists are ordered sequences of items. The items can be of different data types, and you can change, add, or remove items after the list creation.
- `my_list: list[int] = [1, 2, 3, 4, 5]`

**Tuples:** 
- Tuples are similar to lists, but unlike lists, tuples are immutable. This means that you can't change elements of a tuple once it's been assigned.
- `my_tuple: tuple = (1, 2, 3, 4, 5)`

**Dictionaries:** 
- Dictionaries are unordered collections of data in a key:value pair form. They are used when we have a set of unique keys that map to values.
- `my_dict: dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}`

**Sets:** 
- Sets are unordered collections of unique elements. They are beneficial when we want to eliminate duplicate values.
- `my_set: set = {1, 2, 3, 4, 5}`

Remember, Python is dynamically-typed, which means that you don't need to declare the type of a variable when you create one. Python automatically determines the data type based on the value you assign.
</details>


### 1.2.2 Creating some variables for our game
Here, we're setting up some variables for our Tic Tac Toe game. 
```python
player1_name: str = "David"
player1_symbol: str = "X"

player2_name: str = "Vicky"
player2_symbol: str = "O"
```
This sets up the names and symbols for two players. `player1_name` is set to `"David"`, and `player1_symbol` is set to `"X"`. Likewise, `player2_name` is `"Vicky"` and `player2_symbol` is `"O"`. The `: str` part tells us that these variables are supposed to hold strings (sequences of characters).

Next, we define the game board:
```python
game_board = [
  [" ", " ", " "],
  [" ", " ", " "],
  [" ", " ", " "]
]
```
This is a list of lists - essentially a grid. Each inner list represents a row on the game board, and each space inside those lists represents a cell on that row. We start with all cells being `" "`, which represents an empty cell. As the game progresses, these will be filled with `"X"` or `"O"`, depending on the players' moves.

## 1.3 Interacting with Players - Input & Output
In this section, we'll look at how we can make our game interactive by using Python's built-in functions to communicate with our players.

### 1.3.1 Print & Input Functions Explained
Python has several built-in functions that we can use to interact with users. Two of the most essential are print and input.

The print function is used to output information to the user. We can use it to display messages, such as instructions or status updates.

On the other hand, the input function is used to get information from the user. This function prompts the user for input, waits for them to type something, and then returns what they typed as a string.

These two functions form the basis of Python's input/output (I/O) capabilities, and they'll be instrumental in making our game interactive.

### 1.3.2 Print & Input in Action
Now that we understand what the print and input functions do, let's use them in our game. We'll use input to ask the players for their names and print to display a personalized greeting for each player.

Here's a simple example of how we might do this:


```python
player1_name = input("Please enter your name, Player 1: ")
print(f"Welcome {player1_name}! You'll be playing as 'X'.")

player2_name = input("Please enter your name, Player 2: ")
print(f"Welcome {player2_name}! You'll be playing as 'O'.")
```
In this example, we first use the input function to prompt Player 1 for their name. Whatever they type is then stored in the player1_name variable. We then use the print function to display a personalized welcome message for Player 1, informing them that they'll be playing as 'X'.

We do the same thing for Player 2, except that they'll be playing as 'O'.

## 1.4 Crafting the Game Board
This section focuses on creating our Tic Tac Toe game board. We'll explore Python lists, learn about multi-dimensional lists, and use them to build our 3x3 game grid.
### 1.4.1 What are Lists.
Lists are a core part of Python programming. They are used to store an ordered collection of items, which can be of any type and are mutable, i.e., they can be modified after they're created.

A simple list looks like this:
```python
simple_list = ["apple", "banana", "cherry"]
```

### 1.4.2 Multi-dimensional lists.
For our game board, we need a grid-like structure. That's where multi-dimensional lists come into play. These are lists that have lists as their elements. They are also often known as nested lists.
```python
multi_list = [
  ["a", "b", "c"], 
  ["d", "e", "f"], 
  ["g", "h", "i"]
]
```
### 1.4.3 Building the Game Board
Let's apply this to our Tic Tac Toe game. We need a 3x3 grid, and each cell should start as an empty space (`"-"`) since the game starts with an empty board.

Here's what our game board would look like as a multi-dimensional list:
```python
game_board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]
```
This creates a list called game_board, where each sub-list is a row on the game board, and each dash (`"-"`) in those lists represents an empty cell on that row.

## 1.5 The Code so far
Seems like we've done quite a bit so far right ? Let's look at the code.
```python
player1_symbol: str = "X"
player2_symbol: str = "O"

player1_name = input("Please enter your name, Player 1: ")
print(f"Welcome {player1_name}! You'll be playing as 'X'.")

player2_name = input("Please enter your name, Player 2: ")
print(f"Welcome {player2_name}! You'll be playing as 'O'.")

game_board: list = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
```
This is where we are at. It's a good start, we've set up the players and the game board. Lots to go, let's continue ! 
# Part 2: The Game Logic
In this section, we will delve into the underlying mechanics of our Tic Tac Toe game. This encompasses how the game responds to player actions, how the board is updated, and the rules governing the gameplay.
## 2.1 Visualizing the Game Board: Looping Concepts
One of the first steps in bringing our game to life is being able to visualize the game board. We accomplish this using loops, powerful programming constructs that allow us to perform repetitive tasks efficiently.

### 2.1.1 The Power of Loops: For & While
Python provides two types of loops - 'for' and 'while'. 'For' loops are used for iterating over a sequence (like a list or string) or performing an action a specific number of times. On the other hand, 'while' loops continuously execute a block of code as long as a given condition is true.

<details>
<summary>
Need further explanation on For & While loops ? Click Me !
</summary>

**For Loops**  

A 'for' loop in Python is used to iterate over a sequence such as a list, tuple, string, or other iterable objects. Iterating over a sequence is called traversal. The 'for' loop has a straightforward syntax:

```python
for value in sequence:
    # do something with value
```
In this structure, value is the variable that takes the value of the item inside the sequence on each iteration. The 'for' loop continues until it has gone through all items in the sequence. Here's a simple example:

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```
In this example, the 'for' loop will print each fruit in the list, iterating from the beginning to the end of the list.

**While Loops**

While loops, on the other hand, are used for repeated execution as long as an expression is true. This is known as loop iteration. The syntax for a 'while' loop is:

```python
while expression:
    # do something
```
In this structure, expression is a condition that the 'while' loop checks before each iteration. If the condition is true, the loop's body is executed. If it becomes false, the loop stops, and the control moves to the next statement after the 'while' loop. Here's a basic example:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # equivalent to count = count + 1
```
In this example, the 'while' loop will continue printing the value of count and incrementing it by 1 as long as count is less than 5. Once count reaches 5, the condition becomes false, and the loop stops.

It's important to manage the condition in a 'while' loop carefully because if the condition never becomes false, the 'while' loop will continue indefinitely, creating an infinite loop.

Both 'for' and 'while' loops are powerful tools in Python that allow you to automate and repeat tasks in an efficient manner.

</details>

### 2.1.2 Displaying the Game Board
For our Tic Tac Toe game, we want to present the game board in a way that's easy for players to understand. This means separating each cell and each row visually. We can accomplish this by modifying our previous loop:
```python
for row in game_board:
    print('|'.join(row))
    print('---')
```
In this modified version, we use the join method to concatenate each cell in the row with a '|' character in between. This gives us a visual separator between cells in the same row.

We also add a second print statement to display a line of dashes '---' after each row, serving as a divider between rows.

However, we'll notice that this code adds an extra divider line after the last row. To fix this, we introduce a condition to check if we're at the last row:
```python
for index, row in enumerate(game_board):
    print('|'.join(row))
    if index < len(game_board) - 1:  # if it's not the last row
        print('---')
```
Here, we've added enumerate to our for loop, which provides a counter (index) as we iterate over the game_board. We then check if we're not at the last row before printing the divider line.

This gives us a visually pleasing game board that's easy for players to understand.
```
-|-|-
-----
-|-|-
-----
-|-|-
```
## 2.2 Making Moves: Control Flow
 
### 2.2.1 Control flow: directing the game's progression with conditionals.
### 2.2.2 Exercise: Check if a player's move is valid and if they've won.
## 2.3 Streamlining the Process: Functions
### 2.3.1 Learning about functions: simplifying our code and avoiding repetition.
### 2.3.2 Exercise: Break down the game logic into manageable functions.
## 2.4 Catching Mistakes: Error Handling

### 2.4.1 Handling errors: making our game foolproof with try and except statements.
### 2.4.2 Exercise: Improve the game's user experience by handling invalid inputs.

# Part 3: Assembling the Game
## 3.1 Applying What We've Learned

### 3.1.1 Review and apply all concepts learned to complete our Tic Tac Toe game.
## 3.2 Bonus Round: AI Concepts (Optional)
### 3.2.1 Introduction to basic AI concepts: understanding how AI could play Tic Tac Toe.
### 3.2.2 Exercise: Spice up the game by implementing a basic AI opponent.