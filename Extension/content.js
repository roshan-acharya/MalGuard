function injectBadge(result) {
  // remove old badge if exists
  const existing = document.getElementById("phishguard-badge");
  if (existing) existing.remove();

  // Create badge container
  const badge = document.createElement("div");
  badge.id = "phishguard-badge";

  badge.style.position = "fixed";
  badge.style.bottom = "20px";
  badge.style.right = "20px";
  badge.style.padding = "12px 16px";
  badge.style.borderRadius = "50%";
  badge.style.width = "40px";
  badge.style.height = "40px";
  badge.style.display = "flex";
  badge.style.alignItems = "center";
  badge.style.justifyContent = "center";
  badge.style.fontSize = "20px";
  badge.style.fontWeight = "700";
  badge.style.zIndex = "999999";
  badge.style.boxShadow = "0 4px 12px rgba(0,0,0,0.35)";
  badge.style.color = "white";
  badge.style.cursor = "pointer";

  // Set icon based on prediction
  if (result.prediction === "Legitimate") {
    badge.textContent = "✔";
    badge.style.background = "#16a34a";
  } else {
    badge.textContent = "✖";
    badge.style.background = "#dc2626";
  }

  // Create close button
  const closeBtn = document.createElement("span");
  closeBtn.textContent = "×";
  closeBtn.style.position = "absolute";
  closeBtn.style.top = "-8px";
  closeBtn.style.right = "-8px";
  closeBtn.style.background = "#000000cc";
  closeBtn.style.color = "white";
  closeBtn.style.borderRadius = "50%";
  closeBtn.style.width = "18px";
  closeBtn.style.height = "18px";
  closeBtn.style.display = "flex";
  closeBtn.style.alignItems = "center";
  closeBtn.style.justifyContent = "center";
  closeBtn.style.fontSize = "12px";
  closeBtn.style.cursor = "pointer";

  // Close badge on click
  closeBtn.addEventListener("click", () => {
    badge.remove();
  });

  // Append close button to badge
  badge.appendChild(closeBtn);

  // Append badge to body
  document.body.appendChild(badge);
}

// Read result saved by background.js
chrome.storage.local.get("phishguard_result", (data) => {
  if (!data.phishguard_result) return;
  if (data.phishguard_result.error) return;

  injectBadge(data.phishguard_result);
});
