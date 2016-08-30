# def asciibomb(dictRef):
#     data = dictRef['data'].split(' ', 3)
#     print(data)
#     target = data[2] #who it is directed to
#     message = data[3]
#     message = "{m}".format(m=message)
#     dictRef['bot'].talk(target, message)

def asciibomb(dictRef):
    data = dictRef['data'].split(' ', 2)
    el_ascii = data[2]
    print('attempting to ascii')
    for i in dictRef['bot'].lessers:
        dictRef['bot'] = less
        f = open('masters.txt')
        for line in f:
            print line,
            sck.send('PRIVMSG ' + chan + " " + line)
        f.close()
        less[i].performAbility(ability, dictRef)
