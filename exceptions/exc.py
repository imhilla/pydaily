# in python exceptions can be handled using a try statement
# the code that handles the exceptions is written in the except clause
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Ooops!", sys.exc_info()[0], "occured")
        print("Next entry")
        print()
print("The reciprocal of", entry, "is", r)
