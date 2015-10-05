#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01"""


def get_party_stats(families, table_size=6):
    """This function helps set up for the party.

    Args:
        families (list): number of family members.
        table_size (int): number of tables available.  Default set to 6.

    Returns:
        total number of guests.
        total number of tables.

    Examples:
    >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    """
    guests = 0
    tables = 0
    for family in families:
        guests += len(family)
        tables += -(-len(family) // table_size)
    return (guests, tables)
