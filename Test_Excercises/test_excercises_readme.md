 I did not create the exercises listed below. I got them from: http://www.practicepython.org
\
\
Exercise 1\
\
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.\
\
============================\
\
Exercise 2\
\
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?\
\
==============================\
\
Exercise 3 \
\
Take a list, say for example this one:\
\
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\
and write a program that prints out all the elements of the list that are less than 5.\
==============================\
Divisors  \
Exercise 4 \
\
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don\'92t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)\
======================================\
Exercise 5 \
\
Take two lists, say for example these two:\
\
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]\
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.\
===============================\
Exercise 6 \
\
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)\
==================================\
Exercise 7 \
\
Let\'92s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.\
\
ages = [2014 - year for year in years_of_birth]\
=================================\
Exercise 8 \
\
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)\
====================================\
Exercise 9 \
\
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)\
=====================================\
Exercise 10 \
\
This week\'92s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.\
\
Take two lists, say for example these two:\
\
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]\
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).\
\
The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.\
====================================\
Check Primality Functions   \
Exercise 11 \
\
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below\
\
Concepts for this week:\
\
Functions\
Reusable functions\
Default arguments\
=======================================\
List Ends \
Exercise 12 \
\
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.\
\
======================================\
\
Exercise 13 
\
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, \'85)\
\
========================================\
List Remove Duplicates  \
Exercise 14 
\
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.\
\
Extras:\
\
Write two different functions to do this - one using a loop and constructing a list, and another using sets.\
Go back and do Exercise 5 using sets, and write the solution for that in a different function.\
\
=======================================\
\
Exercise 15 
\
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:\
\
 My name is Michele\
Then I would see the string:\
\
 Michele is name My\
shown back to me.\
\
==========================================\
Exercise 16 
\
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.\
============================================\
Exercise 17 
\
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.\
\
=============================================\
Exercise 18 
\
Create a program that will play the \'93cows and bulls\'94 game with the user. The game works like this:\
\
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a \'93cow\'94. For every digit the user guessed correctly in the wrong place is a \'93bull.\'94 Every time the user makes a guess, tell them how many \'93cows\'94 and \'93bulls\'94 they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.\
============================================\
Exercise 19 
\
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: {\field{\*\fldinst{HYPERLINK "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"}}{\fldrslt \cf2 \ul \ulc2 http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture}}.\
\
The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.\
============================================}