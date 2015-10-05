#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def get_party_stats(families, table_size=6):
    """Explaining the function get_party_stats.
    Args:
        familes(list): A list of familes
        table_size(int): The maximum number of seats at each table.
    Returns:
        guests(int): total number of guests
        tables(int): total number of tables

    Examples:
        >>> get_party_stats(['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)
    """
    tables = 0
    guests = 0
    for family in families:
        guests += len(family)
        tables += -(-len(family)//table_size)
    return (guests, tables)
