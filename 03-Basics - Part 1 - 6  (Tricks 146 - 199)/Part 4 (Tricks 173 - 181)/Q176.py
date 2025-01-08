from sys import argv
sum = 0

for  i  in range(2,  len(argv)):
       sum += float(argv[i])

print( " The average score for {0} is { 1:.2f} " .format(argv[1], sum/(len(argv) - 2))  )


"""
You want the following output: 
The average score for Peter is 200.00.

Which command do you have to execute 
in the command line?


Answer:   python index.py Peter 100 200 300

 
"""

