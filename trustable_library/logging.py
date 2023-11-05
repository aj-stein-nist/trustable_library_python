#!/usr/bin/env python3

import json
import logging
from traceback import format_tb
from typing import Any, Dict, Optional

class StructuredMessageLogger(object):
    def __init__(self, name: Optional[str] = None, level: Optional[str] = 'info', configuration: Optional[Dict[str, Any]] = {}) -> None:
        self.configuration = configuration
        self.name = name if name else 'root'
        self.configuration['level'] = getattr(logging, level.upper())
        self.configuration['format'] = '%(message)s'
        logging.basicConfig(**configuration)
        self.logger = logging.getLogger(self.name)

    def debug(self, data: Dict[str, Any] = {}) -> Dict[str, Any]:
        record = {
            self.name: {
                'level': 'debug',
                'data': data
            }
        }
        self.logger.debug(json.dumps(record))
        return record

    def error(self, data: Dict[str, Any] = {}) -> Dict[str, Any]:
        record = {
            self.name: {
                'level': 'error',
                'data': data
            }
        }
        self.logger.error(json.dumps(record))
        return record

    def exception(self, error: Exception) -> Dict[str, Any]:
        record = {
            self.name: {
                'level': 'exception',
                'data': {
                    'message': error.__repr__(),
                    'traceback': format_tb(error.__traceback__)
                }
            }
        }
        self.logger.exception(json.dumps(record))
        return record

    def info(self, data: Optional[Dict[str, Any]] = {}) -> Dict[str, Any]:
        record = {
            self.name: {
                'level': 'info',
                'data': data
            }
        }
        self.logger.info(json.dumps(record))
        return record
