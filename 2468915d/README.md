# Aidan Dow

## Kata 1
### This problem involved counting the number of vowels in a String using JavaScript
The problem was solved by looping through each of the letters in the string, and for each letter looping through the vowels to check if the letter is a vowel. If it was, the counter variable is incremented. Finally, the counter is returned. 

This solution passed all of the tests



## Kata 2
### This problem involves reversing any word in a string which has a length of more than 5
The problem was solved by using the .split() function to split up the string into words. The words were then looped through, and added to a new array. If the length of the word was more than or equal to 5, then the word would be reversed when added to the new array. The array was then converted into a string using .join().

This solution passed all of the tests


## Kata 3
### This problem involves finding all anagrams of a string in an array of strings
The problem was solved by creating a HashMap where each letter in the string was mapped to the number of occurences. This way, the array could be looped through and the occurence of letters compared to the original string. If the occurences of each letter weren't the same, then the string would be flagged as not an anagram. This way, only those strings which were anagrams would be returned.

This solution passed all of the tests.

In the original implemention, the strings were only tested to see if each letter was present in the original string. This meant that strings which weren't anagrams were being returned, and thus, the code was failing the tests. This was resolved by using the hashmap, and checking the lengths of the strings.


## Kata 4
### This problem involves computing the distance travelled in an elevator, given an array of floors visited
The problem was solved by looping through the floors visited, and, keeping track of the previous floor visited, subtracting the value of the current floor from the last floor.

In the original implementation, the values were just summated as they were, however this was yielding the wrong answers. This was because travelling down floors would yield a negative distance, which when added, took away from the final sum. 

To rectify this, the absolute value of the difference in floors was taken.

After this change, the code passed all of the tests.



## Kata 5
### This problem involves calculating every permutation of coins which can be used to sum up to a total
The problem was approached by using the modulo function, and a double loop, whereby every coin was tested to see if it fit neatly into the total. Then the coin was 'used' against the total, and the remaining coins tested against the remaining sum. Unfortunately, the code doesn't produce the correct answer and doesn't pass the tests required.
