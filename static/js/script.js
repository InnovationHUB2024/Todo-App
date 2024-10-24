function ToastIt(text, status = "success", duration = 3000) {
  let color = "";
  let text_color = "";
  if (status == "success") {
    color = "#28A745";
  } else if (status == "error") {
    color = "#FF4C4C";
  } else if (status == "warning") {
    color = "#FFC107";
    text_color = "#000";
  } else {
    color = "blue";
  }
  console.log(color);

  Toastify({
    text: text,
    duration: duration,
    newWindow: true,
    close: true,
    gravity: "top",
    position: "right",
    stopOnFocus: true,
    style: {
      background: color,
      color: text_color,
    },
    onClick: function () {}, // Callback after click
  }).showToast();
}

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

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".completed-checkbox").forEach((checkbox) => {
    console.log(checkbox);

    checkbox.addEventListener("change", function () {
      const todoId = this.getAttribute("data-id");
      const completed = this.checked;

      // Use Fetch API to send the update request
      fetch(`/todos/${todoId}/update/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ completed }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log("Todo updated successfully");
            if (completed) {
              ToastIt("Todo marked as done.", "success");
            } else {
              ToastIt("Todo marked as undone.", "warning");
            }
          } else {
            this.checked = !completed;
            console.error("Failed to update todo");
          }
        })
        .catch((error) => console.error("Error:", error));
    });
  });
});
