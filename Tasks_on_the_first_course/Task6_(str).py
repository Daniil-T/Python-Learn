n = int(input())
if 1 < n <= 4:
    print(n, 'программиста')
elif 5 <= n <= 20:
    print(n, 'программистов')
elif n == 1:
    print(n, 'программист')
elif n == 0:
    print(n, 'программистов')
else:
    b = str(n)
    c = len(b)
    if c == 2:
        if 1 < n % 10 <= 4:
            print(n, 'программиста')
        elif n % 10 == 1:
            if n == 11:
                print(n, 'программистов')
            else:
                print(n, 'программист')
        else:
            print(n, 'программистов')
    elif c == 3:
        if 5 <= n % 100 <= 20:
            print(n, 'программистов')
        elif 1 < n % 10 <= 4:
            print(n, 'программиста')
        elif n % 10 == 1:
            if n == 111:
                print(n, 'программистов')
            else:
                print(n, 'программист')
        else:
            print(n, 'программистов')
    elif c == 4:
        if 5 <= n % 1000 <= 20:
            print(n, 'программистов')
        elif 1 < n % 10 <= 4:
            print(n, 'программиста')
        elif n % 10 == 1:
            if n == 1111:
                print(n, 'программистов')
            else:
                print(n, 'программист')
        else:
            print(n, 'программистов')
    elif c == 5:
        if 5 <= n % 10000 <= 20:
            print(n, 'программистов')
        elif 1 < n % 10 <= 4:
            print(n, 'программиста')
        elif n % 10 == 1:
            if n == 11111:
                print(n, 'программистов')
            else:
                print(n, 'программист')
        else:
            print(n, 'программистов')