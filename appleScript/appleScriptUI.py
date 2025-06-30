import subprocess # For command io

boolean = bool

def runCommand(command: list[str]) -> str:
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def showDialouge(message: str, allow_cancel: boolean = False) -> bool:
    if not allow_cancel:
        cmd = ["osascript", "-e", f'display dialog "{message}"' + 'buttons {"OK"} default button "OK"']
    else:
        cmd = ["osascript", "-e", f'display dialog "{message}"']
    
    if "'" in message or '"' in message:
        raise RuntimeError("Your message may not have single or double quotes in them")

    
    runCommand(cmd)

showDialouge('hi!')