chrome.storage.local.get("phishguard_result", (data) => {
  const box = document.getElementById("result");

  if (!data.phishguard_result) {
    box.innerHTML = "<span class='warn'>No data yet</span>";
    return;
  }

  if (data.phishguard_result.error) {
    box.innerHTML = `<span class="error">${data.phishguard_result.error}</span>`;
    return;
  }

  const prediction = data.phishguard_result.prediction;
  const url = data.phishguard_result.url;

  if (prediction === "Legitimate") {
    box.innerHTML = `<span class="safe">SAFE ✔</span><br><small>${url}</small>`;
  } else {
    box.innerHTML = `<span class="phishing">PHISHING ✖</span><br><small>${url}</small>`;
  }
});
