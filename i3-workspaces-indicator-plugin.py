""" i3-workspaces-indicator-plugin.py
"""
import i3ipc, time
from setproctitle import setproctitle
setproctitle("i3-workspaces-indicator.py")

def get_active_workspaces(i3, workspaces):
    curr_workspaces = []

    for w in workspaces:
        for x in w:
            if x == "num":
                curr_workspaces.append(w[x])

    return curr_workspaces

def main():
    i3 = i3ipc.Connection()

    while True:
        time.sleep(0.025)
        workspaces = i3.get_workspaces()
        curr_workspaces = get_active_workspaces(i3, workspaces)
        ws_string = ""

        for x in curr_workspaces:
            ws_string += str(x) + " "

        print(ws_string)

if __name__ == "__main__":
    main()
