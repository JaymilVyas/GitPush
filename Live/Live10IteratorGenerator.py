l = [1, 2, 3, 4, 5, 6]
for i in l:
    print(i)

t = iter((10, 56, 98, 78, 46))
print(next(t))

j = list(range(1, 10))
print(j)

def sq(n):
    ll=[]
    for i in range(n):
        ll.append(i*i)
    return ll


def sq1(n):
    x=[i*i for i in range(n)]
    return x

print(sq(5))
print(sq1(5))

def sq2(n):
    x=[i*i for i in range(n)]
    yield x

print(sq2(6))