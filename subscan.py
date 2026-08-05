import shutil
import subprocess

def check_nmap():
    if shutil.which("nmap") is None:
        print("Nmap not found")
        return False
    return True


def nmap_scan(target):
    if not check_nmap():
        return None

    result = subprocess.run(
        [
            "nmap",
            "-p", "22,21,80,8080,445",
            "-T4",
            "-oA", "scan_result",
            target
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    return result.stdout


output = nmap_scan("192.168.1.1")
print(output)