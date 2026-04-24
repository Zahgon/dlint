#!/usr/bin/env python

import abc

from .. import base
from ... import tree


class BadModuleUseLinter(base.BaseLinter, abc.ABC):
    """This abstract base class provides a simple interface for creating new
    lint rules that block bad modules.
    """

    @property
    @abc.abstractmethod
    def illegal_modules(self):
        """Subclasses must implement this property to return a list that
        looks like:

            [
                "module_name1",
                "parent_module_name.module_name2",
            ]
        """

    @property
    def whitelisted_modules(self):
        """Subclasses may implement this property to return a list that
        looks like:

            [
                "parent_module_name.whitelisted_name1",
            ]
        """
        pass

    def visit_Import(self, node):
        pass

    def visit_ImportFrom(self, node):
        pass
