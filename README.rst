######################################
Advent of Code 2022 – Python Solutions
######################################

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

Solutions for `Advent of Code <https://adventofcode.com>`_ 2022 in pure Python 3.10. 🎄
No dependencies, no speed hacks:
pythonic code with just the standard library. 👍
Well, unless I'm too annoyed by the challenge of the day. 🤪

Feel free to take a look around and find inspiration. 🤔

Usage 🎅🤶
--------

The module is directly executable from the CLI.
Daily input data is searched inside `./data/` named
`dayXY.txt` or `dayXY_ex.txt` for examples.

.. code:: bash

    # run day 3
    python3 -m aoc2022 3
    # run day 4 with example code
    python3 -m aoc2022 4 -e
    # run days 1,2,3,4,5
    python3 -m aoc2022 1 2 3 4 5
    # show available options
    python3 -m aoc2022 -h

Use the ``--data`` switch to point to a custom data location.

Running with ``aocd``
^^^^^^^^^^^^^^^^^^^^^

.. note::

    Oh, oh, no! 🎅
    This does not work yet – stay tuned! 👀

The module can be installed to allow running it with
`aocd <https://github.com/wimglenn/advent-of-code-data>`_.
This lets you compare its solutions against your own and others.

.. code:: bash

    # install the current directory (this repo) and aocd
    pip install . advent-of-code-data
    # export your session cookie
    export AOC_SESSION=612b7c47656....
    # run year 2021 solutions
    aoc -y 2021
