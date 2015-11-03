#!/usr/bin/env python
# -*- coding: utf-8 -*
"""Task 01"""


def get_party_stats(families, table_size=6):
    """Setting up for the party
    Args:
         a list of familes
        table_size the maximum number of seats at each table
    Returns:
         total number of guests
         total number of tables
    """
    guests = 0
    tables = 0
    for family in families:
        guests += len(family)
        tables += -(-len(family)//table_size)
    return (guests, tables)
