

file1 = open('/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter9/MadLibs/Madlibs.txt', 'r')

#Initial content
print('Content - ')
content = file1.read()
print(content)

list_strings = content.split()

for i in range(len(list_strings)):

    if "ADJECTIVE" in list_strings[i]:
        adj = input("Enter an adjective - ")
        list_strings[i] = list_strings[i].replace("ADJECTIVE", adj)
    
    elif "NOUN" in list_strings[i]:
        noun = input("Enter a noun - ")
        list_strings[i] = list_strings[i].replace("NOUN", noun)
    
    elif "VERB" in list_strings[i]:
        verb = input("Enter a verb - ")
        list_strings[i] = list_strings[i].replace("VERB", verb)

#displaying content
print('After replacing')
for i in list_strings:
    print(i, end = " ")
file1.close()

file2 = open('Madlibs_Result.txt', 'w')
for i in list_strings:
    file2.write(i)
    file2.write(' ')
file2.close()

