// JS for Like Button Animation & Form Interactivity
document.addEventListener("DOMContentLoaded", function () {
  const likeButtons = document.querySelectorAll(".like-btn");
  likeButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.classList.toggle("liked");
      if (btn.classList.contains("liked")) {
        btn.style.color = "#ef4444";
      } else {
        btn.style.color = "#2563eb";
      }
    });
  });

  // Smooth scroll to top when post created
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
});
