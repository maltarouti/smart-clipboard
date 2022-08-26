import sys
import signal

from listener import Listener


if __name__ == "__main__":
    # Activate CTRL + C and Deactivate CTRL + Z
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)

    sys.exit(Listener())
