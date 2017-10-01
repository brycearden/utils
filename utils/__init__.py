# -*- coding: utf-8 -*-
import pkg_resources

__author__    = "Bryce Arden"
__copyright__ = "Centaur Technologies"
__date__      = "2017-03-03"

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'

