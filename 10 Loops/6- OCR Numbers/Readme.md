# Instructions
Given a 3 x 4 grid of pipes, underscores, and spaces, determine which number is represented, or whether it is garbled.

# Step One
To begin with, convert a simple binary font to a string containing 0 or 1.

The binary font uses pipes and underscores, four rows high and three columns wide.

![image](https://user-images.githubusercontent.com/54405665/207935522-e9a2135a-9609-4e0f-b7c7-2b80eae0b793.png)

Is converted to "0"

![image](https://user-images.githubusercontent.com/54405665/207935655-02edbdf8-4059-4cfb-8640-bc62ceb2c5f2.png)

Is converted to "1"

If the input is the correct size, but not recognizable, your program should return '?'

If the input is the incorrect size, your program should return an error.

# Step Two
Update your program to recognize multi-character binary strings, replacing garbled numbers with ?

# Step Three
Update your program to recognize all numbers 0 through 9, both individually and as part of a larger string.

![image](https://user-images.githubusercontent.com/54405665/207935760-56589638-0d7a-4f4a-b68c-68714379281c.png)

Is converted to "2"

![image](https://user-images.githubusercontent.com/54405665/207935810-ac74d216-8f42-47c3-87cb-a37cb40db575.png)

Is converted to "1234567890"

# Step Four
Update your program to handle multiple numbers, one per line. When converting several lines, join the lines with commas.

![image](https://user-images.githubusercontent.com/54405665/207935946-bcb3acb2-ba6a-4242-8ce4-1a5e2a8c4ea0.png)

Is converted to "123,456,789".

# Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a ValueError when the convert() function receives a string that isn't a valid OCR number. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

![image](https://user-images.githubusercontent.com/54405665/207936077-742cb705-3295-48a7-adbd-75c7e262ceb6.png)

