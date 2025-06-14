Fileconfig
==========

|PyPI version| |License| |Supported Python| |Downloads|

|Build| |Codecov|

Fileconfig turns config file sections into instances of your class. Create a
class referring to an **INI file** collecting the arguments for the different
instances to be created. Calling the class with the section name as parameter
will return the instance with the parameters specified in the given section.


Links
-----

- GitHub: https://github.com/xflr6/fileconfig
- PyPI: https://pypi.org/project/fileconfig/
- Issue Tracker: https://github.com/xflr6/fileconfig/issues
- Download: https://pypi.org/project/fileconfig/#files


Installation
------------

This package runs under Python 3.9+, use pip_ to install:

.. code:: bash

    $ pip install fileconfig


Usage
-----

Create as subclass of ``fileconfig.Config`` and set its ``filename`` attribute
to the path of your INI file.

If the filename is relative, it is resolved **relative to the path of the
module** where your class is defined (i.e. *not* relative to the current working
directory if its file not happens do be there).

.. code:: python

    >>> import fileconfig

    >>> class Cfg(fileconfig.Config):
    ...     filename = 'docs/pet-shop.ini'
    ...     def __init__(self, key, **kwargs):
    ...         self.key = key
    ...         self.__dict__.update(kwargs)

On instance creation, the ``__init__`` method will be called with the section
name (``key``) and the keyword parameters from the given section of the
specified file.

Suppose your INI file begins like this:

.. code:: ini

    [parrot]
    species = Norwegian blue
    can_talk = yes
    quantity = 0
    characteristics = beautiful plumage, pining for the fjords

To retrieve this instance, call the class with its section name.

.. code:: python

    >>> c = Cfg('parrot')

    >>> print(c)
    {
      'can_talk': 'yes',
      'characteristics': 'beautiful plumage, pining for the fjords',
      'key': 'parrot',
      'quantity': '0',
      'species': 'Norwegian blue'
    }


Singleton
---------

Only *one* instance will be created, cached and returned for each config file
section (a.k.a. the singleton pattern):

.. code:: python

    >>> Cfg('parrot') is c
    True

The constructor is also *idempotent*:

.. code:: python

    >>> Cfg(c) is c
    True
	
The default ``__repr__`` of instances allows round-trips:

.. code:: python

    >>> c
    __main__.Cfg('parrot')


Aliasing
--------

You can specify a **space-delimited** list of ``aliases`` for each section:

.. code:: ini

    [slug]
    aliases = snail special_offer
    species = slug
    can_talk = no
    quantity = 1

For changing the delimiter, see below.

Aliases map to the *same* instance:

.. code:: python

    >>> s = Cfg('special_offer')

    >>> s
    __main__.Cfg('slug')

    >>> s is Cfg('snail') is Cfg('slug')
    True

Inspect instance ``names`` (key + aliases):

.. code:: python

    >>> s.key
    'slug'

    >>> s.aliases
    ['snail', 'special_offer']

    >>> s.names
    ['slug', 'snail', 'special_offer']


Inheritance
-----------

Config file sections can inherit from another section:

.. code:: ini

    [Polly]
    inherits = parrot
    can_talk = no
    characteristics = dead, totally stiff, ceased to exist

Specified keys override inherited ones:

.. code:: python

    >>> print(Cfg('Polly'))
    {
      'can_talk': 'no',
      'characteristics': 'dead, totally stiff, ceased to exist',
      'inherits': 'parrot',
      'key': 'Polly',
      'quantity': '0',
      'species': 'Norwegian blue'
    }

Sections can inherit from a single section. Multiple or transitive inheritance
is not supported.


Introspection
-------------

Use the class to iterate over the instances from all section:

.. code:: python

    >>> list(Cfg)
    [__main__.Cfg('parrot'), __main__.Cfg('slug'), __main__.Cfg('Polly')]

Print the string representation of all instances:

