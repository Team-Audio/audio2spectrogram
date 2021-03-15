from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import iter_modules
from . import base
from typing import Dict, Type

available: Dict[str, Type[base.Converter]] = {}

package_dir = Path(__file__).resolve().parent

for (_, module_name, _) in iter_modules([package_dir]):
    module = import_module(f"{__name__}.{module_name}")

    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if attribute is base.Converter:
            continue

        if not isclass(attribute):
            continue

        if issubclass(attribute, base.Converter):
            globals()[attribute_name] = attribute
            available[attribute().responsibility] = attribute
