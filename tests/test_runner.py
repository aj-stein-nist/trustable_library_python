#!/usr/bin/env python3

from trustable_library import TrustableRunner
import unittest

class TrustableRunnerTestSuite(unittest.TestCase):
    def test_valid_command_returns(self):
        runner = TrustableRunner()
        result = runner.run(['whoami'])
        self.assertEqual(result, (0, "me\n", ''))

    def test_valid_command_invalid_args_errors(self):
        runner = TrustableRunner()
        result = runner.run(['ls', '/bad/example'])
        self.assertEqual(
            result, 
            (2, '', "ls: cannot access '/bad/example': No such file or directory\n")
        )

    def test_nonexistent_command_errors(self):
        runner = TrustableRunner()
        result = runner.run(['no_such_command'])
        self.assertEqual(
            result,
            (127, '', '/bin/sh: 1: no_such_command: not found\n')
        )
