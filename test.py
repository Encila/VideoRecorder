import os
import sys
import logging
import coloredlogs
from datetime import datetime
from picamera2 import Picamera2
import argparse

# Custom color scheme for log levels to match your terminal
custom_colors = {
    'asctime': {'color': 'white'},
    'debug': {'color': 'green'},
    'info': {'color': 'green'},
    'warning': {'color': 'yellow'},
    'error': {'color': 'red', 'bold': True},
    'critical': {'color': 'magenta', 'bold': True},
}

# Configure logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO', logger=logger, fmt='[%(asctime)s] [%(process)d] %(levelname)s %(message)s', level_styles=custom_colors)

def setup_directory(base_path):
    """Create the directory if it doesn't exist."""
    try:
        os.makedirs(base_path, exist_ok=True)
        logger.info(f"Directory {base_path} is ready.")
    except Exception as e:
        logger.error(f"Failed to create directory {base_path}: {e}")
        sys.exit(1)

def generate_filename(base_path):
    """Generate a unique filename based on the current timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(base_path, f"video_{timestamp}.mp4")

def configure_camera(resolution):
    """Configure the Picamera2 instance with the specified resolution."""
    try:
        picam2 = Picamera2()
        video_config = picam2.create_video_configuration(main={"size": resolution})
        picam2.configure(video_config)
        logger.info(f"Camera configured with resolution {resolution}.")
        return picam2
    except Exception as e:
        logger.error(f"Failed to configure camera: {e}")
        sys.exit(1)

def record_video(picam2, duration, filename):
    """Record video for the specified duration."""
    try:
        logger.info(f"Recording video for {duration} seconds...")
        picam2.start_and_record_video(filename, duration=duration, show_preview=True)
        logger.info(f"Recording complete. Video saved as {filename}.")
    except Exception as e:
        logger.error(f"Failed to record video: {e}")
        sys.exit(1)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Record video using Picamera2.")
    parser.add_argument("--duration", type=int, default=15, help="Duration of the video recording in seconds.")
    parser.add_argument("--width", type=int, default=2592, help="Width of the video resolution.")
    parser.add_argument("--height", type=int, default=2592, help="Height of the video resolution.")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    duration = args.duration
    resolution = (args.width, args.height)

    home_dir = os.path.expanduser("~")
    base_path = os.path.join(home_dir, "Desktop", "database")

    setup_directory(base_path)
    filename = generate_filename(base_path)
    picam2 = configure_camera(resolution)
    record_video(picam2, duration, filename)
