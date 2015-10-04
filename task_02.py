#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program for auto email composition"""


import data


def prepare_email(appointments):
    """This function will generate auto emails for clients' appointments.

    Args:
        It takes one argument, appointment.

    Returns:
        A string with changing information.

    Examples:
    >>> ['Dear Gaye,\nI look forward to meeting with you on...'
    """
    mail = 'Dear {0},\nI look forward to meeting with you on {1}.\nBest, \nMe'
    new_list = []
    for info in appointments:
        new_list.append(mail.format(info[0], info[1]))
    return new_list

print prepare_email(data.get_email_data())
