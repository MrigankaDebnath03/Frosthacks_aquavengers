 const contactButton = document.querySelectorAll('.contact-button');
const contactModal = document.getElementById('contactModal');

function openContactModal() {
    contactModal.style.display = 'block';
}

function closeContactModal() {
    contactModal.style.display = 'none';
}

window.addEventListener('click', (event) => {
    if (event.target === contactModal) {
        closeContactModal();
    }
});

// Add event listeners to all contact buttons
contactButton.forEach(button => {
    button.addEventListener('click', openContactModal);
});
