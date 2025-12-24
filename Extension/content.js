function injectBadge(result) {
  // remove old badge if exists
  const existing = document.getElementById("phishguard-badge");
  if (existing) existing.remove();

  const badge = document.createElement("div");
  badge.id = "phishguard-badge";

  badge.style.position = "fixed";
  badge.style.bottom = "20px";
  badge.style.right = "20px";
  badge.style.padding = "12px 18px";
  badge.style.borderRadius = "10px";
  badge.style.fontSize = "14px";
  badge.style.fontWeight = "600";
  badge.style.zIndex = "999999";
  badge.style.boxShadow = "0 4px 12px rgba(0,0,0,0.35)";
  badge.style.color = "white";

  if (result.prediction === "Legitimate") {
    badge.textContent = "✔ SAFE WEBSITE";
    badge.style.background = "#16a34a";
  } else {
    badge.textContent = "✖ MALICIOUS WEBSITE";
    badge.style.background = "#dc2626";
  }

  document.body.appendChild(badge);
}

// Read result saved by background.js
chrome.storage.local.get("phishguard_result", (data) => {
  if (!data.phishguard_result) return;
  if (data.phishguard_result.error) return;

  injectBadge(data.phishguard_result);
});
