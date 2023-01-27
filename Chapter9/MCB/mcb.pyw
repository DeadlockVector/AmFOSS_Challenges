import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

#deleting specific key
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    pyperclip.copy("")
    try:
        del mcbShelf[sys.argv[2]]
    except:
        print('Invalid key')

#clearing entire shelf
#copying empty string to pyperclip
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete':
        pyperclip.copy("")
        mcbShelf.clear()

    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
