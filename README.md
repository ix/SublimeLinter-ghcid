SublimeLinter-ghcid
===================

A basic linter for use with ghcid's JSON output mode.

For best results, invoke ghcid like this:

`ghcid --command="stack ghci --ghc-options \"-fno-diagnostics-show-caret\"" --outputfile=/tmp/ghcid.json`