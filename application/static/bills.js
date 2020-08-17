const billsTable = document.querySelector('table');
const trashCan = document.querySelector('.delete-btn');

billsTable.addEventListener('click', (e) => {
    if (e.target.getAttribute('type') === 'checkbox') {
        console.log('clicked');
        e.target.parentElement.parentElement.classList.toggle('table-info');
        trashCan.classList.toggle('d-none');
    }
});
