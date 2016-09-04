import time
import re, socket


def hearMyName(dictRef):
    topDog = dictRef['bot']
    data = dictRef['data'].split(' ', 4)
    if len(data) > 3:
        if len(data) > 4:
            ayy(dictRef, topDog, "ayy")
        else:
            dictRef['bot'].joinChan(data[3])
            dictRef['bot'].channels.append(data[3])
            for less in dictRef['bot'].lessers:
                dictRef['bot'] = less
                less.joinChan(data[3])
                less.channels.append(data[3])
            time.sleep(1)
            dictRef['bot'] = topDog
            ayy(dictRef, topDog, "ayy")
            dictRef['bot'] = topDog
            time.sleep(1)
            for less in dictRef['bot'].lessers:
                dictRef['bot'] = less
                less.leave(data[3])
                less.channels.remove(data[3])
            topDog.leave(data[3])
            topDog.channels.remove(data[3])
    else:
        ayy(dictRef, topDog, "ayy")


def ayy(dictRef, top, names):
    data = dictRef['data'].split(' ', 4)
    i = 0
    el_ascii = names
    art_file = "/home/members/akessler/bots/demonIRCBot/abilities/names/{f}".format(f=el_ascii)
    if len(data) > 3:
        say_in = data[3]
    else:
        say_in = dictRef['where']
    f = open(art_file)
    lines = f.readlines()

    while i < range(len(lines)):
        for less in top.lessers:
            less.nick(lines[i])
            # ircsock.send("NICK " + lines[i])
            i += 1
            if len(say_in) > 6:
                time.sleep(0.05)
            if i % 29 == 0 and len(lines) > 30:
                time.sleep(2)
            if len(lines) == i:
                break
        if len(lines) == i:
            break
    f.close()
