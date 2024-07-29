window.addEventListener('load', () => {
    const loader = document.getElementById('loader');
    const content = document.getElementById('content');
    
    setTimeout(() => {
        loader.style.opacity = '0'; // Начать анимацию исчезновения
        setTimeout(() => {
            loader.style.display = 'none'; // Полностью скрыть после окончания анимации
            content.style.display = 'block';
        }, 500); // Время должно совпадать с длительностью анимации исчезновения
    }, 500); // 3000 milliseconds = 3 seconds
});
