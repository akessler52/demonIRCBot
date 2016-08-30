# def asciibomb(dictRef):
#     data = dictRef['data'].split(' ', 3)
#     print(data)
#     target = data[2] #who it is directed to
#     message = data[3]
#     message = "{m}".format(m=message)
#     dictRef['bot'].talk(target, message)

def asciibomb(dictRef):
    data = dictRef['data'].split(' ', 2)
    i = 0
    el_ascii = "dice"
    art_file = "./art/{f}".format(f=el_ascii)
    print('attempting to ascii')
    f = open('/home/members/akessler/bots/demonIRCBot/abilities/art/dice')
    lines = f.readlines()
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.talk(dictRef['where'], lines[i])
        i += 1
    f.close()
