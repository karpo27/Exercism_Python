# Instructions
For want of a horseshoe nail, a kingdom was lost, or so the saying goes.

Given a list of inputs, generate the relevant proverb. For example, given the list ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"], you will output the full text of this proverbial rhyme:

![image](https://user-images.githubusercontent.com/54405665/210110652-2b146b02-8054-42fc-9532-69dfe5344eda.png)

Note that the list of inputs may vary; your solution should be able to handle lists of arbitrary length and content. No line of the output text should be a static, unchanging string; all should vary according to the input given.

In unpacking-and-multiple-assignment (https://exercism.org/tracks/python/concepts/unpacking-and-multiple-assignment), you learned multiple techniques for working with lists/tuples of arbitrary length as well as function arguments of arbitrary length. This exercise would be a great place to practice those techniques.

# How this exercise is implemented for Python
The test cases for this track add an additional keyword argument called qualifier. You should use this keyword arguments value to modify the final verse of your Proverb.
