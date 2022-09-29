dict = {}


def search_dictionary():
    key = input("Please enter the word you need to find : ")
    print(dict[key.lower()])


def print_dict():
    print(dict)


def add_vocabulary():
    key = input("Please enter the english word : ")
    value = input("Please enter the definition of the word : ")
    dict[key.lower()] = str(value)


def main():
    command = input("Please select the enter the command you need to progress ..... "
                    "\nA : Read the dictionory \nB : Add knowledge to dictionary "
                    "\nC : Search for a definition \nE: exit\n")
    if command.lower() == "a":
        print_dict()
    elif command.lower() == "b":
        add_vocabulary()
    elif command.lower() == "c":
        search_dictionary()
    elif command.lower() == "e":
        quit()

print("Welcome to my dictionary ......")
while True:
    main()