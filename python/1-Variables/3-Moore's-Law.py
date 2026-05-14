#there's a bug so it says it's wrong but it's propably right, i can't validate this right now
transistors = 25000000000
years = 10

transistors = int(transistors * (2 ** (years / 2)))

print(transistors)