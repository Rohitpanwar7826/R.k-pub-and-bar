window.onload = () => {
    setTimeout(() => {
        document.querySelector("body").classList.add("display");
    }, 5000);
};

$(".gallery").magnificPopup({
    delegate: 'a',
    type: 'image',
    gallery: {
        enabled: true
    }
});

var counter = 1;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 4) {
        counter = 1;
    }
}, 5000);