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
    - [2.2.1  Validating Moves: IF \& ELSE](#221--validating-moves-if--else)
    - [2.2.2 Determining the Winner](#222-determining-the-winner)
    - [2.2.3 The Full Play Flow](#223-the-full-play-flow)
- [Part 3 - Improving the Code](#part-3---improving-the-code)
  - [3.1 Streamlining the Process: Functions](#31-streamlining-the-process-functions)
    - [3.1.1 Learning about functions: simplifying our code and avoiding repetition.](#311-learning-about-functions-simplifying-our-code-and-avoiding-repetition)
    - [3.1.2 Exercise: Break down the game logic into manageable functions.](#312-exercise-break-down-the-game-logic-into-manageable-functions)
  - [3.2 Catching Mistakes: Error Handling](#32-catching-mistakes-error-handling)
    - [3.2.1 Handling errors: making our game foolproof with try and except statements.](#321-handling-errors-making-our-game-foolproof-with-try-and-except-statements)
    - [3.2.2 Exercise: Improve the game's user experience by handling invalid inputs.](#322-exercise-improve-the-games-user-experience-by-handling-invalid-inputs)
  - [3.3 The Full Play flow (rename me)](#33-the-full-play-flow-rename-me)
- [Part 4: Implementing basic AI](#part-4-implementing-basic-ai)
  - [3.2 Bonus Round: AI Concepts (Optional)](#32-bonus-round-ai-concepts-optional)
    - [3.2.1 Introduction to basic AI concepts: understanding how AI could play Tic Tac Toe.](#321-introduction-to-basic-ai-concepts-understanding-how-ai-could-play-tic-tac-toe)
    - [3.2.2 Exercise: Spice up the game by implementing a basic AI opponent.](#322-exercise-spice-up-the-game-by-implementing-a-basic-ai-opponent)
- [Part 5: Review and Next Steps](#part-5-review-and-next-steps)
    - [3.1.1 Review and apply all concepts learned to complete our Tic Tac Toe game.](#311-review-and-apply-all-concepts-learned-to-complete-our-tic-tac-toe-game)
  - [3.1 Applying What We've Learned](#31-applying-what-weve-learned)
- [Part 6: Bonus - Advanced AI](#part-6-bonus---advanced-ai)

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
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"],
]
```
This is a list of lists - essentially a grid. Each inner list represents a row on the game board, and each space inside those lists represents a cell on that row. We start with all cells being `"-"`, which represents an empty cell. As the game progresses, these will be filled with `"X"` or `"O"`, depending on the players' moves.

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
 In any game, certain rules dictate what can and cannot happen, and our game of Tic Tac Toe is no exception. The way our program responds to different situations, like a player's move or the end of a game, is called control flow.

 By using these control flow structures, we can define the rules of our game, respond to player moves, and determine when the game ends. The ability to control the flow of our program based on conditions and loops is a fundamental aspect of programming and is key to building our Tic Tac Toe game.

### 2.2.1  Validating Moves: IF & ELSE 
In Python, we use conditionals, statements that control the flow of a program based on certain conditions, to guide our game's progress. The two most common conditional statements are 'if' and 'else'. An 'if' statement checks if a particular condition is true, and if so, it executes a block of code. The 'else' statement catches all other scenarios not caught by the 'if'.

For instance, in our game, we might want to check if a cell on the game board is empty before allowing a player to make a move. We can do that with an 'if' statement like this:
```python
# checking if the cell is empty
if game_board[row][col] == " ":
    game_board[row][col] = player_symbol
else:
    print("Invalid move! Try again.")
```
In this example, we're checking if the cell at a particular row and column is empty. If it is, the player's symbol is placed in that cell. If not, the game tells the player that the move is invalid.

And if we want to incorporate a loop to keep asking the player for a move until we get a valid move:
```python
while True:
    row = int(input("Enter the row for your move: "))  
    col = int(input("Enter the column for your move: ")) 

    # Check if the cell is empty
    if game_board[row][col] == "-":
        # Make the move
        game_board[row][col] = player_symbol
        # Exit the loop
        break
    else:
        # Notify the player that the move is invalid and they should try again
        print("Invalid move! Try again.")
```
Notice that if there are no valid moves left on the board, the loop will continue forever. This is called an infinite loop, and it's something we want to avoid. We'll learn how to handle this situation in a later section.

### 2.2.2 Determining the Winner
Beyond checking for valid moves, we also need to know when a player has won the game. In Tic Tac Toe, a player wins when they have three of their symbols in a row, column, or diagonal.

We can check for a win condition after every move by checking all rows, columns, and diagonals. Here's an example of how we might check for a win in a row:

**Checking for a win in a row**
```python
for row in game_board:
    if row.count(player) == 3:
        return True # we have not discussed functions yet
```
This loop iterates over each row in the game board. If a row contains three of the same player's symbol, it means that the player has won, so the function returns True.

**Checking for a win in a column**
To check if a player has won in any column, we have to inspect each column across all rows. Checking columns in less straightforward than checking the rows. Our game board is organize by rows, and so checking a row is just checking each cell of the row. However, for us to check vertical wins, we need to check the columns. For that we need to check the cell matching each column, in every row. So, we have to iterate over each row and within that, get the elements at the same column index. Here's how you might do it:

```python
game_won = False
player_symbol = "X"

for col in range(3):
  
  first_row = game_board[0][col]
  second_row = game_board[1][col]
  third_row = game_board[2][col]

  if first_row == player_symbol and 
    first_row == second_row and
    first_row == third_row:
      game_won = True
```
This code loops over each column index (0, 1, 2). For each column, it checks if all the rows have the same value at that column index and that the value isn't an empty space. If all values are the same (meaning, they're all the current player's symbol), it means the player has won, so the function returns True.

**Checking for a win in a diagonal**
Checking for a win in a diagonal is a bit different because there are only two diagonals, and each one needs to be checked separately. Here's how you might do it:

```python
  game_won = False
  player_symbol = "X"

  # Check the first diagonal (top left to bottom right)
  first_diagonal_top_left = game_board[0][0]
  middle_diagonal = game_board[1][1]
  first_diagonal_bottom_right = game_board[2][2]

  if first_diagonal_top_left == player_symbol and 
    first_diagonal_top_left == middle_diagonal and 
    first_diagonal_top_left == first_diagonal_bottom_right:
      game_won = True

  # Check the second diagonal (top right to bottom left)
  second_diagonal_top_right = game_board[0][2]
  second_diagonal_bottom_left = game_board[2][0]

  if second_diagonal_top_right == player_symbol and 
    second_diagonal_top_right == middle_diagonal and 
    second_diagonal_top_right == second_diagonal_bottom_left:
      game_won = True

```
Each if statement checks if all cells in a diagonal have the same value (i.e., they're all the current player's symbol) and that the value isn't an empty space. If this is the case, it means the player has won, so the function returns True.

By putting together these checks (for rows, columns, and diagonals), we can correctly determine when a player has won the game.

**Checking for all Wins**
Let's look at a more efficient way to do this. Since we know apriori that there are only 8 ways to win the game, we can check for all of them in one go. We will name each cell 0-8, and use a little math to figure out which row/column that refers to. Our game board looks like this:
  
```python
  0 | 1 | 2
  ---------
  3 | 4 | 5
  ---------
  6 | 7 | 8
```
So for us to check for all 3 types of wins, we can look at the specific combinations:

```python
game_won = False
EMPTY_COLUMN = "-"
winning_combinations = [
  (0, 1, 2), 
  (3, 4, 5), 
  (6, 7, 8), 
  (0, 3, 6), 
  (1, 4, 7), 
  (2, 5, 8), 
  (0, 4, 8), 
  (2, 4, 6)
]

for combination in winning_combinations:
    values = [game_board[cell//3][cell%3] for cell in combination]
    if values.count(values[0]) == 3 and values[0] != EMPTY_COLUMN:
        game_won = True 
        break
```
Let's look at some of the details;  

**Break Statement**  
```python
    if values.count(values[0]) == 3 and values[0] != EMPTY_COLUMN:
        game_won = True 
        break
```
Remember when I mentioned infinite loops ? Well, we can use the break statement to break out of a loop. In this case, we are using it to break out of the for loop as soon as we find a winning combination. This is because we don't need to check for any more wins once we find one.

**Loop: for ... in**  
`for combination in winning_combinations:`  
The for .. in loop is an extension of the for loop. It allows us to iterate over a list of items. In this case, we are iterating over the list of winning combinations. 

**List Comprehension & A Little Math**  
`values = [game_board[cell//3][cell%3] for cell in combination]`
This line of code is a bit tricky. It uses list comprehension to create a list of values from the game board. it is getting the `game_board[cell//3][i%3]` value for each `cell` in the `combination` list. The `game_board[cell//3][cell%3]` is a bit of math that allows us to get the correct row and column for each cell. `cell//3` means full integer division eg 
 - `4 // 3 = 1`
 - `6 // 3 = 2`
 - `7 // 3 = 2`
  
Now let's look at `cell%3`. This gets the value of what is the leftover of the full integer division. Here are some examples:
 - `4 % 3 = 1`
 - `6 % 3 = 0`
 - `7 % 3 = 1`
 - `8 % 3 = 2`




### 2.2.3 The Full Play Flow
build a mainloop here, bring it all together rough as it is. Mention MVPs, code that works, building a proof of concept 
# Part 3 - Improving the Code
## 3.1 Streamlining the Process: Functions
### 3.1.1 Learning about functions: simplifying our code and avoiding repetition.
### 3.1.2 Exercise: Break down the game logic into manageable functions.
## 3.2 Catching Mistakes: Error Handling

### 3.2.1 Handling errors: making our game foolproof with try and except statements.
### 3.2.2 Exercise: Improve the game's user experience by handling invalid inputs.
## 3.3 The Full Play flow (rename me)

# Part 4: Implementing basic AI
## 3.2 Bonus Round: AI Concepts (Optional)
### 3.2.1 Introduction to basic AI concepts: understanding how AI could play Tic Tac Toe.
### 3.2.2 Exercise: Spice up the game by implementing a basic AI opponent.

# Part 5: Review and Next Steps
### 3.1.1 Review and apply all concepts learned to complete our Tic Tac Toe game.
## 3.1 Applying What We've Learned

# Part 6: Bonus - Advanced AI





--------- alternative titles
Part 2: Game Logic
2.1 Looping Concepts
2.1.1 Power of Loops
2.1.2 Displaying the Board
2.2 Control Flow
2.2.1 Directing Game Progression
2.2.2 Validating Moves & Winning
2.3 Functions
2.3.1 Simplifying Code
2.3.2 Dividing Game Logic
2.4 Error Handling
2.4.1 Making the Game Foolproof
2.4.2 Handling Invalid Inputs
Part 3: Assembling the Game
3.1 Applying Concepts
3.1.1 Review & Application
3.2 AI Concepts (Optional)
3.2.1 Basic AI Principles
3.2.2 Creating an AI Opponent