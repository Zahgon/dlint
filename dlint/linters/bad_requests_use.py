#!/usr/bin/env python

from .helpers import bad_kwarg_use

from .. import tree


class BadRequestsUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for use of the "verify=False" kwarg when using the
    "requests" module. SSL verification is good, use SSL verification.

    http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification
    """
    off_by_default = False

    _code = 'DUO123'
    _error_tmpl = 'DUO123 use of "verify=False" is insecure in "requests" module'

    @property
    def kwargs(self):
        pass
