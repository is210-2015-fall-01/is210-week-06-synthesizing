#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


def prepare_email(appointments):
    """Explaining the function get_party_stats.
    Args:
       appointments(list):A list of two-item tuples with the client's name
       and their appointment time as members.
    Returns:
        email(list): returns a new list with an email reminder.
    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    email = []
    reminder = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for remind in appointments:
        email.append(reminder.format(remind[0], remind[1]))
    return email
