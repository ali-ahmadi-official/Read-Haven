const CloseBtns = document.querySelectorAll(".mobile-list");
const MobileCategories = document.getElementById("categories");

CloseBtns.forEach(element => {
    element.addEventListener("click", () => {
        MobileCategories.classList.toggle("none");
    });
});