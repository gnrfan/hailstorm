Hailstorm
=========

Hailstorm is an open source Python templating library extracted from Facebook's Tornado, 
the non-blocking web server available at http://www.tornadoweb.org/

The key feature of Hailstorm is not restricting the kind of expressions that can be used in
the statements within the template files. It's just Python so you don't need filters or template
tags like in Jinja2 or Django templates. You just pass the objects you intend to use to the template 
and you're good to go.

Hailstorm is licensed under the Apache Licence, Version 2.0
(http://www.apache.org/licenses/LICENSE-2.0.html).

Usage
=====

Basic usage looks like::

    t = template.Template("<html>{{ myvalue }}</html>")
    print t.generate(myvalue="XXX")

Loader is a class that loads templates from a root directory and caches
the compiled templates::

    loader = template.Loader("/home/gnrfan")
    print loader.load("test.html").generate(myvalue="XXX")

We compile all templates to raw Python. Error-reporting is currently... uh,
interesting. Syntax for the templates::

    ### base.html
    <html>
      <head>
        <title>{% block title %}Default title{% end %}</title>
      </head>
      <body>
        <ul>
          {% for student in students %}
            {% block student %}
              <li>{{ escape(student.name) }}</li>
            {% end %}
          {% end %}
        </ul>
      </body>
    </html>

    ### bold.html
    {% extends "base.html" %}

    {% block title %}A bolder title{% end %}

    {% block student %}
      <li><span style="bold">{{ escape(student.name) }}</span></li>
    {% end %}

Unlike most other template systems, we do not put any restrictions on the
expressions you can include in your statements. if and for blocks get
translated exactly into Python, you can do complex expressions like:

    {% for student in [p for p in people if p.student and p.age > 23] %}
      <li>{{ escape(student.name) }}</li>
    {% end %}

Translating directly to Python means you can apply functions to expressions
easily, like the escape() function in the examples above. You can pass
functions in to your template just like any other variable::

    ### Python code
    def add(x, y):
        return x + y
    template.execute(add=add)

    ### The template
    {{ add(1, 2) }}

We provide the functions escape(), url_escape(), json_encode(), and squeeze()
to all templates by default.

Syntax Reference
----------------

Template expressions are surrounded by double curly braces: ``{{ ... }}``.
The contents may be any python expression, which will be escaped according
to the current autoescape setting and inserted into the output.  Other
template directives use ``{% %}``.  These tags may be escaped as ``{{!``
and ``{%!`` if you need to include a literal ``{{`` or ``{%`` in the output.

To comment out a section so that it is omitted from the output, surround it
with ``{# ... #}``.

``{% apply *function* %}...{% end %}``
    Applies a function to the output of all template code between ``apply``
    and ``end``::

        {% apply linkify %}{{name}} said: {{message}}{% end %}

    Note that as an implementation detail apply blocks are implemented
    as nested functions and thus may interact strangely with variables
    set via ``{% set %}``, or the use of ``{% break %}`` or ``{% continue %}``
    within loops.

``{% autoescape *function* %}``
    Sets the autoescape mode for the current file.  This does not affect
    other files, even those referenced by ``{% include %}``.  Note that
    autoescaping can also be configured globally, at the `Application`
    or `Loader`.::

        {% autoescape xhtml_escape %}
        {% autoescape None %}

``{% block *name* %}...{% end %}``
    Indicates a named, replaceable block for use with ``{% extends %}``.
    Blocks in the parent template will be replaced with the contents of
    the same-named block in a child template.::

        <!-- base.html -->
        <title>{% block title %}Default title{% end %}</title>

        <!-- mypage.html -->
        {% extends "base.html" %}
        {% block title %}My page title{% end %}

``{% comment ... %}``
    A comment which will be removed from the template output.  Note that
    there is no ``{% end %}`` tag; the comment goes from the word ``comment``
    to the closing ``%}`` tag.

``{% extends *filename* %}``
    Inherit from another template.  Templates that use ``extends`` should
    contain one or more ``block`` tags to replace content from the parent
    template.  Anything in the child template not contained in a ``block``
    tag will be ignored.  For an example, see the ``{% block %}`` tag.

``{% for *var* in *expr* %}...{% end %}``
    Same as the python ``for`` statement.  ``{% break %}`` and
    ``{% continue %}`` may be used inside the loop.

``{% from *x* import *y* %}``
    Same as the python ``import`` statement.

``{% if *condition* %}...{% elif *condition* %}...{% else %}...{% end %}``
    Conditional statement - outputs the first section whose condition is
    true.  (The ``elif`` and ``else`` sections are optional)

``{% import *module* %}``
    Same as the python ``import`` statement.

``{% include *filename* %}``
    Includes another template file.  The included file can see all the local
    variables as if it were copied directly to the point of the ``include``
    directive (the ``{% autoescape %}`` directive is an exception).
    Alternately, ``{% module Template(filename, **kwargs) %}`` may be used
    to include another template with an isolated namespace.

``{% module *expr* %}``
    Renders a `~tornado.web.UIModule`.  The output of the ``UIModule`` is
    not escaped::

        {% module Template("foo.html", arg=42) %}

``{% raw *expr* %}``
    Outputs the result of the given expression without autoescaping.

``{% set *x* = *y* %}``
    Sets a local variable.

``{% try %}...{% except %}...{% finally %}...{% else %}...{% end %}``
    Same as the python ``try`` statement.

``{% while *condition* %}... {% end %}``
    Same as the python ``while`` statement.  ``{% break %}`` and
    ``{% continue %}`` may be used inside the loop.


On the "Hailstorm" name
=======================

""" I guess the ideal name was 'Tempest' but there already was a package named like that in PyPi so 
I went with this name since one of my new favorite hard rock bands is Halestorm! """ -Antonio Ognio

(c) 2013, Bit Zeppelin S.A.C - Lima, Peru.