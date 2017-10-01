# -*- coding: utf-8 -*-
import pkg_resources

__author__    = "Bryce Arden"
__copyright__ = "Centaur Technologies"
__date__      = "2017-03-03"

from .io import *
from .reg import *
from .misc import *
from .constants import *
from .jinja2_ext import *

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'

__all__ = (
    io.__all__ +
    reg.__all__ +
    misc.__all__ +
    jinja2_ext.__all__
)

