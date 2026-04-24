#!/usr/bin/env python

import ast

from . import namespace


class MultiNodeVisitor(ast.NodeVisitor):
    def __init__(self, linters, *args, **kwargs):
        self.linters = linters
        self.namespace = None

        super(MultiNodeVisitor, self).__init__(*args, **kwargs)

    def visit(self, node):
        pass
