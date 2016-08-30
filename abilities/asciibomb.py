

# def asciibomb(dictRef):
#     data = dictRef['data'].split(' ', 4)
#     i = 0
#     el_ascii = data[2]
#     art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
#     f = open(art_file)
#     lines = f.readlines()
#     for less in dictRef['bot'].lessers:
#         dictRef['bot'] = less
#         less.talk(dictRef['where'], lines[i])
#         i += 1
#     f.close()

def asciibomb(dictRef):
    data = dictRef['data'].split(' ', 4)
    if len(data) < 4:
        print(dictRef)


def printer(dictRef):
    data = dictRef['data'].split(' ', 4)
    i = 0
    el_ascii = data[2]
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
    f = open(art_file)
    lines = f.readlines()
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.talk(dictRef['where'], lines[i])
        i += 1
    f.close()
