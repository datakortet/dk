# -*- coding: utf-8 -*-
from dk.identifiers.email import is_email

valid_emails = ['erlend.dalen@gmail.com', 'a@b.com', 'ed@norsktest.no']
invalid_emails = ['erlend@gmail_com', 'test^@.here.com', 'somewhere_there.no', 'not@anywherebuthere']


def test_emails():
    for email in valid_emails:
        assert is_email(email)

    for email in invalid_emails:
        assert not is_email(email)
