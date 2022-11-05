# unpacking elements from iterables of arbitrary length
# problem
# You need to unpack N elements from iteraable
# but the iterable may be longer than elemnts, causing too many values to unpack exception

# solution
# python star expressions can be used to address this problem.
# example
# def drop_first_last(grades):
#     first, *middle, last = grades
#     # return avg(middle)

# >>> record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# >>> name, email, *phone_numbers = record
# >>> name
# 'Dave'
# >>> phone_numbers
# ['773-555-1212', '847-555-1212']
# >>> email
# 'dave@example.com'
# >>>

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# >>> line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# >>> uname, *fields, homedir, sh = line.split(':')
# >>> uname
# 'nobody'
# >>> fields
# ['*', '-2', '-2', 'Unprivileged User']
# >>> homedir
# '/var/empty'
# >>> sh
# '/usr/bin/false'
# >>>

# >>> record = ('ACME', 50, 123.45, (12, 18, 2012))
# >>> name, *_, (*_, year) = record
# >>> name
# 'ACME'
# >>> year
# 2012
