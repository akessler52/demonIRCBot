import time
from .echo import *
from .join import *
from .suicide import *
from .addOwner import *
from .telephone import *
from .createImp import *
from .identify import *
from .teach import *
from .github import *
from .rampage import *
from .leave import *
from .yell import *
from .createswarm import *
from .broadcast import *
from .becomeswarm import *
from .timedevent import *
from .repeat import *
from .asciibomb import *
from .hearMyName import *
from .getem import *

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
        if i%30 == 0:
            time.sleep(30)
