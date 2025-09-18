def main():
    print("Two-dimensional arrays (tuples and lists).")

    # here is a mystery 3 x 3 matrix from HW3

    # a 2-d tuple is a tuple whose elements are tuples
    kernel = (
        (0.05, 0.20, 0.05),
        (0.20, 0, 0.20),
        (0.05, 0.20, 0.05),
    )

    print(kernel)

    # I can access individual elements 
    # kernel[r][c] gives element at row r, col c
    print(kernel[0][2])
    print(kernel[1][1])
    print(kernel[2][1])

    # we can isolate rows too 
    print("Row 1 is", kernel[1])

    # tuples are immutable, so not that practical most of time 
    # kernel[1][1] = 0.3 # type error!

    # say we want to make a 2-d list with 7 rows and 4 columns 

    # remember: ...
    a = [0] * 7
    print(a)

    # declaring a 7 x 4 list
    a = [[0] * 4] * 7

    for r in range(7):
        print(a[r])

    # changing an element 
    a[1][3] = 5

    print("List has been changed!")

    for r in range(7):
        print(a[r])

    # this is the ugly of python 
    # what happened? We created only one list of length 4, and we created 7 references to it ?!!!

    a = []
    for row in range(7):
        new_row = [0] * 4
        a.append(new_row)

    print("a has been updated.")

    print(a)

    print("Changing one value? Yes :)")

    a[1][3] = 5
    print(a)


if __name__ == "__main__":
    main()