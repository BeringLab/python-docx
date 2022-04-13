"""
Hyperlink-related proxy types.
"""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
    annotations,
)
from typing import TYPE_CHECKING

from .run import Run
from ..shared import Parented
from ..runcntnr import RunItemContainer

if TYPE_CHECKING:
    from docx.oxml.text.hyperlink import CT_Hyperlink


class Hyperlink(RunItemContainer):
    """
    Proxy object wrapping ``<w:hyperlink>`` element.
    """

    element: CT_Hyperlink

    def __init__(self, h, parent):
        super(Hyperlink, self).__init__(h, parent)
        self._h = self._element = h

    def clear(self):
        """
        Return this same paragraph after removing all its content.
        Paragraph-level formatting, such as style, is preserved.
        """
        self._h.clear_content()
        return self

    @property
    def runs(self):
        return super(Hyperlink, self).runs
