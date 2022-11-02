# files are named location on disk to store related information
# when we want to read from or write to a file , we need to open it first
# when we are done, it needs to be closed so that resources that are tied with the file are freed

# opening file in python
# open() function to open a file
# f = open("test.txt", "w")  # open file in current directory
# f = open("C:/Python38/README.txt")  # specify full path
# f = open("exist.txt")
f = open("test.txt", mode="r", encoding="utf-8")
print(f)
f.close()

# use try finally block safer way
try:
    f = open("test.txt", mode="r", encoding="utf-8")
finally:
    f.close()

# best way to close file is by using with statement
# this ensures that the file is cosed when the block inside with statement is exited
with open("test.txt", mode="r", encoding="utf-8") as f:
    print("helooooooo")
