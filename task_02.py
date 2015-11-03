#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week 6 task_02."""


def prepare_email(appointments):
    """This function will generate email body.

    This function will prepare some data and generate automated e-mails for
    clients.

    Args:
        appointments(tuple): Tuples that displays client's name.

    Returns:
        email(list): Returns auto generated email body.

    Example:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')]
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """

    messages = []
    email = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for email_body in appointments:
        messages.append(email.format(email_body[0], email_body[1]))
    return messages
