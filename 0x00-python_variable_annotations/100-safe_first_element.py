#!/usr/bin/env python3
""" first element of a sequence """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ first element """
    if lst:
        return lst[0]
    else:
        return None
