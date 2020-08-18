const billsTable = document.querySelector('table');
const editDeleteDiv = document.querySelector('.edit-delete-div');
const deleteBtn = document.querySelector('.delete-btn');
const errorsDiv = document.querySelector('.errors');
const editBtn = document.querySelector('.edit-btn');

import {
    toggleDeleteBtnShow,
    handleEdit,
    handleDelete,
} from './editDeleteHandler.js';

// Show/hide delete btn and row highlight upon checkbox click
toggleDeleteBtnShow(billsTable, editDeleteDiv);

// Handle bill edit
handleEdit(editBtn, errorsDiv, 'data-bill-id', '/user/bills/edit');

// Handle bill deletion
handleDelete(deleteBtn, 'data-bill-id', '/user/bills/delete');
