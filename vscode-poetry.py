#!/usr/bin/env python3

# See https://github.com/microsoft/vscode-python/issues/8372
import json
import subprocess
from pathlib import Path

venv_path = subprocess.check_output("poetry env info --path", shell=True)
venv_path = venv_path.decode("UTF-8")

print(f"venv_path = {venv_path}")

settings = dict()

Path(".vscode").mkdir(parents=True, exist_ok=True)

if Path(".vscode/settings.json").exists():
    with open(".vscode/settings.json", "r") as f:
        settings = json.load(f)
        print(f"old settings={settings}")
else:
    Path(".vscode/settings.json").touch()

settings["python.pythonPath"] = venv_path
# Add the settings for linting
settings["python.linting.enabled"] = True
settings["python.linting.flake8Enabled"] = True
# Settings for formatting
settings["editor.formatOnSave"] = True
settings["editor.formatOnPaste"] = False
settings["editor.formatOnType"] = False
settings["editor.formatOnSaveTimeout"] = 3000
settings["python.formatting.provider"] = "black"

with open(".vscode/settings.json", "w") as f:
    json.dump(settings, f, sort_keys=True, indent=4)

print(f"new settings: {json.dumps(settings, sort_keys=True, indent=4)}")
abs_path = str(Path(".vscode/settings.json").resolve())
print(f"written to: {abs_path}")
