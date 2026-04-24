#!/usr/bin/env python

from .helpers import bad_module_attribute_use


class BadOneLoginModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of OneLogin SAML module attributes.
    These attributes may indicate weaknesses in SAML authentication support.
    """
    off_by_default = False

    _code = 'DUO129'
    _error_tmpl = 'DUO129 insecure "OneLogin" SAML attribute use'

    @property
    def illegal_module_attributes(self):
        pass
