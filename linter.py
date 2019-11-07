from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter
import sys

class Ghcid(Linter):
    regex = r'\"start\":\[(?P<line>\d+),(?P<col>\d+)\],.*\"message\":\"(?P<message>.*)\"'
    multiline = True
    defaults = {
        'selector': 'source.haskell'
    }

    def cmd(self):
      if sys.platform.startswith("win32"):
        return ["cmd.exe", "/c", "type", "%TEMP%\\ghcid.json"]
      else:
        return ["cat", "/tmp/ghcid.json"]

    def split_match(self, match):
      match, line, col, error, warning, message, near = super().split_match(match)
      return match, line, col, error, warning, message, near  
