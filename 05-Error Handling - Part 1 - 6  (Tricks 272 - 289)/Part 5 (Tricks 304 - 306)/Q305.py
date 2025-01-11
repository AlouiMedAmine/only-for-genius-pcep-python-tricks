"""

try:
    ...
except (TypeError, ValueError, ZeroDivisonError):
    ...

-----------

This syntax allows the except block to catch any
of the specified exceptions.

If any one of these exceptions occurs, the code
within the corresponding block will be executed.

It's important to enclose the exceptions within
parentheses to define them as a tuple and separate
different types of exceptions with commas.


"""