
This repository was created for usage in the Programming and Scripting module from the Higher Diploma in Data Analytics course from ATU Galway.

Author: Neil Anglim
---


## Hello world
This first program is to simply show that we can create a simple program and run it.
It was also to create our GitHub accounts and inspire us to do our initial commits.

## Bank
This program asked us to make use of the different formatting which is available to us in python. It asks us to take two user inputs and then have the program output this information in a different format.

## Accounts
In this program we showed how to replace characters in a given range with different characters, with the aim of adding obscurity to an account number that might exist in a online banking application.

The reference I used was from (https://thispointer.com/replace-first-n-characters-from-a-string-in-python/).

## Collatz
The function defined at the beginning provides most of the hard work in this program.

The if statement checks if the number is even using modulus operation. If the remainder of the operation is zero, the number is even and the program divides the number by 2 and prints it out.

If the remainder is not zero, program performs the elif statement - multiplying the number by three and adding one, and prints out the result.

I found this quite confusing at the beginning, but cracked the case using help from this YouTube video (https://www.youtube.com/watch?v=lAp_5qTdOhM).

Andrew did ask that I output this onto one line, but I couldn't determine how to do that, and I like the way it looks output onto many different lines, finding it much easier to read!

## Weekday
(https://pynative.com/python/datetime/) 

In this program I make use of the datetime module. The script reads the date using the date.today, and then determines which print statement to print out based on the integer it receives from the module.

## Squareroot
source: (https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)
My maths being a bit rusty, I tried different methods to get this to work, but I couldn't find any way of making it function properly with the time I could allocate to it, I was continually getting TypeErrors when I thought I was getting somewhere.

## E's
This was a very difficult task as I found the coding relating to calling files and using os quite confusig at the beginning. 

The code calls in the os module to check if there is a file in place with the same name, and then it reads through the lines to see the number of 'e' characters which are in the file, then reads this back to the user.

## Plottask
(https://www.tutorialspoint.com/matlab/matlab_plotting.htm)
This task required a lot of learning and recalling of things I had not explored for a long time(math and graphs). But once it was working it was very rewarding.

The histogram reads from the random.normal distribution and then displays when called in using the plt.show().

And then in the second part of the code the function is plotted using the numpy array method and call in using the same function as the histogram
