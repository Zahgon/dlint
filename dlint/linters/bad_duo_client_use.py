#!/usr/bin/env python

from .helpers import bad_kwarg_use

from .. import tree


class BadDuoClientUseLinter(bad_kwarg_use.BadKwargUseLinter):
    """This linter looks for unsafe HTTP use when using the "duo_client" module.
    """
    off_by_default = False

    _code = 'DUO127'
    _error_tmpl = 'DUO127 use of "ca_certs=HTTP|DISABLE" is insecure in "duo_client" module'

    @property
    def kwargs(self):
        pass
