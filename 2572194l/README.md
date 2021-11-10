# Chuxiang Luo

## Kata 1

### Problem: Return the number (count) of vowels in the given string.

### Solution: Create a array consists all vowels and check every char of string

## Kata 2

### Problem: Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed

### Solution: Splitting input by white space and get a array. Checking the length of each element and reverse those elements which consist five or more letter. Then every element are combined into a new string.

## Kata 3

### Problem: Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words

### Solution: Create a copy of input called result. If element of input is not anagram of word, remove it from result.

## Kata 4

### Problem: Given an array representing a series of floors you must reach by elevator, return an integer representing the total distance travelled for visiting each floor in the array in order.

### Solution: Start from the last element of array. Calculate the difference between it and its left element and add the difference into the sum.

## Kata 5

### Problem: Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations.

### Solution: Using modulo and adding all element of array to get the sum.