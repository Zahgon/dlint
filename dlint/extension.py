#!/usr/bin/env python

import functools
import importlib
import inspect
import pkgutil
import optparse
import sys

from flake8 import style_guide

import dlint


class Flake8Extension(object):
    name = dlint.__name__
    version = dlint.__version__
    options = None

    def __init__(self, tree, filename):
        self.tree = tree
        self.filename = filename

    @classmethod
    def add_options(cls, parser):
        pass

    @classmethod
    def parse_options(cls, options):
        pass

    @classmethod
    @functools.lru_cache()
    def get_plugin_linter_classes(cls):
        pass

    @classmethod
    def get_linter_classes(cls):
        pass

    def run(self):
        pass
