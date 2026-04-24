#!/usr/bin/env python

import functools

from .helpers import bad_kwarg_use

from .. import tree


class BadItsDangerousKwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of itsdangerous keyword arguments. These
    keyword arguments may indicate insecure signing is being performed.
    """
    off_by_default = False

    _code = 'DUO137'
    _error_tmpl = 'DUO137 insecure "itsdangerous" use allowing empty signing'

    @property
    def kwargs(self):
        pass
