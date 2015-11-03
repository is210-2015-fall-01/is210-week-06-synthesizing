#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Email task 02."""


def prepare_email(appointments):
    """This function creates a canned e-mail response just add name and date.

    Args:
        appointment(list): List of tuples.

    Returns:
        Str: Canned message.

    Example:
        >>> prepare_email([('Jen', '2015'), ('Max', 'October 3')])
        >>> ['Dear Jen,\nI look forward to meeting with you on 2015.
            \nBest,\nMe', 'Dear Max,\nI look forward to meeting with
            you on /October 3.\nBest,\nMe']
    """

    record = 0
    message = []
    canned = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for recipient in appointments:
        recipient = appointments[record]
        name = recipient[0]
        date = recipient[1]
        record += 1
        message.append(canned.format(name, date))

    return message
