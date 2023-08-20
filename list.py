x = 'abc'
list1 = (c := ord(a) for a in x if ord(a) > 97)
list2 = list(filter(lambda c: c > 97, map(ord, x)))
t = (1, 2)

print(t)
print(tuple(reversed(t)))

print(next(list1))
for a in list1:
    print(a)
print(list2)

def fix(o):
    try:
        hash(0)
    except TypeError:
        return False
    return True