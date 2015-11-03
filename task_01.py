#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring."""


def get_party_stats(families, table_size=6):
    """This is a function that defines how many guests and table should.
       be expected and planned.

    This functio helps with identifying how many tables, of a specific size,
    a party should have for a given number of guests.

    Args:
        families (list): A list of families (individual names)
        table_size (int, default = 6): Table size

    Returns:
        Total number of guests, Number of tables

    Example:
        >>> get_party_stats([['Joe', 'Jane', 'Alice'],
                             ['Heidi', 'Miriam'],['Adam']], 3)
        (6, 3)

    """
    num_guest = 0
    num_tables = 0
    for guest in families:
        num_guest += len(guest)
        num_tables += 1
        if len(guest) > table_size:
            num_tables += (len(guest) // table_size)
    return (num_guest, num_tables)
