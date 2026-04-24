#!/usr/bin/env python

import functools

from .helpers import bad_kwarg_use

from .. import tree


class BadUrllib3KwargUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of urllib3 keyword arguments. These
    keyword arguments may indicate insecure connections are being performed.
    """
    off_by_default = False

    _code = 'DUO132'
    _error_tmpl = 'DUO132 "urllib3" certificate verification disabled, insecure connections possible'

    @property
    def kwargs(self):
        # See 'urllib3.util.ssl_.resolve_cert_reqs' for more information
        pass
