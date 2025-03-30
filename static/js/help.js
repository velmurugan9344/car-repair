document.addEventListener("DOMContentLoaded", function() {
    // Open Help Popup
    window.openHelpPopup = function() {
        document.getElementById("help-popup").style.display = "block";
    };

    // Close Help Popup
    window.closeHelpPopup = function() {
        document.getElementById("help-popup").style.display = "none";
    };

    // Handle Help Form Submission
    document.getElementById("help-form").addEventListener("submit", function(event) {
        event.preventDefault();

        let email = document.getElementById("user-email").value;
        let message = document.getElementById("help-message").value;
        let successMessage = document.getElementById("help-success-message");

        fetch("/help-request/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ email: email, message: message })
        })
        .then(response => response.json())
        .then(data => {
            successMessage.textContent = "Your request has been submitted successfully!";
            successMessage.style.display = "block";

            // Clear form fields
            document.getElementById("user-email").value = "";
            document.getElementById("help-message").value = "";
        })
        .catch(error => {
            successMessage.textContent = "Something went wrong. Please try again!";
            successMessage.style.color = "red";
            successMessage.style.display = "block";
            console.error("Error:", error);
        });
    });
});

// Get CSRF Token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.split('=')[1]);
            }
        });
    }
    return cookieValue;
}