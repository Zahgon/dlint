#!/usr/bin/env python

import ast
import copy

from functools import lru_cache
from . import util


class Namespace(object):
    def __init__(self, imports, from_imports):
        self.imports = imports
        self.from_imports = from_imports

    @classmethod
    def from_module_node(cls, module_node):
        # For now only add top-level, module imports. Let's avoid the rabbit
        # hole of looking at things like function and class-scope imports and
        # conditional imports in 'if' or 'try' statements
        pass

    @lru_cache(maxsize=1024)
    def name_imported(self, name):
        pass

    def asname_to_name(self, asname):
        pass

    @lru_cache(maxsize=1024)
    def illegal_module_imported(self, module_path, illegal_module_path):
        pass
