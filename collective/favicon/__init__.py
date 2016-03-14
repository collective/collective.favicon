# -*- extra stuff goes here -*-

from zope.i18nmessageid import MessageFactory
FaviconMessageFactory = MessageFactory('collective.favicon')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
