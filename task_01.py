#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""This is week 6 task_01"""


def get_party_stats(families, table_size=6):
    """This function will return number of tables with people.

    The purpose of this function is to analyze arbitrary lists of families and
    return a total headcount for your caterer as well as a total number of
    tables needed.

    Args:
        families (list): Will return number of families per table.
        table_size (int): Return table required per family.

    Returns:
           Total number of guest per table.

    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)
    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
    (6, 4)
    """

    total_tables = 0
    total_guest = 0

    for family in families:
        total_tables += -(-len(family)//table_size)
        total_guest += len(family)
    return total_guest, total_tables
