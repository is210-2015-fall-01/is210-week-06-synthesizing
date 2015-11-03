#!/usr/bin/env python
# -*- coding: utf-8 -*
"""Task 02"""


def prepare_email(appointments):
    """Working on this email
    Args:
        appointments: A list of two-item tuples with the client's name
        and their appointment time as members
    Returns:
        Return your new list.

    """
    email = []
    reminder = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for remind in appointments:
        email.append(reminder.format(remind[0], remind[1]))
    return email
