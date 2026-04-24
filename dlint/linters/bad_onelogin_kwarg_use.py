#!/usr/bin/env python

import functools

from .helpers import bad_kwarg_use

from .. import tree


class BadOneLoginKwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of OneLogin SAML keyword arguments.
    These arguments may indicate weaknesses in SAML authentication support.
    """
    off_by_default = False

    _code = 'DUO128'
    _error_tmpl = 'DUO128 insecure "OneLogin" SAML function call'

    @property
    def kwargs(self):
        pass
