import {
    toggleDeleteBtnShow,
    handleEdit,
    handleDelete,
} from './editDeleteHandler.js';

document.addEventListener('DOMContentLoaded', () => {
    const billsTable = document.querySelector('table');
    const editDeleteDiv = document.querySelector('.edit-delete-div');
    const deleteBtn = document.querySelector('.delete-btn');
    const errorsDiv = document.querySelector('.errors');
    const editBtn = document.querySelector('.edit-btn');

    // Show/hide delete btn and row highlight upon checkbox click
    toggleDeleteBtnShow(billsTable, editDeleteDiv);

    // Handle bill edit
    handleEdit(editBtn, errorsDiv, 'data-bill-id', '/user/bills/edit');

    // Handle bill deletion
    handleDelete(deleteBtn, 'data-bill-id', '/user/bills/delete');

    /* ##### Paid Button Handler ##### */
    const paidBtn = document.querySelector('.paid');

    paidBtn.addEventListener('click', async () => {
        const selectedBills = document.querySelectorAll(
            'input[type="checkbox"]:checked'
        );

        const idArr = [];

        for (const bill of selectedBills) {
            idArr.push(
                bill.parentElement.parentElement.getAttribute('data-bill-id')
            );
        }

        const { data } = await axios.post('/user/bills/paid', { idArr });

        if (data['msg'] === 'success') {
            location.reload();
        }
    });
});
