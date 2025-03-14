def goldilocks(bear=3):
    """
    :param bear: which number bear's food are you trying to eat; valid numbers: [1, 2, 3]
    :return: description of how the food's temperature is

    >>> goldilocks(bear=1)
    'too hot'
    """
    if bear == 1:
        return "too hot"
    elif bear == 2:
        return "too cold"
    elif bear == 3:
        return "just right"
    else:
        ValueError("There are only 3 bears!")


def rapunzel(hair_len=20):
    """Lets down hair from tower to be used as climbing rope

    :param hair_len: length of hair (cannot be negative)
    :return: strand of hair that is hair_len characters long

    >>> rapunzel(hair_len=15)
    '~~~~~~~~~~~~~~~'
    """
    if hair_len < 0:
        ValueError("hair_len cannot be negative!")

    return "~" * hair_len


def mary(white_as="snow"):
    """How white was mary's little lamb?

    >>> mary(white_as='salt')
    'Mary had a little lamb whose fleece was white as salt'
    """
    return "Mary had a little lamb whose fleece was white as {}".format(white_as)


def sleeping_beauty(awake=False):
    """Should Sleeping Beauty wake up?

    :param awake: if True then wake up; else snooze
    :return: string showing sleepiness or wakefulness
    """
    if awake is True:
        return "o_o"

    return "Zzzzz"
