#Task-2

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = int(input())
bc = int(input())

h = math.sqrt(ab**2 + bc**2)
h = h/2.0
adj = bc/2.0

print(str(int(round(math.degrees(math.acos(adj/h))))) + u'\N{DEGREE SIGN}')
