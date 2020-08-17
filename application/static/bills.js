const billsTable = document.querySelector('table');
const deleteDiv = document.querySelector('.delete-div');
const deleteBtn = document.querySelector('.delete-btn');

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
            deleteDiv.classList.remove('d-none');
        } else {
            deleteDiv.classList.add('d-none');
        }
    });
}

// Handle bill deletion
deleteBtn.addEventListener('click', async (e) => {
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
