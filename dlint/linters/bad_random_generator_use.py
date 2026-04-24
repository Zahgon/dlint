#!/usr/bin/env python

import ast

from . import base


class BadRandomGeneratorUseLinter(base.BaseLinter):
    """This linter looks for any use of the Python "random" module EXCEPT
    SystemRandom.

    By default Python uses a Mersenne Twister[1] implementation to generate
    random values, and this is not suitable for cryptographic purposes.
    SystemRandom uses os.urandom to get random data, which is generally a
    much better choice.

    [1] https://en.wikipedia.org/wiki/Mersenne_twister
    """
    off_by_default = False

    _code = 'DUO102'
    _error_tmpl = 'DUO102 insecure use of "random" module, prefer "random.SystemRandom"'

    def visit_Attribute(self, node):
        pass

    def visit_ImportFrom(self, node):
        pass
