document.addEventListener('DOMContentLoaded', () => {
    const deleteBtn = document.querySelector('.delete-btn');
    const warningDiv = document.querySelector('.delete-account');
    const cancelBtn = document.querySelector('.cancel-btn');

    deleteBtn.addEventListener('click', () => {
        warningDiv.classList.toggle('d-none');
    });

    cancelBtn.addEventListener('click', () => {
        warningDiv.classList.add('d-none');
    });
});
