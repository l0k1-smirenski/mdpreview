#!/usr/bin/python3
# Fuck copyright. Here's your stinkin' licence: http://unlicense.org/
# I made this first and the burden of proof is on you.
#
# - l0k1
#
# Contact details for l0k1
# steemit.com - https://steemit.com/@l0k1
# bitmessage - BM-2cXWxTVaXJbNyMxv5tAjNg87xS98hrAg8P
# torchat - xq6xcvqc2vy34qtx
# email - l0k1@null.net

import sys, os, argparse, gi, json, markdown, pyinotify
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit, GObject, Gio

class MDPmain ():
    def __init__(self, window, mdfilename):
        self.window = window
        window_title = self.window_title = self.mdfilename = mdfilename
        if mdfilename == "":
            window_title = "no file opened"
        else:
            window_title = mdfilename
        self.set_up_interface ()
        window.set_title (window_title)

    def set_up_interface (self):
        window = self.window
        self.create_headerbar ()
        window.set_titlebar (self.headerbar)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_default_size (800, 600)
        window.show_all ()

    def create_headerbar (self):
        """
        Creates the navigation headerbar for the interface using the
        Gnome 3 standard design principles
        """
        window = self.window
        self.headerbar = headerbar = Gtk.HeaderBar ()
        headerbar.set_show_close_button (True)
        window.set_titlebar (headerbar)
        # Refresh button - Reloads the current view
        self.refreshbutton = refreshbutton = self.create_button_from_name (
            "view-refresh-symbolic")
        headerbar.pack_start (refreshbutton)
        # Share button - This allows the user to save the file as html
        self.sharebutton = sharebutton = self.create_button_from_name (
            "folder-publicshare-symbolic")
        headerbar.pack_end (sharebutton)

    def create_button_from_name (self, icon_name):
        button = Gtk.Button ()
        button.set_image (
            Gtk.Image.new_from_icon_name (icon_name,
                Gtk.IconSize.BUTTON)
            )
        return button


class mdpreview_gtk3(Gtk.Application):

    def __init__(self):
        """
        This does the initial setup of the Gtk.Application and starts
        the initial opening of the interface
        """
        Gtk.Application.__init__(self,
            application_id="org.ascension.mdpreview-gtk3",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, data=None):
        """
        Parses commandline argument
        Opens initial window, launches interface
        """
        parser = argparse.ArgumentParser(description="Markdown Previewer")
        parser.add_argument ('filename', metavar='FILENAME',
            type=str, nargs="?", default="",
            help="Name of markdown file to display")
        args = parser.parse_args()

        self.window = window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        self.add_window(window)

        MDPmain (window, args.filename)


if __name__ == "__main__":
    app = mdpreview_gtk3()
    app.run(None)
