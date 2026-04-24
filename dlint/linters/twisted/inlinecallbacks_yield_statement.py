#!/usr/bin/env python

import ast

from .. import base
from ... import tree


class InlineCallbacksYieldStatementLinter(base.BaseLinter):
    """This linter looks for inlineCallbacks functions that are missing a
    yield statement. The presence of a yield statement turns a normal function
    into a generator. The inlineCallback generator depends on this behavior,
    so let's check for cases where it's missing.
    """
    off_by_default = False

    _code = 'DUO113'
    _error_tmpl = 'DUO113 "inlineCallbacks" function missing "yield" statement'

    def visit_FunctionDef(self, node):
        pass
