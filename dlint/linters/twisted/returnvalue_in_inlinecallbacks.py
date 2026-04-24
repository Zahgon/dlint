#!/usr/bin/env python

import ast

from .. import base
from ... import tree


class ReturnValueInInlineCallbacksLinter(base.BaseLinter):
    """This linter looks for returnValue calls that are in a function missing
    a inlineCallbacks decorator.
    """
    off_by_default = False

    _code = 'DUO114'
    _error_tmpl = 'DUO114 "returnValue" in function missing "inlineCallbacks" decorator'

    def visit_FunctionDef(self, node):
        pass
