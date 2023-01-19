window.onload = function () {
    const toggle = document.getElementById("togthemebtn");
    const theme = document.getElementById("stylesheet_toggle");
    const selected = localStorage.getItem("css");
    if (selected !== null) {
      theme.href = selected;
    }

    toggle.addEventListener("click", function () {
        if (theme.getAttribute("href") == "/static/styles.css") {
            theme.href = "/static/dark.css";
        } else {
            theme.href = "/static/styles.css";
        }
        localStorage.setItem("css", theme.href);
    });
}