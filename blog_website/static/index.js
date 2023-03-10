function toggleTheme() {
    var theme = document.getElementById('stylesheet');
    if (theme.getAttribute('href') == '/static/light.css' || theme.getAttribute('href') == 'http://127.0.0.1:5000/static/light.css') {
        theme.setAttribute('href', '/static/dark.css');
    } else {
        theme.setAttribute('href', '/static/light.css');
    }
    localStorage.setItem("stylesheet", theme.href);
}

function switchDefault() {
    var theme = document.getElementById('stylesheet');
    const selected = localStorage.getItem("stylesheet");
    if (selected !== null) {
        theme.href = selected;
    }
}
