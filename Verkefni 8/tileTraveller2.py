# 1. Það var mun léttara að gera seinna verkefnið því að við gátum notað functions.
# 2. Það er mikið betra að lesa verkefni númer 2 þó að það hafi verið fleiri línur í þeim kóða, functions hjálpuðu okkur að dreifa kóðanum sem gerði hann þægilegri að lesa. 
# 3. Við bjuggum til lausn við fyrsta verkefninu og gátum notað hluta af henni aftur í seinna verkefninu. 

#https://github.com/aronhr/SC-T-111-PROG/edit/master/Verkefni%208

pos = 1.1
travel = "(N)orth."
no_print = True


def check_victory(p):
    """
    :param p:
    :return:
    """
    if p == 3.1:
        print("Victory!")
        quit()


def east(p, pr):
    """
    :param p:
    :param pr:
    :return:
    """
    if p == 1.1 or p == 2.2 or p == 3.3 or p == 3.2 or p == 2.1 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p += 1.0
        pr = True
    return p, pr


def west(p, pr):
    """
    :param p:
    :param pr:
    :return:
    """
    if p == 1.1 or p == 1.2 or p == 2.1 or p == 1.3 or p == 3.2 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p -= 1.0
        pr = True
    return p, pr


def north(p, pr):
    """
    :param p:
    :param pr:
    :return:
    """
    if p == 1.3 or p == 2.3 or p == 3.3 or p == 2.2:
        print("Not a valid direction!")
        pr = False
    else:
        p += 0.1
        pr = True
    return p, pr


def south(p, pr):
    """
    :param p:
    :param pr:
    :return:
    """
    if p == 1.1 or p == 2.1 or p == 2.3 or p == 3.1:
        print("Not a valid direction!")
        pr = False
    else:
        p -= 0.1
        pr = True
    return p, pr


def check_direction(d, p, pr):
    """
    :param d:
    :param p:
    :param pr:
    :return:
    """
    if d == "n":
        return north(p, pr)
    elif d == "s":
        return south(p, pr)
    elif d == "w":
        return west(p, pr)
    elif d == "e":
        return east(p, pr)
    else:
        print("Not a valid direction!")


def check_possible_directions(t):
    """
    :param t:
    :return:
    """
    if round_pos == 1.1:
        t = "(N)orth."
    elif round_pos == 1.2:
        t = "(N)orth or (E)ast or (S)outh."
    elif round_pos == 2.2:
        t = "(S)outh or (W)est."
    elif round_pos == 2.1:
        t = "(N)orth."
    elif round_pos == 1.3:
        t = "(E)ast or (S)outh."
    elif round_pos == 2.3:
        t = "(E)ast or (W)est."
    elif round_pos == 3.3:
        t = "(S)outh or (W)est."
    elif round_pos == 3.2:
        t = "(N)orth or (S)outh."
    return t


while True:
    round_pos = round(pos, 1)

    check_victory(round_pos)

    travel = check_possible_directions(travel)

    if no_print:
        print("You can travel:", travel)

    direction = input("Direction: ").lower()

    pos, no_print = check_direction(direction, round_pos, no_print)
