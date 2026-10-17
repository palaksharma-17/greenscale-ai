const authForm = document.getElementById("authForm");
const loginTab = document.getElementById("loginTab");
const signupTab = document.getElementById("signupTab");
const authTitle = document.getElementById("authTitle");
const authSubtitle = document.getElementById("authSubtitle");
const authSubmit = document.getElementById("authSubmit");
const nameGroup = document.getElementById("nameGroup");
const confirmGroup = document.getElementById("confirmGroup");
const fullName = document.getElementById("fullName");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const authMessage = document.getElementById("authMessage");

let currentMode = new URLSearchParams(window.location.search).get("mode") === "signup" ? "signup" : "login";

function showMessage(message, type) {
  authMessage.textContent = message;
  authMessage.className = `alert alert-${type}`;
}

function setMode(mode) {
  currentMode = mode;
  const signingUp = mode === "signup";
  loginTab.classList.toggle("active", !signingUp);
  signupTab.classList.toggle("active", signingUp);
  nameGroup.classList.toggle("d-none", !signingUp);
  confirmGroup.classList.toggle("d-none", !signingUp);
  fullName.required = signingUp;
  confirmPassword.required = signingUp;
  authTitle.textContent = signingUp ? "Create your account" : "Welcome back";
  authSubtitle.textContent = signingUp ? "Create an account to explore GreenScale AI." : "Log in to continue to your dashboard.";
  authSubmit.textContent = signingUp ? "Create account" : "Login";
  authMessage.className = "alert d-none";
}

loginTab.addEventListener("click", () => setMode("login"));
signupTab.addEventListener("click", () => setMode("signup"));

authForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const email = document.getElementById("email").value.trim();

  if (currentMode === "signup") {
    if (password.value !== confirmPassword.value) {
      showMessage("Passwords do not match. Please try again.", "danger");
      return;
    }
    // Demo only: do not store real passwords in browser storage.
    sessionStorage.setItem("greenscaleDemoUser", JSON.stringify({
      name: fullName.value.trim(),
      email: email
    }));
    showMessage("Demo sign-up complete. Opening the dashboard…", "success");
  } else {
    // Demo only: this checks that fields are filled, not real credentials.
    const savedUser = JSON.parse(sessionStorage.getItem("greenscaleDemoUser") || "null");
    if (savedUser && savedUser.email.toLowerCase() === email.toLowerCase()) {
      sessionStorage.setItem("greenscaleDemoUser", JSON.stringify(savedUser));
    } else {
      sessionStorage.setItem("greenscaleDemoUser", JSON.stringify({
        name: email.split("@")[0],
        email: email
      }));
    }
    showMessage("Demo login complete. Opening the dashboard…", "success");
  }

  setTimeout(() => window.location.href = "dashboard.html", 500);
});

setMode(currentMode);
