# 🛡️ PhishNet – URL Phishing Detection System

PhishNet is a lightweight web-based URL safety checker designed to identify potentially suspicious and phishing URLs using rule-based URL analysis.

The application analyzes different characteristics of a URL and assigns a safety score between **0 and 100**. Based on the score, the URL is classified as **Safe**, **Suspicious**, or **Phishing**.

## 🚀 Features

* 🔗 URL safety analysis
* 🔐 HTTPS detection
* 🌐 IP-address based URL detection
* ⚠️ Detection of suspicious `@` symbols
* 📏 Detection of unusually long domain names and URL paths
* 🌍 Suspicious TLD detection
* 🔤 Punycode / homograph detection
* 🔀 URL shortener detection
* 🧩 Detection of excessive subdomains
* 📊 Safety score from 0–100
* 🚨 Detailed alerts explaining suspicious URL characteristics
* 💻 Simple and interactive web interface

## 🔍 How It Works

1. The user enters a website URL.
2. PhishNet validates and normalizes the URL.
3. The Flask backend extracts the domain, path, and other URL components.
4. Multiple URL characteristics are checked using predefined security rules.
5. A score is calculated based on the detected characteristics.
6. The application generates a final verdict.
7. The result and detected alerts are displayed on the web interface.

### Verdict Classification

| Score  | Verdict       |
| ------ | ------------- |
| 80–100 | ✅ Safe        |
| 50–79  | ⚠️ Suspicious |
| 0–49   | 🚨 Phishing   |

## 🧠 Detection Rules

PhishNet currently checks for the following indicators:

* Missing HTTPS
* IP address used instead of a domain name
* `@` symbol in the URL
* Very long domain names
* Excessive subdomains
* Suspicious top-level domains
* Punycode / possible homograph attacks
* Very long URL paths
* Common URL shorteners

Each detected indicator decreases the initial score, helping identify potentially malicious URLs.

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Regular Expressions**
* **URL Parsing**

## 📁 Project Structure

```text
phishnet/
│
├── app.py
├── index.html
├── script.js
├── style.css
├── requirements.txt
└── README.md
```

### File Description

* `app.py` – Flask backend and URL analysis logic
* `index.html` – Web interface
* `script.js` – Frontend URL checking and API communication
* `style.css` – User interface styling
* `requirements.txt` – Python dependencies
* `README.md` – Project documentation

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bhargu07/phishnet.git
cd phishnet
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally using Flask's development server.

Open the displayed local URL in your web browser and enter a website URL to analyze it.

## 🖥️ Example

Enter:

```text
https://example.com
```

PhishNet analyzes the URL and displays:

```text
URL: https://example.com
Score: 100
Verdict: SAFE
No alerts found
```

For a URL containing suspicious characteristics, the application displays the corresponding alerts and lowers the safety score.

## 🔒 Security Approach

PhishNet uses static URL characteristics rather than visiting or executing the submitted website. This allows the application to perform lightweight analysis based on the structure of the URL.

However, the result should be treated as an **indicator rather than a guaranteed security verdict**, since phishing detection based only on URL characteristics cannot identify every malicious website.




