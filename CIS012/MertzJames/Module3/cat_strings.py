if __name__ == "__main__":
    
    #Concatenation

    #You can concatenate two strings together using +.
    leia = "I love you."
    han = "I know."
    print(leia + ' ' + han)

    #Indexing a string
    ship = "Millennium Falcon"
    print(ship[0])

    #indexing a range in a string
    #Python starts at 0, slices TO the end index (not including)
    print("'" + ship[0:9] + "'")
    
    #a blank range assumse either from the very first or to the very last index
    print("'" + ship[:12] + "'") #from 0 index to 12
    print("'" + ship[11:] + "'") #from 11 to end

    bold_statement = ship + " is the fastest ship in the galaxy"
    print(bold_statement)

    #Strings are immutable; this will not compile
    #ship[0] = 'S'

    #String can be modified by using concatenation
    #concatenate an 'S' + everything AFTER the [0] index letter, 'M', returning 'Sellennium Falcon'
    ship = 'S' + ship[1:]
    print(ship)

    #'in' operator check to see if the right side contains the left side
    jedi_masters = "Obi-Wan Kenobi, Yoda, Qui-Gon Gin"
    print('Anakin' in jedi_masters)

    council_members = "Anakin, Obi-wan Kenobi, Qui-Gon Gin"
    print("Anakin" in council_members)