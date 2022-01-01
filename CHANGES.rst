Changelog
=========


Version 0.6.1 (in development)
------------------------------

Drop Python 3.6 support.


Version 0.6
-----------

Drop Python 2 support.

Drop Python 3.5 support and tag Python 3.9 and 3.10 support.


Version 0.5.10
--------------

Tag Python 3.8 support.


Version 0.5.9
-------------

Drop Python 3.4 support.


Version 0.5.8
-------------

Tag Python 3.7 support, add simple ``tox`` config.


Version 0.5.7
-------------

Add ``python_requires``, update package scaffolding.

Increase test coverage.


Version 0.5.6
-------------

Drop Python 3.3 support.

Include license file in wheel.


Version 0.5.5
-------------

Fix ``ConfigParser.readfp()`` ``DeprecationWarning`` under Python 3.


Version 0.5.4
-------------

Fix failing config filepath tests under Linux.


Version 0.5.3
-------------

Port tests from ``nose``/``unittest`` to ``pytest``, add Travis CI and coveralls.

Update meta data, tag Python 3.5/3.6 support.


Version 0.5.2
-------------

Documentation fix.


Version 0.5.1
-------------

Added config filename normalization.

Fixed names property with instances lacking aliases.


Version 0.5
-----------

Added Python 3.3+ support.

Documented ``sys._getframe`` dependency.


Version 0.4.1
-------------

Simplified inspection in ``caller_path``.

Fixed some typos.


Version 0.4
-----------

Add custom encoding support.

Make available underlying stack attribute on ``Stacked``.

Add ``caller_steps`` parameter to add method of ``Stacked``.


Version 0.3.1
-------------

Improved documentation.


Version 0.3
-----------

Replaced ``Stack`` by refactored ``Stacked`` config.


Version 0.2
-----------

Added default ``__init__`` and ``__str__`` methods.

Save ``Config`` filename as absolute path.

Raise an error if the file is not found.

Support direct usage from then interactive shell.

Add ``Stack`` as experimental feature.


Version 0.1
-----------

First public release.
