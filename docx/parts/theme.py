"""
Theme part objects
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

import os

from ..opc.constants import CONTENT_TYPE as CT
from ..opc.packuri import PackURI
from ..oxml import parse_xml
from ..theme import Theme
from .story import BaseStoryPart

class ThemePart(BaseStoryPart):
    """
    Proxy for the theme.xml part containing theme definitions for a document.
    """
    @classmethod
    def default(cls, package):
        """
        Return a newly created theme part, containing a default set of
        elements.
        """
        partname = PackURI('/word/theme/theme1.xml')
        content_type = CT.OFC_THEME
        element = parse_xml(cls._default_theme_xml())
        return cls(partname, content_type, element, package)

    @property
    def theme(self):
        return Theme(self.element, self)

    @classmethod
    def _default_theme_xml(cls):
        """
        Return a bytestream containing XML for a default theme part.
        """
        path = os.path.join(
            os.path.split(__file__)[0], '..', 'templates',
            'default-theme.xml'
        )
        with open(path, 'rb') as f:
            xml_bytes = f.read()
        return xml_bytes