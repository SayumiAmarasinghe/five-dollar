#!/usr/bin/env bash
set -euo pipefail

# --- Configuration based on your folder structure ---
# Using the path observed in your screenshot: PythonApp
APP_DIR="$HOME/PythonApp"
APP_FILE="five-dollar-app.py"
# The path to the python binary inside your virtual environment
PY="$APP_DIR/.venv/bin/python"

cd "$APP_DIR"

# 1. Pull latest code (Ensures your EC2 is synced with GitHub)
echo "Syncing code with origin/main..."
git fetch --all
git reset --hard origin/main

# 2. Ensure virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    # Using python3.12 as seen in your reference image
    python3.12 -m venv .venv
fi

# 3. Install/update dependencies using your requirements.txt
echo "Updating dependencies..."
"$PY" -m pip install -U pip
"$PY" -m pip install -r requirements.txt

# 4. Stop previous process (if any)
echo "Stopping old process..."
pkill -f "$PY $APP_FILE" || true

# 5. Start new process in background
echo "Starting Flask server on port 5050..."
nohup "$PY" "$APP_FILE" > log.txt 2>&1 &

echo "Started successfully."
echo "Tail logs with: tail -n 200 -f $APP_DIR/log.txt"
