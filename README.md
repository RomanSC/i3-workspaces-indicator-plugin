## i3 workspaces indicator plugin

A work in progress. Ultimately stalled until I either pick up C/C++ or xfce4 gets gobject introspection for Python bindings. (or until I find a workaround, which is possible.)

Licensed as WTFPL, so you can do wtf you want with this code. This Python script listens to a few i3 events on a socket and produces a table for all active workspaces as well as their status, specifically focused and urgent mode. The script also listens for the binding mode, if you enter resize mode in i3 the script is updated with that information as well. I encourage anyone to use this if they want for plugins in various Linux desktops that allow for i3 to be used as the window manager and that happen to have Python bindings.

What's not implemented is the GTK or Qt aspects that would make this a plugin. So for now it's TODO.

The goal is to write a plugin for the xfce4 desktop that displays the status of your i3 workspaces and binding mode just like the default, only allowing for transparency and custom color options.

# Dependencies:
+ <a href="https://www.python.org/">Python3</a>
+ <a href="https://github.com/i3/i3">i3</a>
+ <a href="https://github.com/i3/i3/search?utf8=%E2%9C%93&q=i3ipc-python&type=">i3ipc-python</a>
+ <a href="https://github.com/dvarrazzo/py-setproctitle">setproctitle</a>

# Issue:

Awaiting patch or workaround:
<br><a href="https://bugzilla.xfce.org/show_bug.cgi?id=12159">https://bugzilla.xfce.org/show_bug.cgi?id=12159</a></br>
