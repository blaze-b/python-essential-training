try:
    import msvcrt

    def get_key():
        return msvcrt.getch()
except ImportError:
    import sys
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch
