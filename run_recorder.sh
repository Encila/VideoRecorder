#!/bin/bash

# Activer l'environnement conda
source /home/pi/miniconda3/etc/profile.d/conda.sh
conda activate flower_detection

# Aller dans le répertoire VideoRecorder
cd ~/Desktop/VideoRecorder

# Exécuter le script Python
python main.py
