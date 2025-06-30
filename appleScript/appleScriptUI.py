import subprocess
import shlex
from typing import List

def run_command(command: List[str]) -> str:
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def show_dialog(message: str, allow_cancel: bool = False) -> bool:
    # Escape double quotes in the message
    safe_message = message.replace('"', '\\"')

    if allow_cancel:
        script = f'display dialog "{safe_message}"'
    else:
        script = f'display dialog "{safe_message}" buttons {{"OK"}} default button "OK"'

    cmd = ["osascript", "-e", script]
    output = run_command(cmd)

    # Check if the user clicked "OK" or canceled
    return "button returned:OK" in output

# Example usage:
if __name__ == "__main__":
    result = show_dialog("Hello, world!")
    print(f"User clicked OK? {result}")