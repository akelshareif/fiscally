const billForm = document.querySelector('form');
const billNameInput = document.querySelector('input[name="bill_name"]');
const billDateInput = document.querySelector('input[name="bill_due_date"]');
const billAmountInput = document.querySelector('input[name="bill_amount"]');
const billsTable = document.querySelector('table');
const editDeleteDiv = document.querySelector('.edit-delete-div');
const deleteBtn = document.querySelector('.delete-btn');
const errorsDiv = document.querySelector('.errors');
const editBtn = document.querySelector('.edit-btn');
let wasEditClicked = false;

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
    wasEditClicked = true;
    const numCheckedBoxes = document.querySelectorAll(
        'input[type="checkbox"]:checked'
    ).length;

    if (numCheckedBoxes > 1) {
        errorsDiv.classList.remove('d-none');
    } else {
        errorsDiv.classList.add('d-none');

        const selectedBill = document.querySelector(
            'input[type="checkbox"]:checked'
        ).parentElement.parentElement;
        const selectedBillId = selectedBill.getAttribute('data-bill-id');

        const rowData = selectedBill.querySelectorAll('td');
        const rowDate = rowData[0].innerText;
        const dateString =
            rowDate.slice(6) +
            '-' +
            rowDate.slice(0, 2) +
            '-' +
            rowDate.slice(3, 5);
        billNameInput.value = rowData[1].innerText;
        billDateInput.value = dateString;
        billAmountInput.value = rowData[2].innerText.slice(1);
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

// Form logic to handle edit/deletion
billForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (wasEditClicked === true) {
        const selectedBill = document.querySelector(
            'input[type="checkbox"]:checked'
        ).parentElement.parentElement;
        const selectedBillId = selectedBill.getAttribute('data-bill-id');

        axios.post('/user/bills/delete', { idArr: [selectedBillId] });
        wasEditClicked = false;
        billForm.submit();
    } else {
        billForm.submit();
    }
});
