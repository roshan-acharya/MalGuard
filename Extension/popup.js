chrome.storage.local.get("phishguard_result", (data) => {
  const statusCard = document.getElementById("status-card");
  const statusText = document.getElementById("status-text");

  // No data yet
  if (!data.phishguard_result) {
    statusCard.className = "status checking";
    statusText.textContent = "No scan data available";
    return;
  }

  // Error case
  if (data.phishguard_result.error) {
    statusCard.className = "status malicious";
    statusText.textContent = `Error: ${data.phishguard_result.error}`;
    return;
  }

  const { prediction, url } = data.phishguard_result;

  // Legitimate
  if (prediction === "Legitimate") {
    statusCard.className = "status safe";
    statusText.innerHTML = `
      ✅ This site is SAFE
      <br>
      <small>${url}</small>
    `;
  }
  // Phishing
  else {
    statusCard.className = "status malicious";
    statusText.innerHTML = `
      ⚠️ Malicious URL
      <br>
      <small>${url}</small>
    `;
  }
});
