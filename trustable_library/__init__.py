#!/usr/bin/env python3

from .logging import StructuredMessageLogger
import logging
from os import getcwd
import subprocess
from typing import Any, Dict, List, Optional, Tuple, Union

class TrustableRunner:
    def __init__(self, path: Optional[str] = None, configuration: Optional[Dict[str, Any]] = None) -> None:
        self.path = path if path else getcwd()
        self.configuration = configuration if configuration else {}
        # Whether or not the calling application sets an insecure configuration
        # value for subprocess.run(), this library will override it.
        self.configuration['shell'] = True
        self.configuration['stderr'] = subprocess.PIPE
        self.configuration['stdout'] = subprocess.PIPE
        self.configuration['text'] = True
        self.logger = StructuredMessageLogger(name=__name__, level='info')

    def run(self, cmd: Union[str, List[str]]) -> Tuple[int, str, str]:
        """Run commands with opinionated defaults for more secure command
        execution. The command is run with popen configuration provided by the
        calling application and defaults overriden by the library.

        :param cmd: A list of strings to compose the command, parameters, and
        its arguments.
        :returns: the return code, standard output, and standard error in that
        order.
        :rtype: tuple
        """
        try:
            _cmd = ' '.join(cmd) if isinstance(cmd, list) else cmd
            self.logger.debug({'message': 'Setting up command', 'cmd': ' '.join(cmd)})
            result = subprocess.run(_cmd, **self.configuration)
            if result.returncode == 0:
                self.logger.debug({
                    'message': 'Command ok, no error',
                    'return_code': result.returncode,
                    'stdout': result.stdout,
                    'stderr': result.stderr
                })
            else:
                self.logger.error({
                    'message': 'Command failed, error',
                    'return_code': result.returncode,
                    'stdout': result.stdout,
                    'stderr': result.stderr
                })                
            return result.returncode, result.stdout, result.stderr          
        except Exception as err:
            self.logger.exception(err)
            raise err
