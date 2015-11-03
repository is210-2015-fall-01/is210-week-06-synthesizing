#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module analyzes arbitrary lists of families."""


def get_party_stats(families, table_size=6):
    """This function analyzes lists of families and return a total headcount.
    Args:
        families(list): list of families which are lists of members
        table_size(int): maximum number of seats at each table

    Returns:
        a tuple with total number of guests and total number of tables

    Examples:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']])
        (6, 3)
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack',
        'Janis']], 2)
        (6, 4)
    """
    tot_guests = 0
    tot_tables = 0
    for member in families:
        tot_guests += len(member)
        tot_tables = tot_tables - (-len(member)//table_size)
    return (tot_guests, tot_tables)
