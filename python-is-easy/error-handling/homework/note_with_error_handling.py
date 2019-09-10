import os

def take_note(file, prompt='Please enter your note: '):
    text = input(prompt)
    file.write('{}\n'.format(text))
    file.close()

def read(filename):
    try:
        file = open(filename, 'r')
        for line in file.readlines():
            print(line)
    except OSError as e:
        print(f'An error occurred when opening {filename}: {e}')
    else:
        file.close()

def restart(filename):
    try:
        file = open(filename, 'w+')
        file.seek(0)
        file.truncate()
        take_note(file)
    except OSError as e:
        print(f'An error occurred when opening {filename}: {e}')

def append(filename):
    try:
        file = open(filename, 'a+')
        take_note(file, 'Please enter the text you would like to append: ')
    except OSError as e:
        print(f'An error occurred when opening {filename}: {e}')

def replace_line(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
    except OSError as e:
        print(f'An error occurred when opening {filename}: {e}')
    else:
        file.close()
    number_of_lines_of_text = len(lines)
    line_number = int(input('What line number would you like to replace?: '))
    if line_number > number_of_lines_of_text:
        print('Sorry, {} only has {} lines of text.'.format(os.path.basename(filename), number_of_lines_of_text))
    else:
        replacement_text = input('With what text would you like it to replaced?: ')
        lines[line_number - 1] = '{}\n'.format(replacement_text)
        try:
            file = open(filename, 'w')
            file.writelines(lines)
        except OSError as e:
            print(f'An error occurred when opening {filename}: {e}')
        else:
            file.close()

def note_taker():
    print('Welcome to Note Taker.')
    name = input("Please enter a file name: ")
    filename = '{}/{}'.format(os.getcwd(), name)

    if os.path.isfile(filename):
        print('What would you like to do?\n\tA) Read the file.\n\tB) Delete the file and start over.\n\tC) Append the file.\n\tD) Replace a line.')
        option = input('Please enter either A, B, C, or D: ')
        option = option.upper()
        if option not in {'A', 'B', 'C', 'D'}:
            print('{} is not a valid option. Goodbye.'.format(option))
        else:
            {
                'A': read,
                'B': restart,
                'C': append,
                'D': replace_line
            }.get(option)(filename)
    else:
        print('{} does not exist in the current directory. It will be created.'.format(name))
        try:
            file = open(filename, 'w+')
        except OSError as e:
            print(f'An error occurred when opening {filename}: {e}')
        else:
            take_note(file)

if __name__ == "__main__":
    note_taker()