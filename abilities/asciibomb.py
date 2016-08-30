

def asciibomb(dictRef):
    data = dictRef['data'].split(' ', 2)
    i = 0
    el_ascii = "dice"
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
    print('attempting to ascii')
    f = open(art_file)
    lines = f.readlines()
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.talk(dictRef['where'], lines[i])
        i += 1
    f.close()
