#!/usr/bin/env python
# -*- coding: utf-8 *-*
"""Be our guest."""


def get_party_stats(families, table_size=6):
    """Input a list of family members returns headcount and tables needed.

    Args:
        families(list): Names of people in party
        table_size(int): How many people can fit at one table the default is 6.

    Returns: Int: Number of people and required tables

    Example:
        get_party_stats([['Jan'], ['Jen', 'Jess'],
        ['Jem', 'Jack', 'Janis']])
        >>> (6, 3)
    """

    people = 0
    tables = 0
    for guest in families:
        people += len(guest)
        seats = -(-len(guest) // table_size)
        tables += seats

    return people, tables
