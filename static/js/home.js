let button = document.getElementById('button');
let form = document.getElementById('form');

button.addEventListener('click', function() {
    button.classList.add('active');
    setTimeout(() => {
        form.style.display = 'flex';
    }, 300);
});

form.addEventListener("submit", function() {    
    setTimeout(() => {
        document.getElementById("cards").scrollIntoView({ behavior: "smooth" });
    }, 500);
});
