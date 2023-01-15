def printTable(table):

    #to get list of lengths
    #of each element
    table_lengths = []
    for i in table:
        lengths = []
        for j in i:
            lengths.append(len(j))
        table_lengths.append(lengths)

    #for loop
    #print in format
    for i in range(len(table[0])):
        for j in range(len(table)):
            #to get value to
            #feed to rjust
            max_length = max(table_lengths[j])
            print(table[j][i].rjust(max_length), end = '  ')
        print()

        

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
        