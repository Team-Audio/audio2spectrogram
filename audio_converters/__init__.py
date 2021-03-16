from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import iter_modules
from . import base
from typing import Dict, Type

# contains available converters sorted by what input type they accept
available: Dict[str, Type[base.Converter]] = {}


# get directory of this package
package_dir = Path(__file__).resolve().parent

# iterate all modules in this package
for (_, module_name, _) in iter_modules([package_dir]):

    # import the module
    module = import_module(f"{__name__}.{module_name}")

    # iterate the module
    for attribute_name in dir(module):

        # get the attribute by name
        attribute = getattr(module, attribute_name)

        # check if the attribute is a class
        if not isclass(attribute):
            continue

        # check if the attribute is base.Converter, in which case we do not want add it
        if attribute is base.Converter:
            continue

        # check if the attribute inherits from base.Converter
        if issubclass(attribute, base.Converter):
            # add it to the globals list so that it can be imported via from <pkg> import *
            globals()[attribute_name] = attribute

            # add it to the available list, we need to instantiate it briefly to do this, so make sure
            # that the converters are lightweight
            available[attribute().responsibility] = attribute
