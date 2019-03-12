import os

def take_note(file, prompt='Please enter your note: '):
    text = input(prompt)
    file.write('{}\n'.format(text))
    file.close()

def read(filename):
    file = open(filename, 'r')
    for line in file.readlines():
        print(line)
    file.close()

def restart(filename):
    file = open(filename, 'w+')
    file.seek(0)
    file.truncate()
    take_note(file)

def append(filename):
    file = open(filename, 'a+')
    take_note(file, 'Please enter the text you would like to append: ')

def note_taker():
    print('Welcome to Note Taker.')
    name = input("Please enter a file name: ")
    filename = '{}/{}'.format(os.getcwd(), name)

    if os.path.isfile(filename):
        print('What would you like to do?\n\tA) Read the file.\n\tB) Delete the file and start over.\n\tC) Append the file.')
        option = input('Please enter either A, B, or C: ')
        option = option.upper()
        if option not in {'A', 'B', 'C'}:
            print('{} is not a valid option. Goodbye.'.format(option))
        else:
            {
                'A': read,
                'B': restart,
                'C': append
            }.get(option)(filename)
    else:
        print('{} does not exist in the current directory. It will be created.'.format(name))
        file = open(filename, 'w+')
        take_note(file)

if __name__ == "__main__":
    note_taker()