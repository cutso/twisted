"""
Interfaces for L{twisted.mail}.
"""

from __future__ import absolute_import, division

from zope.interface import Interface


class IClientAuthentication(Interface):
    def getName():
        """Return an identifier associated with this authentication scheme.

        @rtype: C{bytes}
        """

    def challengeResponse(secret, challenge):
        """Generate a challenge response string"""