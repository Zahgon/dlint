#!/usr/bin/env python

import ast
import collections

from .. import namespace

Flake8Result = collections.namedtuple(
    'Flake8Result',
    ['lineno', 'col_offset', 'message']
)


class BaseLinter(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        self.results = []
        self.namespace = None

        super(BaseLinter, self).__init__(*args, **kwargs)

    def get_results(self):

        pass

    def visit(self, node):
        pass
