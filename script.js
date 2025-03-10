function openModal(product) {
    document.getElementById(product + "-modal").style.display = "block";
}

function closeModal(product) {
    document.getElementById(product + "-modal").style.display = "none";
}

// Close modal if clicked outside of the modal content
window.onclick = function(event) {
    if (event.target.className === 'modal') {
        closeModal('product1');
    }
}
