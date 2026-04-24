#!/usr/bin/env python

from .helpers import bad_module_attribute_use


class BadXmlsecModuleAttributeUseLinter(bad_module_attribute_use.BadModuleAttributeUseLinter):
    """This linter looks for unsafe use of xmlsec module attributes.
    These attributes may indicate weaknesses in cryptographic operations.
    """
    off_by_default = False

    _code = 'DUO136'
    _error_tmpl = 'DUO136 insecure "xmlsec" attribute use'

    @property
    def illegal_module_attributes(self):
        pass
