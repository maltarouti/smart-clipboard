import sys
import signal

from listener import Listener


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(Listener())
