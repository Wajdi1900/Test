for n in range(2, 10):  # 2,3,4,5,6,7,8,9
    for x in range(4, n):  # 4,5,6,7,8,9
        for z in range(5, x):  # 5,6,7,8,9
            for y in range(6, z): #6,7,8,9
                print(n, x, z, y)
                break

print("final", n, x, z, y)
