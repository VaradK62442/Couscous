# Couscous - a programming language that can also be read as music

'''

Notes from low e to high e are variables that initially hold 0
They are incremented and decremented by writing them as sharps or flats
Since e and b notes do not have sharps, they notes are reserved for key operations

When initialised:
e - N/A
d - 0
c - 0
b - N/A
a - 0
G - 0
F - 0
E - N/A

Key operations:
Output note as ASCII character - e
Input as ASCII character and store to note - E
The target note and operation must be played at the same time, for example e/a would output the value in a
Loops are written as repeats, coded as [: and :]
The value of the note before the loop indicates how many times to loop

Coding:
High E -> e
High D -> d
High C -> c
High B -> b
High A -> a
Low G -> G
Low F -> F
Low E -> E
C Sharp -> cs
D Flat -> df

print("Hello World!") ->
ds ds ds ds ds ds ds ds d [: cs cs cs cs cs cs cs cs cs df :] e/c
ds ds ds ds d [: cs cs cs cs cs cs cs df :] cs e/c
cs cs cs cs cs cs cs e/c e/c
cs cs cs e/c
ds ds ds ds ds ds ds ds d [: as as as as df :] e/a
ds ds ds ds ds ds ds ds ds ds ds [: Gs Gs Gs Gs Gs Gs Gs Gs df :] Gf e/G 
e/c
cs cs cs e/c
cf cf cf cf cf cf e/c
ds ds ds ds d [: cf cf df :] e/c
as e/a

'''

def parse(d, c, a, G, F):
    code = input("c>>>")
    inputs = input("i>>>")
    operations = code.split(" ")

    loops = []
    i = 0
    next = -1

    while i < len(operations):
        i = 0
        match len(operations[i]):
            case 1:
                loops.append(operations[i])
            case 2:
                match operations[i][0]:
                    case 'd':
                        if operations[i][1] == 's':
                            d += 1
                        else:
                            d -= 1
                    case 'c':
                        if operations[i][1] == 's':
                            c += 1
                        else:
                            c -= 1
                    case 'a':
                        if operations[i][1] == 's':
                            a += 1
                        else:
                            a -= 1
                    case 'G':
                        if operations[i][1] == 's':
                            G += 1
                        else:
                            G -= 1
                    case 'F':
                        if operations[i][1] == 's':
                            F += 1
                        else:
                            F -= 1
################################################################################################
                    case '[': # start loop
                        pass
                    case ':': # end loop
                        pass
################################################################################################
            case 3:
                match operations[i][0]:
                    case 'e':
                        match operations[i][2]:
                            case 'd':
                                print(chr(d), end='')
                            case 'c':
                                print(chr(c), end='')
                            case 'a':
                                print(chr(a), end='')
                            case 'G':
                                print(chr(G), end='')
                            case 'F':
                                print(chr(F), end='')
                    case 'E':
                        match operations[i][2]:
                            case 'd':
                                d = ord(inputs[0])
                            case 'c':
                                c = ord(inputs[0])
                            case 'a':
                                a = ord(inputs[0])
                            case 'G':
                                G = ord(inputs[0])
                            case 'F':
                                F = ord(inputs[0])
                        inputs.remove(0)

        if next != -1:
            i = next
        else:
            i += 1
            


def main():
    d, c, a, G, F = 0, 0, 0, 0, 0
    parse(d, c, a, G, F)


if __name__ == "__main__":
    main()