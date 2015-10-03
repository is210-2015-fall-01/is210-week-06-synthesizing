#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the task_02 docstring."""


def prepare_email(appointments):
    """A mass appointment reminder function.

    This function takes a list of clients and their appointments as arguments
    and creates a reminder message body for each client as a list.

    Args:
        appointments (tuple): A list containing a tuple encapsulating names
                              and appointmen time for each client.

    Returns:
        email message body (list): A list containing the message body for
                                   each email message to be sent.

    Example:
        >>> prepare_email([('Andrew', '10/22/2015'),
                           ('Jane', 'Monday 8:00 AM')])
        ['Dear Andrew,\nI look forward to meeting with you on 10/22/2015.\n
          Best,\nMe', 'Dear Jane,\nI look forward to meeting with you on
          Monday 8:00 AM.\nBest,\nMe']

    """
    message = []
    string = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    for client in appointments:
        client_name = client[0]
        app_time = client[1]
        message.append(string.format(client_name, app_time))
    return message
