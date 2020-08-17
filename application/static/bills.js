const billForm = document.querySelector('form');
const billNameInput = document.querySelector('input[name="bill_name"]');
const billDateInput = document.querySelector('input[name="bill_due_date"]');
const billAmountInput = document.querySelector('input[name="bill_amount"]');
const billsTable = document.querySelector('table');
const editDeleteDiv = document.querySelector('.edit-delete-div');
const deleteBtn = document.querySelector('.delete-btn');
const errorsDiv = document.querySelector('.errors');
const editBtn = document.querySelector('.edit-btn');

// Show/hide delete btn and row highlight upon checkbox click
if (billsTable) {
    billsTable.addEventListener('click', (e) => {
        if (e.target.getAttribute('type') === 'checkbox') {
            e.target.parentElement.parentElement.classList.toggle('table-info');
        }

        const numCheckedBoxes = document.querySelectorAll(
            'input[type="checkbox"]:checked'
        ).length;
        if (numCheckedBoxes > 0) {
            editDeleteDiv.classList.remove('d-none');
        } else {
            editDeleteDiv.classList.add('d-none');
        }
    });
}

// Handle bill edit
editBtn.addEventListener('click', async () => {
    const numCheckedBoxes = document.querySelectorAll(
        'input[type="checkbox"]:checked'
    ).length;

    if (numCheckedBoxes > 1) {
        errorsDiv.classList.remove('d-none');
    } else {
        errorsDiv.classList.add('d-none');

        const selectedBillId = document
            .querySelector('input[type="checkbox"]:checked')
            .parentElement.parentElement.getAttribute('data-bill-id');

        window.location.href = `/user/bills/edit/${selectedBillId}`;
    }
});

// Handle bill deletion
deleteBtn.addEventListener('click', async () => {
    const selectedBills = document.querySelectorAll(
        'input[type="checkbox"]:checked'
    );

    const idArr = [];
    for (const bill of selectedBills) {
        idArr.push(
            bill.parentElement.parentElement.getAttribute('data-bill-id')
        );
    }

    const { data } = await axios.post('/user/bills/delete', { idArr });

    if (data['msg'] === 'success') {
        location.reload();
    }
});
