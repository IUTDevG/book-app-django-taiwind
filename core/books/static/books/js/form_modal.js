document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("modal-form");
    const openModalBtn = document.getElementById("open-modal-btn");
    const closeModalBtn = document.getElementById("close-modal-btn");
    const modalOverlay = document.getElementById("modal-overlay");
    // document.getElementById('modal-form').classList.add('hidden');


    openModalBtn.addEventListener("click", function() {
        modal.classList.remove("hidden");
        modalOverlay.classList.remove("hidden");
    });

    closeModalBtn.addEventListener("click", function() {
        modal.classList.add("hidden");
        modalOverlay.classList.add("hidden");
    });

    modalOverlay.addEventListener("click", function() {
        modal.classList.add("hidden");
        modalOverlay.classList.add("hidden");
    });
});