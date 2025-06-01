document.querySelector(".toggle-button").addEventListener("click", () => {
  document.querySelector(".sidebar-menu").classList.toggle("collapsed")
});

const toggleBtn = document.getElementById("toggleAccessibility");
const dropdownMenu = document.querySelector(".dropdown-menu");
const arrowIcon = toggleBtn.querySelector(".arrow");

toggleBtn.addEventListener("click", (e) => {
  e.stopPropagation(); 
  dropdownMenu.classList.toggle("active");
  arrowIcon.classList.toggle("rotated");
});

document.addEventListener("click", (event) => {
  const isClickInside = toggleBtn.contains(event.target) || dropdownMenu.contains(event.target);
  if (!isClickInside) {
    dropdownMenu.classList.remove("active");
    arrowIcon.classList.remove("rotated");
  }
});