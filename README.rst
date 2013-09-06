cookiecutter-docopt
===================

A python command-line script template, for use with `cookiecutter <https://github.com/audreyr/cookiecutter>`_.

Features
--------

- docopt_ for command-line arguments parsing
- nose_ for testing.
- The ``bundle`` branch has a vendorized version of docopt.

.. _docopt: http://docopt.org/
.. _nose: https://nose.readthedocs.org/en/latest/

To use this template
--------------------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/sloria/cookiecutter-docopt.git

You will be prompted for basic info (your name, script name, etc.) which will be used in the template.

That's all you need to get started.

Don't want to use docopt?
-------------------------

If you prefer not to use docopt for arguments parsing, simply remove the line ``install_requires=['docopt']`` from ``setup.py`` and remove the docopt code in your script.

Next steps
----------
* Create the Github repo for your project
* Add the repo `Travis-CI`_.
* Release your package to the PyPI. Here's a release checklist: https://gist.github.com/sloria/6277657
* Add the repo to `ReadTheDocs`_.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/


License
-------

`MIT Licensed <http://sloria.mit-license.org>`_.