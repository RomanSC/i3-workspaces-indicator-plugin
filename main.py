#!/usr/bin/python3
""" main.py
"""
# import time
import termcolor

try:
    import i3ipc
except ImportError:
    print("Please install i3ipc-python: https://github.com/acrisci/i3ipc-python ")
    exit()

try:
    from setproctitle import setproctitle
    setproctitle("i3-workspaces-indicator")
except ImportError:
    print("Please install setproctitle: https://github.com/dvarrazzo/py-setproctitle ")
    exit()

i3 = i3ipc.Connection() # Listening socket

class Testing:
    def __init__(self):
        self.eventnum = 0 # testing

class Indicator:
    def __init__(self, focused=None, last=None, mode=None):
        self.focused = focused
        self.last = last
        self.mode = mode
        self.workspaces = [{"name": "__wsn__",
                            "focused": "__wsn__",
                            "urgent": "__wsn__"},
                          ]

        self.info = None

    def update_indicator(self, i3):
        ws = i3.get_workspaces()

        for n in range(len(ws)):
            if len(self.workspaces) < len(ws):
                incr = len(ws) - len(self.workspaces)
                for x in range(incr):
                    self.workspaces.append({"name": "__wsn__",
                                            "focused": "__wsn__",
                                            "urgent": "__wsn__"},
                                          )

            for k, v in ws[n].items():
                if k == "name":
                    self.workspaces[n][k] = v

                if k == "focused":
                    self.workspaces[n][k] = v

                if k == "urgent":
                    self.workspaces[n][k] = v

        self.set_info()

    def set_info(self):
        if self.mode != "default" and self.mode != None:
            self.info = str(self.workspaces) + " " + str(self.mode)
        else:
            self.info = str(self.workspaces)

indicator = Indicator()
test = Testing()

def on_workspace_changed(self, obj):
    test.eventnum += 1
    focused = obj.current.name
    last = obj.old.name
    indicator.focused = focused
    indicator.last = last
    indicator.update_indicator(i3)
    print(termcolor.colored(test.eventnum, 'yellow'))
    print(indicator.info)

def on_mode_changed(self, obj):
    test.eventnum += 1
    mode = obj.change
    indicator.mode = mode
    indicator.update_indicator(i3)
    print(termcolor.colored(test.eventnum, 'yellow'))
    print(indicator.info)

i3.on("workspace::focus", on_workspace_changed)
i3.on("mode", on_mode_changed)

i3.main()

