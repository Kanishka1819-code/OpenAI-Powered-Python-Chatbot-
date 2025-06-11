## PyCharm-specific files
.idea/

# Python Virtual Environments
.venv/
env/
venv/
/venv/  # Explicitly ignore a 'venv' directory in the root

# Python bytecode and compiled files
__pycache__/
*.pyc
*.pyo
*.pyd

# Operating System specific files (Windows)
Thumbs.db
desktop.ini
$RECYCLE.BIN/  # Recycle Bin (can appear in project folders if files are deleted there)
System Volume Information/ # System restore points

# Log files and database files (if your project creates them)
*.log
*.sqlite3
db.sqlite3

# Test and coverage artifacts
.coverage
.pytest_cache/

# Sensitive information and local configuration
# THIS IS CRUCIAL FOR YOUR PROJECT TO PREVENT API KEY EXPOSURE
config.py