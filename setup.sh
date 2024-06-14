#!/bin/bash

# Chemin du script Bash à exécuter
SCRIPT_PATH="/home/fablabensfea/Desktop/VideoRecorder/run_recorder.sh"

# Contenu du fichier .desktop
DESKTOP_ENTRY="[Desktop Entry]
Version=1.0
Type=Application
Name= Run VideoRecorder
Comment=Start the recording script
Exec=${SCRIPT_PATH}
Icon=utilities-terminal
Terminal=true
"

# Chemin du raccourci sur le bureau
DESKTOP_PATH="/home/fablabensfea/Desktop/VideoRecorder.desktop"

# Écrire le contenu dans le fichier .desktop
echo "${DESKTOP_ENTRY}" > ${DESKTOP_PATH}

# Rendre le fichier .desktop exécutable
chmod +x ${DESKTOP_PATH}

# Rendre le script bash exécutable
chmod +x ${SCRIPT_PATH}

echo "Setup complete. The shortcut has been created on the Desktop."
