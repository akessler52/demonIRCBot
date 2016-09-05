import time


def getem(dictRef):
    data = dictRef['data'].split(' ', 3)
    top = dictref['bot']
    i = 0
    while True:

        dictRef['bot'].performAbility(tell, "pilar: tell pilar zag: spawnoverlord  60 {j}".format(j=i)
        # dictRef['bot'].performAbility(tell, "zag: spawnoverlord 60 {j}".format(j=i)
        # time.sleep(.02)
        # dictRef['bot'].performAbility(tell, "overlord{j}: tell {n} test".format(j=i, n=data[2]))
        # time.sleep(70)
        # dictRef['bot'].performAbility(tell, "{t}".format(t=top))
        i = i+1
