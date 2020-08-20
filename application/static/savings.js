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

// Handle savings goals updates
const savingsGoalForm = document.querySelector('.goal-form');
const savingsGoalUpdateAlert = document.querySelector('.goal-update');
const yesBtn = document.querySelector('.yes-btn');
const noBtn = document.querySelector('.no-btn');

savingsGoalForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // upon submit, if goal is present, show warning, else, submit form
    if (document.querySelector('.savings-goal')) {
        savingsGoalUpdateAlert.classList.remove('d-none');
    } else {
        savingsGoalForm.submit();
    }
});

yesBtn.addEventListener('click', () => {
    savingsGoalForm.submit();
});

noBtn.addEventListener('click', () => {
    savingsGoalUpdateAlert.classList.add('d-none');
});
