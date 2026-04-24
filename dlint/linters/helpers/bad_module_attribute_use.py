#!/usr/bin/env python

import abc

from .. import base
from ... import tree


class BadModuleAttributeUseLinter(base.BaseLinter, abc.ABC):
    """This abstract base class provides a simple interface for creating new
    lint rules that block bad attributes within a module.
    """

    @property
    @abc.abstractmethod
    def illegal_module_attributes(self):
        """Subclasses must implement this property to return a dictionary
        that looks like:

            {
                "module_name": [
                    "attribute_name1",
                    "attribute_name2",
                ]
            }
        """

    def __init__(self, *args, **kwargs):
        self.bad_nodes = []

        super(BadModuleAttributeUseLinter, self).__init__(*args, **kwargs)

    def get_results(self):

        pass

    def visit_Name(self, node):
        pass

    def visit_Attribute(self, node):
        pass
