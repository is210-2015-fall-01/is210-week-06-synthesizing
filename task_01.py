#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Planning a picnic."""


def get_party_stats(families, table_size=6):
    """Calculates how many tables are required.

    Args:
        families: list; nested lists of family members
        table_size: int; default value of 6. Max number of guests per table.

    Returns:
        Total number of guests and tables required assuming no family can sit
        with another family.

    Examples:
        get_party_stats((['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']))
        (6, 3)
        get_party_stats((['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']), 2)
        (6, 4)
    Raises:
        TypeError: 'int' object is not iterable (returned if only the table_size
        is passed)
    """
    guests = 0
    tables = 0
    for family in families:
        guests += len(family)
        tables += -(-len(family) // table_size)
    return (guests, tables)
