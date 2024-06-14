#!/bin/bash

# Path to the Bash script to be executed
SCRIPT_PATH="/home/fablabensfea/Desktop/VideoRecorder/run_recorder.sh"

# Content of the .desktop file
DESKTOP_ENTRY="[Desktop Entry]
Version=1.0
Type=Application
Name=VideoRecorder
Comment=Start the recording script
Exec=${SCRIPT_PATH}
Icon=utilities-terminal
Terminal=true
"

# Path to the shortcut on the desktop
DESKTOP_PATH="/home/fablabensfea/Desktop/VideoRecorder.desktop"

# Write the content to the .desktop file
echo "${DESKTOP_ENTRY}" > ${DESKTOP_PATH}

# Make the .desktop file executable
chmod +x ${DESKTOP_PATH}

# Make the Bash script executable
chmod +x ${SCRIPT_PATH}

echo "Setup complete. The shortcut has been created on the Desktop."
