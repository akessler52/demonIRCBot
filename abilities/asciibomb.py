import time

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
    topDog = dictRef['bot']
    data = dictRef['data'].split(' ', 4)
    d = data[3]
    print(data[4])
    print(d.startswith('#'))
    if data[4] == '-pm':
        printer2(dictRef, dictRef['bot'])
    elif len(data) > 3:
        jdata = "x {c}".format(c=data[3])
        dictRef['bot'].joinChan(data[3])
        dictRef['bot'].channels.append(data[3])
        for less in dictRef['bot'].lessers:
            dictRef['bot'] = less
            less.joinChan(data[3])
            less.channels.append(data[3])
        time.sleep(1)
        dictRef['bot'] = topDog
        printer(dictRef, dictRef['bot'])
        dictRef['bot'] = topDog
        time.sleep(1)
        # for i in range(10000000):
        #     j = 1+1+3+635-123
        for less in dictRef['bot'].lessers:
            dictRef['bot'] = less
            less.leave(data[3])
            less.channels.remove(data[3])
        topDog.leave(data[3])
        topDog.channels.remove(data[3])
    else:
        printer(dictRef, dictRef['bot'])


def printer(dictRef, top):
    data = dictRef['data'].split(' ', 4)
    i = 0
    el_ascii = data[2]
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
    if len(data) > 3:
        say_in = data[3]
    else:
        say_in = dictRef['where']
    f = open(art_file)
    lines = f.readlines()
    # for less in top.lessers:
    #     dictRef['bot'] = less
    #     less.talk(say_in, lines[i])
    #     i += 1
    #     if len(lines) == i:
    #         break
    while i < range(len(lines)):
        for less in top.lessers:
            # top = less
            less.talk(say_in, lines[i])
            i += 1
            if len(say_in) > 6:
                time.sleep(0.05)
            if len(lines) == i:
                break
        if len(lines) == i:
            break
    f.close()


def printer2(dictRef, top):
    data = dictRef['data'].split(' ', 4)
    i = 0
    el_ascii = data[2]
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/art/{f}".format(f=el_ascii)
    if len(data) > 3:
        say_in = data[3]
    else:
        say_in = dictRef['where']
    f = open(art_file)
    lines = f.readlines()
    # for less in top.lessers:
    #     dictRef['bot'] = less
    #     less.talk(say_in, lines[i])
    #     i += 1
    #     if len(lines) == i:
    #         break

    for less in top.lessers:
        while i < range(len(lines)):
            # top = less
            less.talk(say_in, lines[i])
            i += 1
            if len(lines) == i:
                break
    i = 0
    f.close()
