document.addEventListener("DOMContentLoaded", function () {
    var body = document.body;

    // Create and append the background element
    var background = document.createElement('div');
    background.classList.add('background');
    body.appendChild(background);

    // Add event listener to dynamically change the background color
    var faqContainer = document.querySelector(".faq-container");
    faqContainer.addEventListener("click", function () {
        background.style.backgroundColor = getRandomColor();
    });

    // Function to generate a random color
    function getRandomColor() {
        var letters = "0123456789ABCDEF";
        var color = "#";
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});

function showAnswer(num) {
    var x = document.getElementById("answer" + num);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}