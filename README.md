# 🔐 Security Posture AI Framework

A lightweight, modular Python + Flask dashboard that analyzes and visualizes your system or cloud security posture based on a real-time or simulated configuration file.

> 💡 Ideal for DevSecOps automation, audit reporting, and CI/CD integration.

---

## 📊 What It Does

- Reads a structured config file (`sample_config.json`)
- Calculates a **security score** out of 100
- Identifies risks: firewall, RDP, open ports, MFA, AV, patching, etc.
- Shows a live **web dashboard** via Flask
- Displays a **pass/fail checklist** of findings

---

## 🚀 Live Demo (Run Locally)

1. **Install Flask (Windows)**  
   (Use your exact Python path if needed)

   ```bash
   python -m pip install flask
   ```

2. **Run the App**

   ```bash
   cd src
   python dashboard.py
   ```

3. **Visit in your browser:**  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Folder Structure

```
security-posture-ai-framework/
├── demo/
│   └── sample_config.json      ← simulated config input
├── src/
│   ├── main.py                 ← analyzer + scoring logic
│   ├── dashboard.py            ← Flask web app
│   └── templates/
│       └── score.html          ← dashboard UI (Jinja2)
```

---

## 🔄 Planned Enhancements

- Auto-generate config from real Windows/Linux/cloud systems
- Export reports (PDF, CSV, JSON)
- REST API for CI/CD integration
- Charts and interactive UI (Chart.js, Bootstrap)

---

## 📦 Example Config (`sample_config.json`)

```json
{
  "firewall_enabled": true,
  "remote_desktop_enabled": true,
  "open_ports": [22, 80, 3389],
  "password_policy": {
    "complexity_enabled": false,
    "minimum_length": 8
  },
  "antivirus_installed": true,
  "disk_encryption_enabled": false,
  "admin_accounts": [
    { "username": "admin", "mfa_enabled": false }
  ],
  "patching_status": "outdated"
}
```

---

## 💼 Real-World Use Cases

- ✅ Internal security audits
- ✅ DevSecOps pipeline gate
- ✅ SIEM data visualizer
- ✅ Security hardening checklist
- ✅ Proof-of-concept for job interviews

---

## 🙌 Author

**Ricnoel**  
GitHub: [github.com/Ricnoel](https://github.com/Ricnoel)

---

## 📜 License

MIT License — free to use and modify

