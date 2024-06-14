
# VideoRecorder Setup

This repository contains scripts to set up a shortcut on the desktop to run the VideoRecorder script.

## Installation Steps

1. **Clone the repository:**

   Open a terminal and run the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. **Navigate to the repository directory:**

   Change into the directory where the repository was cloned:

   ```bash
   cd yourrepository
   ```

3. **Make the setup script executable:**

   Ensure that the `setup.sh` script has execute permissions:

   ```bash
   chmod +x setup.sh
   ```

4. **Run the setup script:**

   Execute the `setup.sh` script to create the desktop shortcut and configure it:

   ```bash
   ./setup.sh
   ```

## Script Details

### `main.py`

The `main.py` script records a video using the Picamera2. It includes the following functions:

- **setup_directory(base_path):** Create the directory if it doesn't exist.
- **generate_filename(base_path):** Generate a unique filename based on the current timestamp.
- **configure_camera(resolution):** Configure the Picamera2 instance with the specified resolution.
- **record_video(picam2, duration, filename):** Record video for the specified duration.
- **parse_arguments():** Parse command-line arguments.

### `run_recorder.sh`

The `run_recorder.sh` script activates the conda environment and runs the `main.py` script:

```bash
#!/bin/bash

# Activate the conda environment
echo "Activating conda environment"
source /home/fablabensfea/miniconda3/etc/profile.d/conda.sh
conda activate flower_detection

# Verify the exit status of the conda command
if [ $? -ne 0 ]; then
    echo "Failed to activate conda environment"
    exit 1
fi

# Move to the directory where the Python script is located
echo "Changing directory to ~/Desktop/VideoRecorder"
cd ~/Desktop/VideoRecorder

# Execute the Python script
python main.py

# Verify the exit status of the Python script
if [ $? -ne 0 ]; then
    echo "Python script failed to run"
    exit 1
fi

echo "Script executed successfully"
```

### `setup.sh`

The `setup.sh` script creates a desktop shortcut to run the `run_recorder.sh` script:

```bash
#!/bin/bash

# Path to the Bash script to be executed
SCRIPT_PATH="/home/fablabensfea/Desktop/VideoRecorder/run_recorder.sh"

# Content of the .desktop file
DESKTOP_ENTRY="[Desktop Entry]
Version=1.0
Type=Application
Name=Run VideoRecorder
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
```

## Troubleshooting

- Ensure that the paths specified in the script (`SCRIPT_PATH` and `DESKTOP_PATH`) are correct and accessible.
- If you encounter permission issues, make sure you have the necessary rights to execute scripts and create files on the desktop.
- If the script does not execute as expected, check the terminal output for any error messages and verify the paths and file permissions.
