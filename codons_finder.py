import sys

if len(sys.argv) < 3:
    print ("Use: <program file name> <input file name> <output file name>")
    sys.exit(0)

filein = open(sys.argv[1], 'r')
fin = filein.read()
fout = open(sys.argv[2], 'w')

# split sequences by '>'
lista1 = str.split(fin, '>')[1:] #the file header is discarded

def evaluation1(seq):
    'Receives a sequence of codons and evaluates if it is equal to AADTAT'
    if seq == 'AAATAT':
       return True
    elif seq == 'AAGTAT':
       return True
    elif seq == 'AATTAT':
       return True
    else:
       return False

def evaluation2(seq):
    'Receives a sequence of codons and evaluates if it is equal to AAVATT'
    if seq == 'AAAATT':
       return True
    elif seq == 'AAGATT':
       return True
    elif seq == 'AACATT':
       return True
    else:
       return False
    

def main():

    choose_seq = input('Type sequence AADTAT or AAVATT ')
    choose_position =input('Type codons positions 34 or 45 ')
    
    for element in lista1:
        lista2 = str.replace(element, '\n', '')
        lista3 = str.split(lista2, '\r')

        names = []
        sequences = []
        try:
            for element in lista3:
                e = element.split('ATG',1)
                names.append(e[0])
                sequences.append(e[1])
        except IndexError:
            pass
        
        if choose_seq == 'AADTAT' and choose_position == '34':
            for i in sequences:
                seq = str(i[3:9])
                n = evaluation1(seq)
                if n == True:
                    e = str(names)
                    e1 = e.replace("['",'')
                    e2 = e1.replace("']",'')
                    fout.write('> ' + e2 + '\n' + str(seq) + '\n')

        if choose_seq == 'AADTAT' and choose_position == '45':
            for i in sequences:
                seq = str(i[6:12])
                n = evaluation1(seq)
                if n == True:
                    e = str(names)
                    e1 = e.replace("['",'')
                    e2 = e1.replace("']",'')
                    fout.write('> ' + e2 + '\n' + str(seq) + '\n')

        if choose_seq == 'AAVATT' and choose_position == '34':
            for i in sequences:
                seq = str(i[3:9])
                n = evaluation2(seq)
                if n == True:
                    e = str(names)
                    e1 = e.replace("['",'')
                    e2 = e1.replace("']",'')
                    fout.write('> ' + e2 + '\n' + str(seq) + '\n')

        if choose_seq == 'AAVATT' and choose_position == '45':
            for i in sequences:
                seq = str(i[6:12])
                n = evaluation2(seq)
                if n == True:
                    e = str(names)
                    e1 = e.replace("['",'')
                    e2 = e1.replace("']",'')
                    fout.write('> ' + e2 + '\n' + str(seq) + '\n')


    print("Done!")
    filein.close()

main()
