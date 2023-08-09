# time-between-days

A simple Python program that finds the calendrical difference (in years/months/days/weeks) between two given dates. 
The dates can be entered in any order.

## Usage: 

Run `python main.py` in your CLI/terminal of choice or run main.py through your Python IDE of choice.

Windows: In order to run this program via command line, [Python 3](https://www.python.org/downloads/) must be 
installed and added to the system PATH.

## Goals:

1. Re-familiarize myself with Python.
2. Create a program that is both simple and faster to use than a similar website from an online search.

## Comments:

Figuring out and implementing the correct behavior for various edge cases was a bit tricky.

Initially, I calculated the day in the year for both dates, found the absolute difference between the two, and used 
that to calculate the calendrical difference. This works if you only want to know the days or weeks between two dates, 
but when considering months, which do not have a consistent number of days, it becomes a bit more complicated.

In order to solve this issue, the two dates are sorted in order under the hood. This makes it significantly easier 
to find the difference in years and/or months between two dates. 

For leap year cases (aka years with 366 days), I consider 1/1 and 12/31 to still be the same year, even though 
there are 365 days between the two dates.

Edit 8/8/23: Added input validation when entering a date. It was more straightforward than I had expected. Part
of my concern was me trying to find a function that checks if an entire array is an int array (i.e., valid date), 
but that does not seem practical in Python. Instead, I opted to write my own function, looping through the input
string and seeing if its elements are/can be converted to positive integers.