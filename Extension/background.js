chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (
    changeInfo.status === "complete" &&
    tab.url &&
    tab.url.startsWith("http")
  ) {

    const apiUrl =
      "http://127.0.0.1:5000/predict?url=" + encodeURIComponent(tab.url);

    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => {
        chrome.storage.local.set({ phishguard_result: data });
      })
      .catch((err) => {
        chrome.storage.local.set({
          phishguard_result: { error: "Flask backend not running" },
        });
      });
  }
});
