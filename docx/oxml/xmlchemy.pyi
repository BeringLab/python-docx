from __future__ import annotations
from typing import TYPE_CHECKING, List

from docx.compat import Unicode

if TYPE_CHECKING:
    from docx.oxml.ns import NamespacePrefixedTag
    from lxml.etree import _Element

class XmlString(Unicode):
    ...


class MetaOxmlElement(type):
    ...


class BaseAttribute(object):
    ...


class OptionalAttribute(BaseAttribute):
    ...


class RequiredAttribute(BaseAttribute):
    ...

class _BaseChildElement(object):
    ...


class Choice(_BaseChildElement):
    ...


class OneAndOnlyOne(_BaseChildElement):
    ...


class OneOrMore(_BaseChildElement):
    ...


class ZeroOrMore(_BaseChildElement):
    ...


class ZeroOrOne(_BaseChildElement):
    ...


class ZeroOrOneChoice(_BaseChildElement):
    ...
    

class BaseOxmlElement:
    """
    Effective base class for all custom element classes, to add standardized
    behavior to all classes in one place. Actual inheritance is from
    BaseOxmlElement below, needed to manage Python 2-3 metaclass declaration
    compatibility.
    """
    
    def first_child_found_in(self, *tagnames):
        """
        Return the first child found with tag in *tagnames*, or None if
        not found.
        """
        ...

    def insert_element_before(self, elm, *tagnames):
        ...

    def remove_all(self, *tagnames) -> None:
        """
        Remove all child elements whose tagname (e.g. 'a:p') appears in
        *tagnames*.
        """
        ...

    @property
    def xml(self) -> XmlString:
        """
        Return XML string for this element, suitable for testing purposes.
        Pretty printed for readability and without an XML declaration at the
        top.
        """
        ...

    def xpath(self, xpath_str: str) -> List[_Element]:
        """
        Override of ``lxml`` _Element.xpath() method to provide standard Open
        XML namespace mapping (``nsmap``) in centralized location.
        """
        ...

    @property
    def _nsptag(self) -> NamespacePrefixedTag:
        ...