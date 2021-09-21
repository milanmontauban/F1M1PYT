import datetime


def start():
    print("Hello You, ik ben Milan!")
    print("Wie ben jij?")

    name = input('')

    print(f"hello {name}")
    print(f"De Datum en tijd is {datetime.datetime.today()}")
    print(f"{name} wil jij dit programa nog een keer doen?\nType Y/N")

    option = input('')
    
    if option.lower() == 'y':
        start()
    else:
        exit()


start()