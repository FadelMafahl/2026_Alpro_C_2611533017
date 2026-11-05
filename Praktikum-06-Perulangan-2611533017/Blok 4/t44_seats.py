blockseat = int(input("Masukkan nilai: "))
for row in range(1, 4):
    print(f"Row", row,":", end=" ")
    for column in range(1, 6):
        if column == blockseat:
            break
        print(column, end=" ")
    print()