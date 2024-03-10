import subprocess
import sys

def install_packages(packages):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *packages])
        print("Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print("Failed to install packages.")

if __name__ == "__main__":
    packages_to_install = [
        "flask",
        "flask_cors",
        "Pillow",
    ]
    
    print("Installing packages...")
    install_packages(packages_to_install)
