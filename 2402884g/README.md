# Davide

## Kata 1 Vowel Count

### Problem

Return the number (count) of vowels in the given string. We will consider a,e,i,o,u as vowels for this Kata (but not y) The input string will only consist of lower case letters and/or spaces.

### Solution

Iterate trough the given string and increment the counter every time a vowel is found

## Kata 2 Stop gninnipS My sdroW!

### Problem

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

### Solution

Split the given string into words, if a word has five or more letters, reverse it. Join the words back into a sentence

## Kata 3 Where my anagrams at?

### Problem

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none.

### Solution

Store in a dict the letters and its relative frequency in a dictionary. Do the same for each word in the given array, return only those that matches.

## Kata 4 Elevator Distance

### Problem

Given an array, calculate the sum of the differences of the adjacent members

### Solution

Iterate the array, subtracting one element to the next one and storing the cumulative sum in a variable. Return such variable
