#  unpacking a sequence into separate variables

# problem
# you have an N-element tuple or sequence that would like to unpack into a collection on N variables.

# solution
# Any sequence (or iterable) can be unpacked into variables using a simple
# assignment operation. The only requirement is that the number of variables and structure match the sequence

# Discussion
# unpacking actually works with any object that happens to be iterable, not just tuples
# or lists, includes strings, files, iterators and generators.

# used terminal to test and solve
# [GCC 7.5.0] :: Anaconda, Inc. on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> p = (4, 5)
# >>> x, y = p
# >>> x
# 4
# >>> y
# 5
# >>> data = ['ACE', 50, 91.1, (2012, 12,21)]
# >>> name, shares, price, date = data
# >>> data
# ['ACE', 50, 91.1, (2012, 12, 21)]
# >>> date
# (2012, 12, 21)
# >>> name
# 'ACE'
# >>> shares
# 50
# >>> price
# 91.1
# >>> s = 'Hello'
# >>> a, b, c, d = s
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: too many values to unpack (expected 4)
# >>> a, b, c, d, e  = s
# >>> a
# 'H'
# >>> b
# 'e'
# >>> c
# 'l'
# >>> d
# 'l'
# >>> e
# 'o'
# >>> data = ['ACE', 50, 91.1, (2012, 12,21)]
# >>> _, shares, price, _ = data
# >>> _
# (2012, 12, 21)
# >>> price
# 91.1
# >>>
