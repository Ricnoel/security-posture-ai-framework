import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def load_config(file_path):
    """Load the JSON config file."""
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        print("[+] Configuration file loaded successfully.")
        return config
    except Exception as e:
        print(f"[-] Error loading config: {e}")
        return None

def analyze_config(config):
    """Analyze the loaded configuration and print results."""
    print("\n[+] Starting analysis...\n")

    # Firewall check
    if config.get("firewall_enabled"):
        print("[+] Firewall is enabled.")
    else:
        print("[-] Firewall is DISABLED! (Bad)")

    # Remote Desktop Protocol (RDP) check
    if config.get("remote_desktop_enabled"):
        print("[-] Remote Desktop is ENABLED! (Potential Risk)")

    # Open ports check
    open_ports = config.get("open_ports", [])
    risky_ports = [22, 3389]
    for port in risky_ports:
        if port in open_ports:
            print(f"[-] Risky port {port} is open!")

    # Password policy checks
    password_policy = config.get("password_policy", {})
    if password_policy.get("complexity_enabled"):
        print("[+] Password complexity is enforced.")
    else:
        print("[-] Password complexity is NOT enforced!")

    if password_policy.get("minimum_length", 0) < 12:
        print("[-] Password minimum length is too short (should be at least 12).")

    # Antivirus check
    if config.get("antivirus_installed"):
        print("[+] Antivirus is installed.")
    else:
        print("[-] Antivirus is NOT installed!")

    # Disk encryption check
    if config.get("disk_encryption_enabled"):
        print("[+] Disk encryption is enabled.")
    else:
        print("[-] Disk encryption is DISABLED!")

    # Admin MFA checks
    for account in config.get("admin_accounts", []):
        if not account.get("mfa_enabled"):
            print(f"[-] Admin account '{account['username']}' does NOT have MFA enabled!")

    # Patching status
    if config.get("patching_status") != "up-to-date":
        print("[-] System patching is OUTDATED!")

def score_config(config):
    """Calculate a security score and provide findings."""
    score = 100
    findings = []

    if config.get("firewall_enabled"):
        findings.append({"check": "Firewall Enabled", "status": "pass"})
    else:
        findings.append({"check": "Firewall Enabled", "status": "fail"})
        score -= 20

    if config.get("remote_desktop_enabled"):
        findings.append({"check": "Remote Desktop Disabled", "status": "fail"})
        score -= 10
    else:
        findings.append({"check": "Remote Desktop Disabled", "status": "pass"})

    open_ports = config.get("open_ports", [])
    risky_ports = [22, 3389]
    for port in risky_ports:
        if port in open_ports:
            findings.append({"check": f"Port {port} Closed", "status": "fail"})
            score -= 5
        else:
            findings.append({"check": f"Port {port} Closed", "status": "pass"})

    password_policy = config.get("password_policy", {})
    if password_policy.get("complexity_enabled"):
        findings.append({"check": "Password Complexity Enabled", "status": "pass"})
    else:
        findings.append({"check": "Password Complexity Enabled", "status": "fail"})
        score -= 10

    if password_policy.get("minimum_length", 0) < 12:
        findings.append({"check": "Password Minimum Length >= 12", "status": "fail"})
        score -= 5
    else:
        findings.append({"check": "Password Minimum Length >= 12", "status": "pass"})

    if config.get("antivirus_installed"):
        findings.append({"check": "Antivirus Installed", "status": "pass"})
    else:
        findings.append({"check": "Antivirus Installed", "status": "fail"})
        score -= 10

    if config.get("disk_encryption_enabled"):
        findings.append({"check": "Disk Encryption Enabled", "status": "pass"})
    else:
        findings.append({"check": "Disk Encryption Enabled", "status": "fail"})
        score -= 15

    for account in config.get("admin_accounts", []):
        if not account.get("mfa_enabled"):
            findings.append({"check": f"MFA Enabled for {account['username']}", "status": "fail"})
            score -= 5
        else:
            findings.append({"check": f"MFA Enabled for {account['username']}", "status": "pass"})

    if config.get("patching_status") != "up-to-date":
        findings.append({"check": "System Patching Up-to-date", "status": "fail"})
        score -= 10
    else:
        findings.append({"check": "System Patching Up-to-date", "status": "pass"})

    score = max(0, score)
    return score, findings

def main():
    """Main entry point."""
    print("Security Posture Framework Starting...")

    # Automatically build the correct path no matter where script is run from
    script_dir = os.path.dirname(os.path.abspath(__file__))           # → src/
    project_root = os.path.dirname(script_dir)                        # → project root
    config_path = os.path.join(project_root, "demo", "sample_config.json")

    config = load_config(config_path)
    if config:
        analyze_config(config)
        score, findings = score_config(config)
        print(f"Final Score: {score}/100")
        for item in findings:
            print(f"{item['check']}: {item['status'].upper()}")

if __name__ == "__main__":
    main()
