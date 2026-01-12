# 🛡️ SOC Log Monitoring Dashboard (SIEM Simulation)

A Security Operations Center (SOC) style **Log Monitoring Dashboard** built using **Flask and Python**, simulating **SIEM fundamentals, incident detection, and response workflows**.

This project demonstrates how login events are collected, analyzed, and acted upon, closely aligning with **SOC Analyst, Blue Team, and Deloitte Cyber Defense simulations**.

---

## 🚀 Key Features

- ✅ Login activity logging
- ✅ Failed login detection
- ✅ Brute-force attempt monitoring
- ✅ IP blacklisting after multiple failures
- ✅ Admin-only SOC dashboard
- ✅ Centralized event log visualization
- ✅ Session-based authentication
- ✅ Incident response automation (basic)

---

## 🛠️ Tech Stack

- **Backend:** Python  
- **Framework:** Flask  
- **Database:** SQLite  
- **Security Logic:** Custom SIEM-style correlation  
- **Frontend:** HTML + CSS (Enterprise SOC UI)  

---

## 🧠 Cybersecurity Concepts Demonstrated

- Security Operations Center (SOC) workflows
- SIEM log ingestion & correlation
- Failed login attack detection
- Brute-force attack mitigation
- IP reputation & blacklisting
- Incident response automation
- Authentication monitoring
- Session management
- Blue Team fundamentals

> ⚠️ This project is strictly for **educational and defensive security purposes**.

---


## ⚙️ How It Works (SOC Flow)

1. User attempts login
2. Login event is logged (username, IP, status, timestamp)
3. Failed attempts are counted per IP
4. Multiple failures trigger IP blacklisting
5. Successful login grants admin dashboard access
6. SOC analyst views events and investigates incidents

---

## 🔐 Detection & Response Logic

| Event | SOC Action |
|----|-----------|
| Successful login | Log event |
| Failed login | Increment failure counter |
| Repeated failures | Blacklist IP |
| Blacklisted IP | Block authentication |
| Admin login | Display SOC dashboard |

---

## 🖥️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/soc_dashboard.git
cd soc_dashboard

2️⃣ Install Dependencies
python -m pip install -r requirements.txt

3️⃣ Run the Application
python app.py

Open in browser:
http://127.0.0.1:5000


👤 Default Admin Credentials
Username: admin
Password: admin123


🧪 Example Use Cases
Detect brute-force login attempts

Monitor suspicious IP behavior

Simulate SOC alert triage

Practice blue team incident response

Demonstrate SIEM fundamentals in interviews

🎯 SOC / Deloitte Interview Mapping
You can confidently explain:

How login logs are ingested

How brute-force attacks are detected

How IP blacklisting mitigates threats

How this simulates SIEM correlation rules

How SOC analysts investigate failed logins

Example interview line:

“I built a SOC-style log monitoring dashboard using Flask that simulates SIEM behavior, failed login detection, IP blacklisting, and basic incident response.”

🔮 Future Enhancements
Email alerts for critical incidents

Geo-IP analysis

Severity-based alert scoring

Dashboard charts & timelines

Log export (CSV / PDF)

IAM integration

Elastic / Splunk-style indexing simulation

👨‍💻 Author
Sunny Yadav
Cybersecurity & FullStack Dev
SOC • SIEM • Blue Team • Incident Response

📜 License
This project is licensed for educational and defensive research use only.
Unauthorized or malicious use is strictly prohibited.
