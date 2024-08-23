const categoryAccount = document.querySelector(".category-account");
const categorySubcategory = document.querySelector(".category-subcategory");

categoryAccount.addEventListener("mouseover", () => {
    categoryAccount.classList.add("active");
});

categoryAccount.addEventListener("mouseout", () => {
    categoryAccount.classList.remove("active");
});

categorySubcategory.addEventListener("mouseover", () => {
    categorySubcategory.classList.add("active");
});

categorySubcategory.addEventListener("mouseout", () => {
    categorySubcategory.classList.remove("active");
});