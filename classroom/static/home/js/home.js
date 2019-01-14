window.onload = function () {
    var swiper1 = new Swiper('#topSwiper', {
      slidesPerView: 1,
      spaceBetween: 0,
      freeMode: false,
      autoplay: {
          delay: 2000,
          disableOnInteraction: false
      },
      loop:true,
      grabCursor: true,
      pagination:true
});

    var swiper2 = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 0,
        freeMode: false,
        loop:true,
        grabCursor: true,
        pagination:true
});
};


