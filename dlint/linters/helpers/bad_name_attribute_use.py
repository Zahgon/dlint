#!/usr/bin/env python

import abc
import ast
import collections

from .. import base
from ... import tree

Assignment = collections.namedtuple(
    'Assignment',
    ['variable', 'module_path', 'lineno', 'col_offset']
)


class BadNameAttributeUseLinter(base.BaseLinter, abc.ABC):
    """This abstract base class provides a simple interface for creating new
    lint rules that block bad attributes on a variable object.
    """

    @property
    @abc.abstractmethod
    def illegal_name_attributes(self):
        """Subclasses must implement this property to return a dictionary
        that looks like:

            {
                "object_attribute": [
                    "parent_module_name1.child_module_name1",
                    "parent_module_name2.child_module_name2",
                ]
            }
        """

    def visit_FunctionDef(self, node):
        pass

    def visit_AsyncFunctionDef(self, node):
        pass
