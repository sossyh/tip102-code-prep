"""
Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string 
sentence and returns the sentence with the order of the words 
reversed. The sentence will contain only alphabetic characters 
and spaces to separate the words. If there is only one word in the sentence, 
the function should return the original string.

For example:
sentence = "tubby little cubby all stuffed with fluff"
"fluff with stuffed all cubby little tubby"

reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence)
"""

"""
0. initilize an empty sting
1. use split() function to split the sentece using the spave as a delimiter
2. iteration over the array starting from the last element
2. append to a new string

string = tubby little cubby all stuffed with fluff
reveresed = [tubby, little, cubby, all, stuffed, with, fluff]
"""

def reverse_sentence(sentence):
    revered_sentence = ""
    new_sentence = sentence.split(" ")

    for j in range(-1, -len(new_sentence)-1, -1):

        if j == -len(new_sentence):
            revered_sentence += new_sentence[j]
        else:
            revered_sentence += new_sentence[j] + " "
    
    return revered_sentence



print(reverse_sentence("tubby little cubby all stuffed with fluff"))
print(reverse_sentence("Pooh"))
print(reverse_sentence(""))



"""
Problem 2: Goldilocks Number
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

"""


def godilocks_number(nums):

    maxnum = max(nums)
    minimun = min(nums)

    if maxnum == minimun:
        return -1 

    else:
        for i in range(len(nums)):
            if nums[i] != maxnum and nums[i] != minimun:
                return nums[i]
    