#!/bin/bash

import random
from py.modules import utilities


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


def sum_list(p_list):
    return sum(p_list)


def element_counter(p_list):

    l_list = p_list[:]
    e_counter = []
    counter = 0

    for e in p_list:
        while e in l_list:
            counter += 1
            l_list.remove(e)

        if counter > 0:
            e_counter.append((e, counter))

        counter = 0

    e_counter.sort(key=lambda x: x[0])

    return e_counter


def print_num(p_list):
    for num, count in p_list:
        print("{:<4}{:<100}".format(num, "*"*count))


l = []

fill_list(l)
splited_list = split_list(l, lambda x: (x % 2) == 0)

if sum_list(splited_list[0]) < sum_list(splited_list[1]):
    print(f"La somma dei numeri pari {sum_list(splited_list[0])}"
          f" è minore alla somma dei numeri dispari {sum_list(splited_list[1])}")
elif sum_list(splited_list[0]) > sum_list(splited_list[1]):
    print(f"La somma dei numeri pari {sum_list(splited_list[0])}"
          f" è maggiore alla somma dei numeri dispari {sum_list(splited_list[1])}")
else:
    print(f"La somma dei numeri pari {sum_list(splited_list[0])}"
          f" è uguale alla somma dei numeri dispari {sum_list(splited_list[1])}")

if len(splited_list[0]) < len(splited_list[1]):
    print("La lista dei numeri dispari ha più elementi.")
elif len(splited_list[0]) > len(splited_list[1]):
    print("La lista dei numeri pari ha più elementi.")
else:
    print("Le due liste hanno stesso numero di elementi.")

c = element_counter(l)
print_num(c)
