#!/usr/bin/env python


from .helpers import bad_kwarg_use

from .. import tree


class BadHashlibUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe use of the Python "hashlib" module. Use of
    md5|sha1 is known to have hash collision weaknesses.
    """
    off_by_default = False

    _code = 'DUO130'
    _error_tmpl = 'DUO130 insecure use of "hashlib" module'

    @property
    def kwargs(self):
        pass
