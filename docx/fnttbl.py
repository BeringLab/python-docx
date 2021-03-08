from __future__ import absolute_import, division, print_function, unicode_literals

from docx.shared import ElementProxy

class FontTable(ElementProxy):
    """
    FontTable object, container for all objects in the font table part
    """
    def __init__(self, element, part):
        super(FontTable, self).__init__(element)
        self._part = part