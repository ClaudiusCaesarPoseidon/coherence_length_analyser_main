import os

def list_files(startpath):
    lst = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        lst.append('{}{}/'.format(indent, os.path.basename(root)))
#        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if 'spec' not in f and 'readme' not in f.lower() and 'license' not in f.lower():
                lst.append('{}{}'.format(subindent, f))
#            print('{}{}'.format(subindent, f))
    string = '\n'.join(lst)
    with open("structure.txt", "w") as file:
        file.write(string)

list_files(r"C:\Users\Haarmeyer\Desktop\git\coherence_length_analyser\coherence_length_analyser")