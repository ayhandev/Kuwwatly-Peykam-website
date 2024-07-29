// script.js
document.addEventListener('DOMContentLoaded', () => {
    const sliderContainer = document.querySelector('.slider-container');
    const sliderItems = document.querySelectorAll('.slider-item');
    const photoModal = document.getElementById('photo-modal');
    const modalImage = document.getElementById('modal-image');
    const closeBtn = document.querySelector('.modal-close');
    const prevBtn = document.querySelector('.slider-nav.prev');
    const nextBtn = document.querySelector('.slider-nav.next');
    const modalPrevBtn = document.querySelector('.modal-nav.prev');
    const modalNextBtn = document.querySelector('.modal-nav.next');

    let currentIndex = 0;
    let autoSlideInterval;
    const slideInterval = 5000; // Интервал переключения слайдов в миллисекундах
    const slidesToShow = 12; // Общее количество видимых слайдов
    const totalSlides = sliderItems.length;

    function updateSlider() {
        const offset = -100 * (currentIndex / slidesToShow);
        sliderContainer.style.transform = `translateX(${offset}%)`;
    }

    function showNextSlide() {
        currentIndex = (currentIndex + 1) % totalSlides;
        updateSlider();
    }

    function showPrevSlide() {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        updateSlider();
    }

    function startAutoSlide() {
        autoSlideInterval = setInterval(showNextSlide, slideInterval);
    }

    function stopAutoSlide() {
        clearInterval(autoSlideInterval);
    }

    startAutoSlide();

    nextBtn.addEventListener('click', () => {
        stopAutoSlide();
        showNextSlide();
    });
    prevBtn.addEventListener('click', () => {
        stopAutoSlide();
        showPrevSlide();
    });

    sliderItems.forEach((item, index) => {
        item.addEventListener('click', (e) => {
            if (e.target.tagName === 'IMG') { // Проверка, что клик на изображение
                photoModal.classList.add('show');
                modalImage.src = e.target.src;
                currentIndex = index;
            }
        });
    });

    closeBtn.addEventListener('click', () => {
        photoModal.classList.remove('show');
        startAutoSlide();
    });

    modalPrevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
        modalImage.src = sliderItems[currentIndex].querySelector('img').src;
    });

    modalNextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % totalSlides;
        modalImage.src = sliderItems[currentIndex].querySelector('img').src;
    });

    window.addEventListener('click', (e) => {
        if (e.target === photoModal) {
            photoModal.classList.remove('show');
            startAutoSlide();
        }
    });
});
