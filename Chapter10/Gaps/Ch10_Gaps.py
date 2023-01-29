'''
All files have a given prefix
TODO: Rename each file everytime
Instead of checking gap in numbers
Rename everytime
'''
import re, shutil, os
#from pathlib import Path



def fixGap(directory, fileName_Regex):
    list_numbers = []
    
    for filename in os.listdir(directory):
        matches = fileName_Regex.search(filename)
        list_numbers.append(int(matches.groups()[0]))
        
    length_number = len(matches.groups()[0])
#prefix for the files to check
fileName_Regex = re.compile(r'Spam(\d\d\d).txt')

#directory to test the program 
directory = "/home/isocyanate/Desktop/AmFOSS_Challenges/Chapter10/Gaps/Testing"

fixGap(directory, fileName_Regex)