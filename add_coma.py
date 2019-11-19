#Añadir ; al final de las lineas, para que no se imprima /n.
with open('text3.txt', 'r') as istr:
    with open('text3_out.txt', 'w') as ostr:
        for line in istr:
            line = line.rstrip('\n') + ';'
            print(line, file=ostr)