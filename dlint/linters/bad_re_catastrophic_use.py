#!/usr/bin/env python

import ast

from .helpers import bad_module_attribute_use
from . import base
from .. import redos


class BadReCatastrophicUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for regular expression catastrophic backtracking in
    the re module. Catastrophic backtracking can cause denial-of-service.

    Some people, when confronted with a problem, think
    "I know, I'll use regular expressions." Now they have two problems.
        * Jamie Zawinski, 1997: http://regex.info/blog/2006-09-15/247
    """
    off_by_default = False

    _code = 'DUO138'
    _error_tmpl = 'DUO138 catastrophic "re" usage - denial-of-service possible'

    @property
    def illegal_module_attributes(self):
        pass

    def __init__(self, *args, **kwargs):
        self.calls = {}

        super(BadReCatastrophicUseLinter, self).__init__(*args, **kwargs)

    def visit_Call(self, node):
        pass

    def get_results(self):
        pass
