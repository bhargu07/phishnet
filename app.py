from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse
import re

app = Flask(__name__)

SUSPICIOUS_TLDS = {"xyz", "top", "club", "win", "bid"}
URL_SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly"}

def score_url(raw_url):
    score = 100
    alerts = []

    parsed = urlparse(raw_url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""

    if parsed.scheme.lower() != "https":
        score -= 30
        alerts.append("No HTTPS detected")

    if re.match(r"^\d+\.\d+\.\d+\.\d+$", hostname):
        score -= 40
        alerts.append("IP address instead of domain")

    if "@" in raw_url:
        score -= 25
        alerts.append("@ symbol in URL")

    if len(hostname) > 30:
        score -= 10
        alerts.append("Very long domain name")

    if hostname.count(".") >= 4:
        score -= 10
        alerts.append("Many subdomains (possible deception)")

    tld = hostname.split(".")[-1] if "." in hostname else ""
    if tld in SUSPICIOUS_TLDS:
        score -= 10
        alerts.append("Suspicious TLD")

    if hostname.startswith("xn--"):
        score -= 30
        alerts.append("Punycode / homograph detected")

    if len(path) > 100:
        score -= 10
        alerts.append("Very long path")

    if hostname in URL_SHORTENERS:
        score -= 20
        alerts.append("URL shortener detected")

    score = max(0, min(100, score))
    verdict = "safe" if score >= 80 else "suspicious" if score >= 50 else "phishing"

    return {"url": raw_url, "score": score, "verdict": verdict, "alerts": alerts}

def is_valid_url(raw_url):
    try:
        parsed = urlparse(raw_url)
        hostname = parsed.hostname
        return bool(hostname and (hostname == "localhost" or "." in hostname))
    except:
        return False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    raw = (data.get("url") or "").strip()

    if not raw:
        return jsonify({"error": "URL is required"}), 400

    raw = raw.split()[0]  # Remove extra text after space

    if not re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", raw):
        raw = "https://" + raw

    if not is_valid_url(raw):
        return jsonify({"error": "Invalid URL format. Try: https://example.com"}), 400

    result = score_url(raw)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
