Fileconfig
==========

|PyPI version| |License|

Fileconfig turns config file sections into Python objects. Create
a class referring to an INI file specifying the arguments for the
different instances to be created. Calling the class with the
section name as parameter will return the instance with the
parameters specified in the config section.


Installation
------------

.. code:: bash

    $ pip install fileconfig


Usage
-----

Create as subclass of ``fileconfig.Config`` and set its ``filename``
attribute to your INI-file name.

If the filename is relative, it is interpreted relative to the path
of the module where your class is defined.

.. code:: python

    >>> import fileconfig

    >>> class Cfg(fileconfig.Config):
    ...     filename = 'examples/pets.ini'
    ...     def __init__(self, key, **kwargs):
    ...         self.key = key
    ...         self.__dict__.update(kwargs)
    ...     def __str__(self):
    ...         items = ('  %r: %r' % (k, v) for k, v in sorted(self.__dict__.iteritems()))
    ...         return '{\n%s\n}' % ',\n'.join(items)

On instance creation, the ``__init__`` method will be called with
the section name (``key``) and the keyword args from the selected
section of the INI-file.

Suppose your INI-file begins like this:

::

    [parrot]
    species = Norwegian blue
    can_talk = yes
    quantity = 0
    characteristics = beatiful plumage, pining for the fjords


To retrieve an instance, call the class with a section name.

.. code:: python

    >>> c = Cfg('parrot')

    >>> print c
    {
      'can_talk': 'yes',
      'characteristics': 'beatiful plumage, pining for the fjords',
      'key': 'parrot',
      'quantity': '0',
      'species': 'Norwegian blue'
    }

Only one instance will be created for each section (a.k.a. the singleton pattern):

.. code:: python

    >>> Cfg('parrot') is c
    True

The default ``__repr__`` of instances is roundtripable:

.. code:: python

    >>> c
    __main__.Cfg('parrot')

The constructor is also idempotent:

.. code:: python

    >>> Cfg(c) is c
    True

Aliasing
--------

You can specify a *space-delimited* list of ``aliases`` for each section:

::

    [slug]
    aliases = snail special_offer
    species = slug
    can_talk = no
    quantity = 1

Aliases map to the *same* instance:

.. code:: python

    >>> s = Cfg('special_offer')

    >>> s
    __main__.Cfg('slug')

    >>> s is Cfg('snail') is Cfg('slug')
    True

Inspect instance ``names``:

.. code:: python

    >>> s.key
    'slug'

    >>> s.aliases
    ['snail', 'special_offer']

    >>> s.names
    ['slug', 'snail', 'special_offer']

To use a different delimiter for ``aliases`` override the ``_split_aliases``
method on your class.

Make it a ``staticmethod`` or ``classmethod`` that takes a single string
argument and returns the splitted list.


Inheritance
-----------

INI-file sections can inherit from another section:

::

    [polly]
    inherits = parrot
    can_talk = no
    characteristics = dead, totally stiff, ceased to exist

Specified keys override inherited ones:

.. code:: python

    >>> print Cfg('polly')
    {
      'can_talk': 'no',
      'characteristics': 'dead, totally stiff, ceased to exist',
      'inherits': 'parrot',
      'key': 'polly',
      'quantity': '0',
      'species': 'Norwegian blue'
    }

Multiple or chained inheritance is not supported.


Introspection
-------------

Use the class to iterate over the instances from all section:

.. code:: python

    >>> list(Cfg)
    [__main__.Cfg('parrot'), __main__.Cfg('slug'), __main__.Cfg('polly')]

Print the string representation of all instances:

.. code:: python

    >>> Cfg.pprint_all()  # doctest: +ELLIPSIS
    {
      'can_talk': 'yes',
      'characteristics': 'beatiful plumage, pining for the fjords',
      'key': 'parrot',
    ...

Hints
-----

Apart from the ``key``, ``aliases``, and ``inherits`` parameters, the
``__init__`` method receives the *unprocessed strings* from the INI-file
parser.

Use the ``__init__`` method to process the other arguments:

.. code:: python

    >>> class Pet(Cfg):
    ...     def __init__(self, can_talk, quantity, characteristics=None, **kwargs):
    ...         self.can_talk = {'yes':True, 'no': False}[can_talk]
    ...         self.quantity = int(quantity)
    ...         if characteristics is not None and characteristics.split():
    ...             self.characteristics = [c.strip() for c in characteristics.split(',')]
    ...         super(Pet, self).__init__(**kwargs)

    >>> print Pet('polly')
    {
      'can_talk': False,
      'characteristics': ['dead', 'totally stiff', 'ceased to exist'],
      'inherits': 'parrot',
      'key': 'polly',
      'quantity': 0,
      'species': 'Norwegian blue'
    }

By default, this package will use ``ConfigParser.SafeConfigParser``
from the standard library to parse the INI-file.

To use a different parser, override the ``_parser`` attribute in your
``fileconfig.Config`` subclass.


License
-------

Fileconfig is distributed under the `MIT license
<http://opensource.org/licenses/MIT>`_.

.. |PyPI version| image:: https://pypip.in/v/fileconfig/badge.png
    :target: https://pypi.python.org/pypi/fileconfig
    :alt: Latest PyPI Version
.. |License| image:: https://pypip.in/license/fileconfig/badge.png
    :target: https://pypi.python.org/pypi/fileconfig
    :alt: License
