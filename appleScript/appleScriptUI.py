import subprocess # For command io

def runCommand(command: str) -> str:
    """Runs a command and returns the result of it, assuming it has no errors"""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


print(runCommand('whoami'))
