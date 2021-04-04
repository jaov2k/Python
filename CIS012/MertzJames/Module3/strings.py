if __name__ == "__main__":

    obis_hello = "Hello There"

    str_length = len(obis_hello)
    print(str_length)

    for index, char in enumerate(obis_hello):
        print(f'{index:02}->"{char}"')

    #Mind the single quote
    Lukes_quote = "I'll never turn to the dark side."
    print(Lukes_quote)

    #triple quotes for multiline statements or use the special character, '\n'
    long_quote = """The dark side of the force is a pathway to many
abilities some consider to be unnatural."""
    print(long_quote)