__author__ = 'bjarrett'
"""
Provides the base classes for every License system. Implementations will be
in a separate module/package.
"""


class LicenseInterface(object):
    """
    Every license interface will inherit from this class
    Defines a standard interface to all license tools.
    """
    pass


class BinaryLicenseInterface(LicenseInterface):
    """
    Base class for any license tools which need to be interfaces through a binary
    This class will provide some basic subprocess communication.
    """
    pass


