import subprocess
import sys

def install_chocolatey():
    try:
        subprocess.run(["powershell", "-Command", "(Get-ExecutionPolicy -Scope CurrentUser) -ne 'AllSigned' | Set-ExecutionPolicy Bypass -Scope CurrentUser -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"], check=True)
        print("Chocolatey has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install Chocolatey.")
        sys.exit(1)

def install_gitleaks():
    try:
        subprocess.run(["choco", "install", "gitleaks", "-y"], check=True)
        print("Gitleaks has been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install Gitleaks using Chocolatey.")
        sys.exit(1)

def main():
    try:
        install_chocolatey()
        install_gitleaks()
    except KeyboardInterrupt:
        print("\nInstallation aborted by user.")

if __name__ == "__main__":
    main()
