document.addEventListener("DOMContentLoaded", function () {
    // Check if user just logged in (example: using sessionStorage)
    if (sessionStorage.getItem("justLoggedIn")) {
        document.getElementById("cookie-popup").style.display = "block";
        sessionStorage.removeItem("justLoggedIn"); // Remove the flag after showing
    } else if (!localStorage.getItem("cookieConsent")) {
        document.getElementById("cookie-popup").style.display = "block";
    }
});

function acceptCookies() {
    localStorage.setItem("cookieConsent", "true");
    document.getElementById("cookie-popup").style.display = "none";
}

function rejectCookies() {
    document.getElementById("cookie-popup").style.display = "none";
}
