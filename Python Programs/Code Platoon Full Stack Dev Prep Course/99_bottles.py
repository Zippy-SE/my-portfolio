def bottle_word(n):
    return "bottle" if n == 1 else "bottles"

for n in range(99, 0, -1):
    next_n = n - 1

    print(f"{n} {bottle_word(n)} of beer on the wall, {n} {bottle_word(n)} of beer.")
    if next_n > 0:
        print(f"Take one down and pass it around, {next_n} {bottle_word(next_n)} of beer on the wall.")
    else:
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    print()

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    
    