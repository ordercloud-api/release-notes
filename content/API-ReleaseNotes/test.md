---
Title: Testing Code Blocks
ApiVersion: 1.1.0
slug: my-code-test
---

.. code-block:: python

   print("Pelican is a static site generator.")


There are two ways to specify the identifier:

    :::python
    print("The triple-colon syntax will *not* show line numbers.")

To display line numbers, use a path-less shebang instead of colons:

    #!python
    print("The path-less shebang syntax *will* show line numbers.")