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
from ..fnttbl import FontTable
from .story import BaseStoryPart

class FontTablePart(BaseStoryPart):
    """
    Proxy for the fontTable.xml part containing fontTable definitions for a document.
    """
    @classmethod
    def default(cls, package):
        """
        Return a newly created fontTable part, containing a default set of
        elements.
        """
        partname = PackURI('/word/fontTable.xml')
        content_type = CT.WML_FONT_TABLE
        element = parse_xml(cls._default_font_table_xml())
        return cls(partname, content_type, element, package)

    @property
    def font_table(self):
        return FontTable(self.element, self)

    @classmethod
    def _default_font_table_xml(cls):
        """
        Return a bytestream containing XML for a default fontTable part.
        """
        path = os.path.join(
            os.path.split(__file__)[0], '..', 'templates',
            'default-fontTable.xml'
        )
        with open(path, 'rb') as f:
            xml_bytes = f.read()
        return xml_bytes