mdpreview-gtk3
==============

**NOTE** This is a fork that l0k1-smirenski is adopting in order to fork 
to Gtk+-3.0 as part of another project, called 'steemportal' - as this 
codebase directly relates to this project due to the fact that Steem 
uses markdown, and steemportal uses gtk3 and python 3.

A simple GTK-based Markdown previewer, designed to be used with an external
editor.

There are many Markdown previewers. `mdpreview` has been written to be as **easy
to use with an external editor** as possible. Just open `mdpreview`, open your
editor and start editing. `mdpreview` will automatically reload when the file
changes, detect when you're viewing the bottom of the document and
automatically scroll down on new content, and more.

It includes themes that closely resemble *github*, and *bitbucket*. 

![](https://raw.githubusercontent.com/fboender/mdpreview/master/mdpreview.png)

*Screenshot: mdpreview running the `solarized` theme.*

Features
--------

* Written in Python, so runs nearly everywhere.
* Remembers window state between invocations.
* Auto-reload that preserves scroll position.
* Theme support (github, bitbucket, solarized, whiteonblack)
* Vi motion keys (`j`, `k`, `G`, `g`)
* Append detection. If the end of the document is being viewed and new contents
  is appended, mdpreview automatically scrolls to the bottom.
* Optional *Keep-on-top* window hint, to keep the preview always on top.

### Todos

* Images are not refreshed on reload.


Installation
------------

Requirements:

* python-webkit
* python-markdown
* pyinotify


On Debian / Ubuntu systems, to install the dependencies (they're most probably
already installed):

    $ sudo apt-get install python-webkit python-markdown python-pyinotify

You can run `mdpreview` directly from the git repository:

    $ git clone https://github.com/fboender/mdpreview.git
    $ cd mdpreview
    $ ./mdpreview README.md

If you wish to install it on your system, run the `install.sh` script:

    $ sudo install.sh

This will also put an `uninstall.sh` script in `/usr/local/lib/mdpreview/uninstall.sh`.

Usage
-----

Basic usage:

    Usage: ./mdpreview <file.md>

    Options:
      -h, --help            show this help message and exit
      -k, --keep-on-top     Keep window on top
      -t THEME, --theme=THEME
                            Theme (name or full path to .html). Default: github

### Examples

Using a theme:

    mdpreview -t bitbucket ./README.md

Specify a full path to a theme:

    mdpreview -t ~/.mdpreview/mytheme.html ./README.md

### Keybindings

* **`r`**: Reload
* **`Esc`**, **`q`**: Quit
* **`j`**, **`k`**: Scroll down / up (vi keybindings)
* **`G`**, **`g`**: Scroll to bottom / top (vi keybindings)
* **`s`**: Save to HTML.

### Auto-reloading

mdpreview automatically reloads the Markdown file if it's been changed. It
preserves the scrolling position during reloading.

Licensing
---------

mdpreview is licensed under the GPLv3:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For the full license, see the LICENSE file.

