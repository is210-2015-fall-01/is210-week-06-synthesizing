#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating an appointment system with email blast."""


def prepare_email(appointments):
    """Generates the text of an email to clients.

    Args:
        appointments: A list of two-item tuples with the client's name and their
        appointment time as members

    Returns:
        A new list with the client's email body

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting with you on March 3.\nBest,\nMe']
        >>> prepare_email([('Mary Moore', '12.1.2015'), ('Jacob Jones', 'May 09,
        2016')])
        ['Dear Mary Moore,\nI look forward to meeting with you on 12.1.2015.\n
        Best,\nMe', 'Dear Jacob Jones,\nI look forward to meeting with you on
        May 09, 2016.\nBest,\nMe']
    """
    emailbody = []
    for client in appointments:
        emailstr = 'Dear {},\nI look forward to meeting with you on {}.' \
            '\nBest,\nMe'
        emailbody.append(emailstr.format(client[0], client[1]))
    return emailbody
