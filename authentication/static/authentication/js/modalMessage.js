    document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll('.hidden-message');

    messages.forEach(function(messageElement) {
        const messageContent = messageElement.getAttribute('data-message');
        showModal(messageContent);
    });

    // 显示弹窗函数
    function showModal(message) {
        console.log(message)
        const modal = document.getElementById('messageModal');
        const modalMessage = document.getElementById('modal-message');
        const closeButton = document.querySelector('.close-button');
        console.log(modalMessage)
        modalMessage.textContent = message;
        modal.style.display = "block";

        closeButton.onclick = function() {
            modal.style.display = "none";
        };

        window.onclick = function(event) {
            if (event.target === modal) {
                modal.style.display = "none";
            }
        };
    }
});