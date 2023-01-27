
# to use os.listdir()
import os

import re  #for regex operations

# TODO: Add a second parameter so we can search in any directory
def readRegex(regexExp, directory = os.getcwd()):

    #listing out all files
    for filename in os.listdir(directory):

        #getting path name
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as f1:
                fileContent = f1.read()
                matches = regexExp.findall(fileContent)
                print('File - ', filename)
                for match in matches:
                    print(match[0])
                print()




#regexExp = re.compile(input('Enter the regex expression to search in the files  - '))
regexExp = re.compile(r'([a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')
directory = "/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter9/RegexSearch"
print('All emails in the files')
readRegex(regexExp, directory)
