const savingsTable = document.querySelector('table');
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
toggleDeleteBtnShow(savingsTable, editDeleteDiv);

// Handle bill edit
handleEdit(editBtn, errorsDiv, 'data-savings-entry-id', '/user/savings/edit');

// Handle bill deletion
handleDelete(deleteBtn, 'data-savings-entry-id', '/user/savings/delete');
