import subprocess
import sys


def run():
    subprocess.call(
        ["ruff", "check", ".", "--fix"],
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
