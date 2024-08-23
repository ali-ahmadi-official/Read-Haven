const tablet = window.matchMedia("(min-width: 768px)");
const laptop = window.matchMedia("(min-width: 1024px)");

let swiper;

const initSwiper = (slidesPerView) => {
    if (swiper) swiper.destroy(true, true);
    swiper = new Swiper(".mySwiper", {
        slidesPerView: slidesPerView,
        spaceBetween: 30,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });
};

const changeTap = () => {
    if (tablet.matches) {
        initSwiper(3);
    } else {
        initSwiper(2);
    }
};

const changeLap = () => {
    if (laptop.matches) {
        initSwiper(5);
    } else {
        changeTap();
    }
};

tablet.addEventListener("change", changeTap);
laptop.addEventListener("change", changeLap);

changeLap();
