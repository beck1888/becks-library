import sys
import tty
import termios

def get_masked_input(prompt="Password: ", mask_char="•"):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    result = ""

    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch in ('\n', '\r'):
                sys.stdout.write('\n')
                break
            elif ch == '\x7f':  # backspace
                if result:
                    result = result[:-1]
                    sys.stdout.write('\b \b')
            else:
                result += ch
                sys.stdout.write(mask_char)
            sys.stdout.flush()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return result