import time


def getem(dictRef):
    data = dictRef['data'].split(' ', 3)
    top = dictRef['bot']
    i = 0
    a = 1
    while a == 1:

        data = dictRef['data'].split(' ')
        ability = data[1]
        # print('attempting to broadcast ability: ' + ability)
        # print('with data: ' + str(dictRef))

        # dictRef['bot'].performAbility(ability, dictRef)
        i = 0

        while True:
            for less in dictRef['bot'].lessers:
                dictRef['bot'] = less
                less.performAbility(ability, dictRef)
                time.sleep(.05)
                i += 1
                if i%30 == 0:
                    time.sleep(30)
        # dictRef['bot'].performAbility(tell, "zag: tell pilar zag: spawnoverlord  60 {j}".format(j=i))
        # dictRef['bot'].performAbility(tell, "zag: spawnoverlord 60 {j}".format(j=i))
        # time.sleep(.02)
        # dictRef['bot'].performAbility(tell, "overlord{j}: tell {n} test".format(j=i, n=data[2]))
        # time.sleep(70)
        # dictRef['bot'].performAbility(tell, "{t}".format(t=top))
        # i = i+1
        # if i == 120:
        #     a = 0
