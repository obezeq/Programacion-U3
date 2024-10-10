#!/usr/bin/env python3

# ASCII CODES MINUSCULA 97-122
# ASCII CODES MAYUSCULA 65-90
abc = []

for i in range(65, 91):
    abc.append(chr(i))

counter = 1
for i in abc:
    if counter % 3 == 0:
        letter = abc[counter-1]
        abc.remove(letter)
    counter += 1

print(abc)