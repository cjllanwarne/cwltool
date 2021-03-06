# Stubs for galaxy.tools.deps.conda_compat (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from conda_build.metadata import MetaData as MetaData

MetaData = ...  # type: Any

class _Memoized:
    func = ...  # type: Any
    cache = ...  # type: Any
    def __init__(self, func) -> None: ...
    def __call__(self, *args): ...

def raw_metadata(recipe_dir): ...

class _MetaData:
    meta = ...  # type: Any
    def __init__(self, input_dir) -> None: ...
    def get_value(self, field, default: Optional[Any] = ...): ...
