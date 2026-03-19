document.addEventListener("DOMContentLoaded", function () {
    // Defina as URLs das imagens usando as tags de template do Django
    const images = [
        "{% static 'img/beachfrontStreet.webp' %}",
        "{% static 'img/Image_bcrfwcbcrfwcbcrf.webp' %}",
        "{% static 'img/Image_y70h8y70h8y70h8y.webp' %}",
        "{% static 'img/Image_zgqc02zgqc02zgqc.webp' %}",
    ];

    let currentIndex = 0;
    const imgElement = document.getElementById('background-slider');

    // Configura o intervalo (ex: 5000ms = 5 segundos)
    setInterval(() => {
        // Inicia o fade out (remove opacity-100, adiciona opacity-0)
        imgElement.classList.replace('opacity-100', 'opacity-0');

        // Aguarda o fim da transição do Tailwind (1000ms) para trocar o src
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % images.length;
            imgElement.src = images[currentIndex];

            // Inicia o fade in (remove opacity-0, adiciona opacity-100)
            imgElement.classList.replace('opacity-0', 'opacity-100');
        }, 1000);

    }, 5000);
});