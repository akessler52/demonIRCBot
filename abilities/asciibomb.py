

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
    data = dictRef['data'].split(' ', 3)
    if len(data) > 3:
        jdata = "x {c}".format(c=data[3])
        for less in dictRef['bot'].lessers:
            dictRef['bot'] = less
            less.joinChan(data[3])
        printer(dictRef)
        for less in dictRef['bot'].lessers:
            dictRef['bot'] = less
            less.leave(data[3])
            # less.channels.remove(data[3])
    else:
        printer(dictRef)


def printer(dictRef):
    data = dictRef['data'].split(' ', 3)
    i = 0
    el_ascii = data[2]
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
    if len(data) > 3:
        say_in = dictRef[3]
    else:
        say_ing = dictRef['where']
    f = open(art_file)
    lines = f.readlines()
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.talk(say_in, lines[i])
        i += 1
        if len(lines) == i:
            break
    f.close()
