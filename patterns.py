def pattern(n):
    stars = 0
    init_space = n - 1
    for i in range(1, 2 * n + 1):
        if (i > n):
            stars = 2 * n - i
        else:
            stars = i
        for j in range(0, init_space):
            print(end=" ")
        for x in range(0, stars):
            print("*", end=" ")
        print("\r")
        if (i > n - 1):
            init_space += 1
        else:
            init_space -= 1


pattern(5)
