# Instructions
Detect saddle points in a matrix.

So say you have a matrix like so:

![image](https://user-images.githubusercontent.com/54405665/206939685-c59cd462-189b-438b-b110-843105a741df.png)

It has a saddle point at row 2, column 1.

It's called a "saddle point" because it is greater than or equal to every element in its row and less than or equal to every element in its column.

A matrix may have zero or more saddle points.

Your code should be able to provide the (possibly empty) list of all the saddle points for any given matrix.

The matrix can have a different number of rows and columns (Non square).

Note that you may find other definitions of matrix saddle points online, but the tests for this exercise follow the above unambiguous definition.

# Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a ValueError if the matrix is irregular. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

![image](https://user-images.githubusercontent.com/54405665/206939735-917061d7-96e0-4e75-bf65-9c2021c0e56b.png)
