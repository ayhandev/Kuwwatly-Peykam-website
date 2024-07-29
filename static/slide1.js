document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelectorAll('#custom-slider .custom-slide');
    let currentSlide = 0;
  
    function showSlide(index) {
      slides.forEach((slide, i) => {
        slide.classList.remove('active');
        if (i === index) {
          slide.classList.add('active');
        }
      });
    }
  
    function nextSlide() {
      currentSlide = (currentSlide + 1) % slides.length;
      showSlide(currentSlide);
    }
  
    showSlide(currentSlide);
    setInterval(nextSlide, 5000); 
  });
  