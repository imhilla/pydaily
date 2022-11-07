# keeping the last N items
# problem
# you want to keep a limited history of the last few items seen during
# iteration or during some other kind of processing

# solution
# keeping a limited history is a perfectuse for collections.deque
# the following code performs a simple text match on a sequence of lines and yields
# the matching line with previous N lines of context when found

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# example use on afile
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
