#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02"""


def prepare_email(appointments):
    """A function thats reminds of appointments.

    Args:
        appointments (tuple): A list containing a tuple that takes names and
        appointment time for each name,

    Returns:
        email message body (list): A message body for each email.

    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    message = []
    string = 'Dear {}, \nI look forward to meeting with you on {}.\nBest,\nMe'
    for client in appointments:
        client_name = client[0]
        app_time = client[1]
        message.append(string.format(client_name, app_time))
    return message
