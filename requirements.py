# Installs the all the modules from requirements.txt

# Pip install all the modules from requirements.txt
from ssl import AlertDescription
import subprocess
import sys


def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        AlertDescription(text="Failed to install requirements", title="Error", button="OK")
        sys.exit(1)
    