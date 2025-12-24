chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (
    changeInfo.status === "complete" &&
    tab.url &&
    tab.url.startsWith("http")
  ) {
    const apiUrl =
      "https://malguard.onrender.com/predict?url=" +
      encodeURIComponent(tab.url);

    fetch(apiUrl)
      .then((res) => res.json())
      .then((data) => {
        chrome.storage.local.set({
          phishguard_result: {
            ...data,
            url: tab.url,
          },
        });
      })
      .catch((err) => {
        chrome.storage.local.set({
          phishguard_result: {
            error: "Flask backend not running",
            url: tab.url,
          },
        });
      });
  }
});
