export function toggleDeleteBtnShow(table, editDeleteDiv) {
    if (table) {
        table.addEventListener('click', (e) => {
            if (e.target.getAttribute('type') === 'checkbox') {
                e.target.parentElement.parentElement.classList.toggle(
                    'table-info'
                );
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
}

export function handleEdit(editBtn, errorsDiv, dataAttribute, redirect) {
    editBtn.addEventListener('click', () => {
        const numCheckedBoxes = document.querySelectorAll(
            'input[type="checkbox"]:checked'
        ).length;

        if (numCheckedBoxes > 1) {
            errorsDiv.classList.remove('d-none');
        } else {
            errorsDiv.classList.add('d-none');

            const selectedBillId = document
                .querySelector('input[type="checkbox"]:checked')
                .parentElement.parentElement.getAttribute(dataAttribute);

            window.location.href = `${redirect}/${selectedBillId}`;
        }
    });
}

export function handleDelete(deleteBtn, dataAttribute, postRoute) {
    deleteBtn.addEventListener('click', async () => {
        const selectedBills = document.querySelectorAll(
            'input[type="checkbox"]:checked'
        );

        const idArr = [];
        for (const bill of selectedBills) {
            idArr.push(
                bill.parentElement.parentElement.getAttribute(dataAttribute)
            );
        }

        const { data } = await axios.post(postRoute, { idArr });

        if (data['msg'] === 'success') {
            location.reload();
        }
    });
}
