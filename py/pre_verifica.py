#!/bin/bash

import random

def fill_list(p_list):
    num = utilities.cinput("Quanti elementi vorresti generare? ",
                            "Inserisci un numero intero: ",
                            "Inserisci un numero positivo non nullo: ",
                            int,
                            lambda x: x > 0)

    for i in range(num):
        p_list.append(random.randint(0, 100))

def split_list(p_list, condition):
    return [x for x in p_list if condition(x)], [x for x in p_list if not condition(x)]

