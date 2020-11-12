def dedup(lst):
    """ Removes duplicates form lst.

    :param lst: list
    :return: new list without duplicated elements

    linear for time and space
    """
    result = []
    repeted = set()

    for elm in lst:
        if elm not in repeted:
            result.append(elm)
            repeted.add(elm)
    return result


print(dedup(['1', '1', '6', '4']))
