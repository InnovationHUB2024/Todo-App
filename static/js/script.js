function getCSRFToken() {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Check if this cookie string begins with "csrftoken="
      if (cookie.substring(0, 10) === "csrftoken=") {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}

// Get the CSRF token

const logout_anchor = document.querySelector("a#logout");

if (logout_anchor) {
  logout_anchor.addEventListener("click", function (e) {
    e.preventDefault();
    const csrftoken = getCSRFToken();

    fetch("/logout/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken, // Include the CSRF token here
      },
    })
      .then((response) => response.json())
      .then((data) => {
        if (data["status"] === "success") {
          window.location.href = "/login/";
        }
      });
  });
}
