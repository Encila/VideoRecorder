#!/bin/bash

# Activer l'environnement conda
echo "Activating conda environment"
source /home/fablabensfea/miniconda3/etc/profile.d/conda.sh
conda activate flower_detection

# Vérifier l'activation de l'environnement
if [ $? -ne 0 ]; then
    echo "Failed to activate conda environment"
    exit 1
fi

# Aller dans le répertoire VideoRecorder
echo "Changing directory to ~/Desktop/VideoRecorder"
cd ~/Desktop/VideoRecorder

# Exécuter le script Python
python main.py

# Vérifier l'exécution du script Python
if [ $? -ne 0 ]; then
    echo "Python script failed to run"
    exit 1
fi

echo "Script executed successfully"