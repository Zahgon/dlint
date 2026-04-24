#!/usr/bin/env python

import ast


def decorator_name(decorator):
    pass


def function_has_inlinecallbacks_decorator(function):
    pass


def function_is_empty(function):
    pass


def call_is_returnvalue(call):
    pass


def non_empty_return(_return):
    pass


def walk_callback_same_scope(node, callback):
    # If we change scope, e.g. enter into a new
    # class or function definition, then halt iteration
    pass


def walk_callback(node, callback, predicate=lambda n: True):
    pass


def kwarg_present(call, kwarg_name):
    pass


def kwarg_not_present(call, kwarg_name):
    pass


def kwarg_primitive(call, kwarg_name, primitive):
    pass


def kwarg_false(call, kwarg_name):
    pass


def kwarg_true(call, kwarg_name):
    pass


def kwarg_none(call, kwarg_name):
    pass


def kwarg_str(call, kwarg_name, s):
    pass


def kwarg_module_path(call, kwarg_name, illegal_module_path, namespace):
    pass


def kwarg_module_path_call(call, kwarg_name, illegal_module_path, namespace):
    pass


def kwarg_any(kwarg_functions):
    """Resolve kwarg predicates with short-circuit evaluation. This optimization
    technique means we do not have to evaluate every predicate if one is already
    true.
    """
    pass


def module_path(node):
    """Recursively walk up a series of node attributes.
    E.g. if we have foo.bar.baz, iterate baz -> bar -> foo.
    """
    pass


def module_path_str(node):
    """Return module path as a string instead of a list.
    E.g. "foo.bar.baz" instead of ["foo", "bar", "baz"].
    """
    pass


def same_modules(s1, s2):
    """Compare two module strings where submodules of an illegal
    parent module should also be illegal. I.e. blacklisting 'foo.bar'
    should also make 'foo.bar.baz' illegal.

    The first argument should 'encompass' the second, not the other way
    around. I.e. passing same_modules('foo', 'foo.bar') will return True,
    but same_modules('foo.bar', 'foo') will not.
    """
    pass
