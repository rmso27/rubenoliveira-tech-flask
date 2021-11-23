window.onload = function update_nav() {
    url = "http://192.168.2.86:5000/"
    current_url = window.location.href

    if (current_url == url) {
        document.getElementById("home").style.background = "#F4FA58"
        document.getElementById("home").style.color = "#0B243B"
    } else if (current_url == (url + "about")) {
        document.getElementById("about").style.background = "#F4FA58"
        document.getElementById("about").style.color = "#0B243B"
    } else {
        document.getElementById("projects").style.background = "#F4FA58"
        document.getElementById("projects").style.color = "#0B243B"
    }
}