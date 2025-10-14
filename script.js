function normalizeInput(raw) {
    if (!raw) return "";
    raw = raw.trim();
    if (raw.indexOf(" ") !== -1) raw = raw.split(/\s+/)[0];
    if (!/^[a-zA-Z][a-zA-Z0-9+.\-]*:\/\//.test(raw)) raw = "https://" + raw;
    return raw;
}

async function checkURL() {
    const raw = document.getElementById("urlInput").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Checking...";
    const url = normalizeInput(raw);
    if (!url) {
        resultDiv.innerHTML = "<p class='alert'>Please enter a URL.</p>";
        return;
    }
    try {
        const res = await fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });
        const data = await res.json();
        if (data.error) {
            resultDiv.innerHTML = `<p class='alert'>${data.error}</p>`;
            return;
        }
        resultDiv.innerHTML = `
            <p><strong>URL:</strong> ${data.url}</p>
            <p><strong>Score:</strong> <span class='${data.verdict}'>${data.score}</span></p>
            <p><strong>Verdict:</strong> <span class='${data.verdict}'>${data.verdict.toUpperCase()}</span></p>
            ${data.alerts.length ? "<p><strong>Alerts:</strong></p><ul>" + data.alerts.map(a => `<li class="alert">${a}</li>`).join("") + "</ul>" : "<p>No alerts found ✅</p>"}
        `;
    } catch (err) {
        console.error(err);
        resultDiv.innerHTML = "<p class='alert'>Server error. Please try again.</p>";
    }
}

document.getElementById("checkBtn").addEventListener("click", checkURL);
document.getElementById("urlInput").addEventListener("keydown", e => {
    if (e.key === "Enter") {
        e.preventDefault();
        checkURL();
    }
});
