#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from unittest import TestCase

from django.db import close_old_connections


class BasicTest(TestCase):
    def setUp(self):
        print(30 * '-')
        os.environ.setdefault(
                "DJANGO_SETTINGS_MODULE",
                "mysite.settings"
        )
        from django import setup
        setup()

    def tearDown(self):
        close_old_connections()
        print(30 * '-')

    def test_empty(self):
        pass

    def test_error(self):
        with self.assertRaises(ZeroDivisionError):
            1/0
