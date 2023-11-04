#!/usr/bin/env python3

from os import getcwd
from typing import Any, Dict, List, Optional

class TrustableRunner:
    def __init__(self, path: Optional[str] = None, configuration: Optional[Dict[str, Any]] = None) -> None:
        self.path = path if path else getcwd()
        self.configuration = configuration if configuration else {}
        # Whether or not the calling application sets an insecure configuration
        # value for os.popen, this library will override it.
        self.configuration['shell'] = True
