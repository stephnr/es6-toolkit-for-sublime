import os
import sys
from .toolkit import *

__version__ = '1.1.0'


class ToolkitCompileFileCommand(compiler.ES6_Toolkit_Compile_File):
    def run(self):
        self.execute()


class ToolkitDumpJsCommand(compiler.ES6_Toolkit_Dump_JS):
    def run(self, edit, compiled_js):
        self.execute(edit, compiled_js)
