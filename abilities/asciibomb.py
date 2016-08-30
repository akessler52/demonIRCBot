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
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        f = open('art/dice')
        less.performAbility('echo', line)
        f.close()
