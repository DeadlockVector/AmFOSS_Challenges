'''
All files have a given prefix
TODO: Rename each file everytime
Instead of checking gap in numbers
Rename everytime
'''
import re, os
#from pathlib import Path

#prefix for the files to check
fileName_Regex = re.compile(r'Spam(\d).txt')

#directory to test the program 
directory = "/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter10/Gaps/Testing"

i = 1    
for filename in os.listdir(directory):
    matches = fileName_Regex.search(filename)
    os.rename(directory+'/'+filename, directory+'/'+filename[:len(filename)-5]+str(i)+'.txt')
    print('og', directory+'/'+filename)
    print('new', directory+'/'+filename[:len(filename)-5]+str(i)+'.txt')
    i += 1
   