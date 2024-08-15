document.addEventListener('DOMContentLoaded', function() {
    // Select the input elements and submit button
    var new_password = document.getElementById("new_password");
    var confirm_password = document.getElementById("confirm_password");

    const submit = document.getElementById("submit");
  
    // Function to validate passwords
    function validatePassword() {
      if (new_password.value === confirm_password.value) {
        submit.disabled = false;
        submit.style.background = "#5482ff";
      } else {
        submit.disabled = true;
        submit.style.background = "#6b93ff"; // Optional: change color for disabled state
      }
    }
  
    // Attach event listeners to password fields
    new_password.addEventListener('input', validatePassword);
    confirm_password.addEventListener('input', validatePassword);
  });
  