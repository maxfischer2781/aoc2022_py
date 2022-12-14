######################################
Advent of Code 2022 â Python Solutions
######################################

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

Solutions for `Advent of Code <https://adventofcode.com>`_ 2022 in pure Python 3.10. ð
No dependencies, no speed hacks:
pythonic code with just the standard library. ð
Well, unless I'm too annoyed by the challenge of the day. ðĪŠ

Most of the code is written the way I would write $DAYJOB code:
generic, reusable, modular and aimed at data streams. ðĒ
In other words, it is somewhat over-engineered and could be reduced
for just the specific task of each day. âïļ
Feel free to take a look around and find inspiration. ðĪ

Usage ððĪķ
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

    *Oh, oh, no! ð This does not work yet â stay tuned! ð*

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
