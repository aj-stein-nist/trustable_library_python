#!/usr/bin/env python3

from trustable_library.logging import StructuredMessageLogger
import unittest
from unittest.mock import patch

class TrustableRunnerLoggingTestSuite(unittest.TestCase):
    def test_config_name(self):
        logger = StructuredMessageLogger(name='example')
        record = logger.info({'message': 'Example'})
        self.assertTrue('example' in record.keys())

    def test_config_level(self):
        logger = StructuredMessageLogger(name='example', level='info')
        logger.debug({'messsage': 'This should not be logged at info level'})
        with patch('trustable_library.logging.logging.debug') as mocked_debug_logger:
            mocked_debug_logger.assert_not_called()

    def test_log_debug(self):
        logger = StructuredMessageLogger(name='example')
        record = logger.debug({'message': 'value'})
        self.assertEqual(record.get('example').get('level'), 'debug')

    def test_log_error(self):
        logger = StructuredMessageLogger(name='example')
        record = logger.error({'message': 'value'})
        self.assertEqual(record.get('example').get('level'), 'error')

    def test_log_exception(self):
        logger = StructuredMessageLogger(name='example')
        try:
            1/0
        except Exception as err:
            record = logger.exception(err)
            self.assertEqual(record.get('example').get('level'), 'exception')
            self.assertEqual(record.get('example').get('data').get('message'), "ZeroDivisionError('division by zero')")
            self.assertEqual(record.get('example').get('data').get('traceback'), 1)

    def test_log_info(self):
        logger = StructuredMessageLogger(name='example')
        record = logger.info({'message': 'value'})
        self.assertEqual(record.get('example').get('level'), 'info')    
