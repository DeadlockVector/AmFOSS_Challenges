'''
1)Get dictionary.txt
2)List of all words
3)loop through list, try opening pdf file
4)uppercase and lowercase
'''
import PyPDF2 as pdf

#TODO: download dictionary
dictionary = ""
#list_words = dictionary_file.readlines()
f1 = open('home/isocyanate/testingEncryption.pdf', 'rb')
reader = pdf.PdfFileReader('home/isocyanate/testingEncryption.pdf')

'''
for word in list_words:
    pass
'''
