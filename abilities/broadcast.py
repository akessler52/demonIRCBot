import time


def broadcast(dictRef):
    data = dictRef['data'].split(' ')
    ability = data[1]
    # print('attempting to broadcast ability: ' + ability)
    # print('with data: ' + str(dictRef))

    # dictRef['bot'].performAbility(ability, dictRef)
    i = 0

    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.performAbility(ability, dictRef)
        time.sleep(.05)
        i += 1
        if i%25 == 0:
            time.sleep(10)
