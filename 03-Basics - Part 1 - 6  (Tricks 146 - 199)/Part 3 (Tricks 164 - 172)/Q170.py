"""

You have the following file.
index.py
----

from sys import argv
print(argv[1] + argv[2])


You run the file by executing the following
command in the terminal.

 python index.py 42 3

Q170: What is the expected output?


Answer: 423



------------------
Explanation:

argv[0] # index.py

argv[1] # "42"

argv[2] # "3"

argv[1] + argv[2] = "42"  + "3" = "423"

"""