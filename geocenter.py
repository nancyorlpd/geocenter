import os
import subprocess
import platform
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_os():
    if platform.system() != 'Windows':
        logging.error("GeoCenter is designed to run on Windows operating systems.")
        return False
    return True

def apply_critical_updates():
    try:
        logging.info("Checking for Windows updates...")
        subprocess.run(['powershell', '-Command', 'Install-WindowsUpdate -AcceptAll -AutoReboot'], check=True)
        logging.info("Windows updates applied successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to apply updates: {e}")

def apply_power_management_tweaks():
    try:
        logging.info("Applying power management tweaks...")
        subprocess.run(['powercfg', '/change', 'monitor-timeout-ac', '10'], check=True)
        subprocess.run(['powercfg', '/change', 'monitor-timeout-dc', '5'], check=True)
        subprocess.run(['powercfg', '/hibernate', 'on'], check=True)
        logging.info("Power management tweaks applied successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to apply power management tweaks: {e}")

def main():
    if not check_os():
        return

    apply_critical_updates()
    apply_power_management_tweaks()

if __name__ == "__main__":
    main()