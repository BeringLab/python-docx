from __future__ import absolute_import, division, print_function, unicode_literals

from docx.shared import ElementProxy

class Theme(ElementProxy):
    """
    Theme object, container for all objects in the theme part
    """
    def __init__(self, element, part):
        super(Theme, self).__init__(element)
        self._part = part