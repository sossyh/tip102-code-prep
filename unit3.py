"""
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

"""

"""
uderstand:
- we need to make sure that we have opning part for every closing part
- If we get a closing we need to make sure that it maches the opening part

plan:
step1: define a dictionary to map the opening and the closing
step2: defin a stack
step3: iterate over the string 
step4:  if it is opening add it to the stack
        else if it is the wrong opning return false
        or else if it is the right one pop from the stack

step5: return true if the stack is empty other false


"""

def is_valid_post_format(posts):
    d = {')':'(', '}': '{', ']':'['}
    stack = []

    for partensis in posts:
        if partensis == '(' or partensis =='{' or partensis == '[':
            stack.append(partensis)
        elif partensis == ')' or partensis == '}' or partensis ==']':
          if stack[-1] == d[partensis]:
            stack.pop()
          else:
            return False
    
    return len(stack) == 0


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))


"""
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']


"""
"""
understand:
- reversing the order of the quuee of comments given

plan:
step1: ninitialize stack, list (answer)
step2: iterate the quee and put elements to the stack
step3: pop elemets from the stack and put to the list (answer)
step4: return the answer list


"""      

def reverse_comments_queue(comments):
  answer, stack = [], []

  for com in comments:
    stack.append(com)
  
  while len(stack) > 0:
    ele = stack.pop()
    answer.append(ele)
  
  return answer

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))



"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Example Output:

True
False



understad:
- we are expected to check if the given string a palinderom or not
- we dont consider spaces

plan:
step1: initialize two pointers one at end and one at the start
sptt3: iterate over the title
       if the tow pointer are alphamiumeric
        if the two pointers have the same elemet moveboth (lower case)
        else retun false
      if one of them are not alphanumeric move
      
stepr: fretu true
"""

def is_symmetrical_title(title):
  i, j = 0, len(title) - 1

  while i < j:
    while not title[i].isalnum():
      i += 1
    while not title[j].isalnum():
      j -= 1
    
    if title[i].lower() != title[j].lower():
      return False
    i += 1
    j -= 1

  return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 


"""
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]


"""


def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

