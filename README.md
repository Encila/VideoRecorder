
# VideoRecorder Setup

This repository contains a script to record video. The script can be executed from the terminal, but it can also be configured to run from a desktop shortcut. This guide provides instructions on how to set up the desktop shortcut for the video recorder script.

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

The `run_recorder.sh` script activates the conda environment and runs the `main.py` script.

### `setup.sh`

The `setup.sh` script performs the following actions:

1. Sets the path to the Bash script to be executed (`run_recorder.sh`).
2. Creates a `.desktop` file with the necessary details to create a shortcut.
3. Writes the `.desktop` file to the desktop.
4. Makes both the `.desktop` file and the Bash script executable.

After running the setup script, you should see a `VideoRecorder` shortcut on your desktop. Double-clicking this shortcut will execute the `run_recorder.sh` script in a terminal window.

## Troubleshooting

- Ensure that the paths specified in the script (`SCRIPT_PATH` and `DESKTOP_PATH`) are correct and accessible.
- If you encounter permission issues, make sure you have the necessary rights to execute scripts and create files on the desktop.
- If the script does not execute as expected, check the terminal output for any error messages and verify the paths and file permissions.
