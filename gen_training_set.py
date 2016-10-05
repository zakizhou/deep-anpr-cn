# -*- coding: utf-8 -*-
"""
Created on Wed Oct 05 22:19:47 2016

@author: Windo
"""

import random
import utils


def make_pure_plate_code(show_code=False):
    """
    The first placeholder of any Chinese plate is the abbreviation of a province.
    The second placeholder is a upper char representing a city in this province.
    Three to six is any combination of upper chars and digits
    """
    code = u"{}{}·{}{}{}{}".format(random.choice(utils.provinces),
                                    random.choice(utils.chars),
                                    random.choice(utils.elements),
                                    random.choice(utils.elements),
                                    random.choice(utils.elements),
                                    random.choice(utils.elements))
    if(show_code==True):
        print(code)
    return code
    