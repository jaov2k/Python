if __name__ == "__main__":
    jar_jar = "Jar Jar Binks"
    #list of methods
    print(dir(jar_jar))

    #convert output to lower case output; does not change original object
    print(jar_jar.lower())
    #upper case output
    print(jar_jar.upper())

    #by using the lower method, you save having to check all the possible variations of the word, 'really, Really, REally', etc
    test_string = "this is a really long string, Probably from a Really long File and respresents a Line"
    print('really' in test_string.lower())

    #stripping leading and trailing white space
    Vaders_Cry = "               NOOOOOOOOO OOOOOOO OOOOOOOO OOOOOOO!!!!!!         "
    print("'" + Vaders_Cry + "'")
    print("'" + Vaders_Cry.strip() + "'")

    #left/right variations of strip()
    print("'" + Vaders_Cry.lstrip() + "'")
    print("'" + Vaders_Cry.rstrip() + "'")

    
    who_talks = "Who talk first? You talk first? I talk first."
    talk_location = who_talks.find('talk')
    print(talk_location)
    print(who_talks[talk_location:talk_location+len('talk')])
    print(who_talks[talk_location + len('talk'):])

    talk_location = who_talks.find('talk', talk_location + 1)
    print(talk_location)

    talk_location = who_talks.find('talk', talk_location + 1)
    print(talk_location)

    sith_lords = 'Sidius, Duku'
    sith_lords = sith_lords.replace('Duku','Vader')
    print(sith_lords)

    #methods can be chained one after the other.
    troubled_anakin = "Not just the men, but the women and the children too!"    
    print(troubled_anakin.replace('women', '').replace('men','').replace('children',''))