.. code:: python

    >>> Cfg.pprint_all()  # doctest: +ELLIPSIS
    {
      'can_talk': 'yes',
      'characteristics': 'beautiful plumage, pining for the fjords',
      'key': 'parrot',
    ...

Hints
-----

Apart from the ``key``, ``aliases``, and ``inherits`` parameters, your
``__init__`` method receives the **unprocessed strings** from the config file
parser.

Use the ``__init__`` method to process the other parameters to fit your needs.

.. code:: python

    >>> class Pet(Cfg):
    ...     def __init__(self, can_talk, quantity, characteristics=None, **kwargs):
    ...         self.can_talk = {'yes':True, 'no': False}[can_talk]
    ...         self.quantity = int(quantity)
    ...         if characteristics is not None and characteristics.strip():
    ...             self.characteristics = [c.strip() for c in characteristics.split(',')]
    ...         super().__init__(**kwargs)

    >>> print(Pet('Polly'))
    {
      'can_talk': False,
      'characteristics': ['dead', 'totally stiff', 'ceased to exist'],
      'inherits': 'parrot',
      'key': 'Polly',
      'quantity': 0,
      'species': 'Norwegian blue'
    }

This way, the ``__init__`` method also defines parameters as required or
optional, set their defaults, etc.


Overlay
-------

Sometimes one wants to **combine multiple config files**, e.g. have a default
file included in the package directory, overridden by a user-supplied file in a
different location.

To support this, subclass ``fileconfig.Stacked`` and set the ``filename`` to the
location of the default config.

.. code:: python

    >>> class Settings(fileconfig.Stacked):
    ...     filename = 'docs/pet-shop.ini'

Use the ``add`` method to load an overriding config file on top of that:

.. code:: python

    >>> Settings.add('docs/lumberjack.ini')

If the filename is relative, it is resolved **relative to the path of the
module** where the ``add`` method has been called.

You can access the sections from all files:

.. code:: python

    >>> print(Settings('Bevis'))
    {
      'can_talk': 'yes',
      'characteristics': "sleeps all night, works all day, puts on women's clothing",
      'key': 'Bevis',
      'species': 'human'
    }

As long as they have *different* names:

.. code:: python

    >>> print(Settings('Polly'))
    {
      'can_talk': 'no',
      'characteristics': 'dead, totally stiff, ceased to exist',
      'inherits': 'parrot',
      'key': 'Polly',
      'quantity': '0',
      'species': 'Norwegian blue'
    }

Config files added to the top of the stack mask sections with the same names
from previous files:

.. code:: python

    >>> print(Settings('parrot'))
    {
      'characteristics': 'unsolved problem',
      'key': 'parrot'
    }


Customization
-------------

To use a **different delimiter** for ``aliases`` override the ``_split_aliases``
method on your class. Make it a ``staticmethod`` or ``classmethod`` that takes a
string argument and returns the splitted list.


By default, fileconfig will use ``ConfigParser.SafeConfigParser`` from the
standard library to parse the config file. To use a **different parser**,
override the ``_parser`` attribute in your ``fileconfig.Config`` subclass.


To specify the **encoding** from which the config file should be  decoded by the
config parser, override the ``_encoding`` attribute on your subclass.


Fileconfig raises an error, if the config file is not found. If you want this
**error to pass silently** instead, set the ``_pass_notfound`` attribute on your
subclass to ``True``.


Potential issues
----------------

This package uses ``sys._getframe`` (which is almost the same as
``inspect.currentframe``, see_ docs_). Under IronPython this might require
enabling the ``FullFrames`` option of the interpreter.


License
-------

Fileconfig is distributed under the `MIT license`_.


.. _pip: https://pip.readthedocs.io

.. _see:  https://docs.python.org/2/library/sys.html#sys._getframe
.. _docs: https://docs.python.org/2/library/inspect.html#inspect.currentframe

.. _MIT license: https://opensource.org/licenses/MIT


.. |PyPI version| image:: https://img.shields.io/pypi/v/fileconfig.svg
    :target: https://pypi.org/project/fileconfig/
    :alt: Latest PyPI Version
.. |License| image:: https://img.shields.io/pypi/l/fileconfig.svg
    :target: https://github.com/xflr6/fileconfig/blob/master/LICENSE.txt
    :alt: License
.. |Supported Python| image:: https://img.shields.io/pypi/pyversions/fileconfig.svg
    :target: https://pypi.org/project/fileconfig/
    :alt: Supported Python Versions
.. |Downloads| image:: https://img.shields.io/pypi/dm/csv23.svg
    :target: https://pypistats.org/packages/csv23
    :alt: Monthly downloads

.. |Build| image:: https://github.com/xflr6/fileconfig/actions/workflows/build.yaml/badge.svg?branch=master
    :target: https://github.com/xflr6/fileconfig/actions/workflows/build.yaml?query=branch%3Amaster
    :alt: Build
.. |Codecov| image:: https://codecov.io/gh/xflr6/fileconfig/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/xflr6/fileconfig
    :alt: Codecov
