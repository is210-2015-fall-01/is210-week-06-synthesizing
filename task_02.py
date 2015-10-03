#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This will be used to e0mail reminder e-mail for appointments."""


def prepare_email(appointments):
    """This function
    Args:
         appointments(two-item tuple): client's name and appointment time

    Returns:
        list with strings that states information to be in e-mail body

    Examples:

        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        {'Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
    """
    body = []
    statement = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for confirm in appointments:
        body.append(statement.format(confirm[0], confirm[1]))
    return body
