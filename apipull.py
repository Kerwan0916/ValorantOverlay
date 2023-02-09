
"""hash(guns) = [
    pistols: classic, shorty, frenzy, ghost, sheriff
    smgs: stinger, spectre
    shotguns: bucky, judge
    rifles: bulldog, guardian, phantom, vandal
    snipers: marshall, operator
    lmgs: ares, odin
]"""

import random

def momoAttaquant(oui, momo):
    if oui >= 54:
        temp = 5 * random()+1
        return momo % temp

print(momoAttaquant(59,12))


    