#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides a function to calculate party stats"""


import data


def get_party_stats(families, table_size=6):
    """This function will calculate table to guest ratio.

    Args:
        It takes two arguments, families and table_size

    Returns:
        A tuple containing guest count and number of tables required

    Examples:
        >>>(1023, 310)
    """
    total_tables = 0
    count = 0
    for family in families:
        count = count + len(family)
        family_size = len(family)
        tables_per_fam = - (-family_size // table_size)
        total_tables = total_tables + tables_per_fam
    return (count, total_tables)

print get_party_stats(data.get_party_list(), 4)
