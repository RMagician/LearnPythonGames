# Let's Learn Python with Tic Tac Toe

## Intro
Welcome - This is a no bullshit tutorial to learn Python. We'll be building a simple Tic Tac Toe game and reviewing the key concepts you need to know to get started with Python.

In this lesson we will cover variables, data types, capturing user input, loops, conditionals, and functions, all while having some fun. 

<details><summary> I am an example 'more details sections' (click me)</summary>

In these sections you will find extra details that you may find helpful in order to understand the content ! If you already know the basics, you probably won't need to open these sections
</details>  
  
You will notice that you have sections that you can click in order to show more detail. If there is something you don't understand, check those out for more detail ! 


## Resources
- The code for the game, and jupyter notebooks with exercises can be found on this github
- The youtube video that covers this article can be found here

## Table of contents
1. To be done & linked
2. also to be done

# Starting the Project

As usual you'll want to setup a new virtual environment.

<details><summary>Click me If you don't know how to setup a virtual environment.</summary>

## Environment Setup


Before we start coding, we'll create a Python virtual environment for our project. A virtual environment is an isolated space where Python can run, keeping any dependencies you install separate from other projects. This is best practice & essential for avoiding package conflicts between projects.

Here are the quick steps to set one up:

 - Open your terminal or command prompt.
Navigate to your desired project directory using `cd path_to_your_directory`.
 - Create the virtual environment using `python3 -m venv .venv`, where `.venv` is your chosen environment name.
 - Activate it with `.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on Unix or MacOS.
  
Now you've created and activated your virtual environment, providing a dedicated space for your Python game project. Let's jump into coding!  
</details>
<br>

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