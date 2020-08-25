document.addEventListener('DOMContentLoaded', () => {
    /* ######## Hourly Calculator Logic ########## */
    const weeksDiv = document.querySelector('#append-to');
    const addHoursBtn = document.querySelector('#add-hours');
    const hourlyForm = document.querySelector('#gross_form');
    const resultsDiv = document.querySelector('#results');
    let weekNum = 1;

    addHoursBtn.addEventListener('click', (e) => {
        e.preventDefault();

        if (weekNum < 4) {
            // Create all elements for Week form field
            const formGroupRow = document.createElement('div');
            const col = document.createElement('div');
            const label = document.createElement('label');
            const hoursInput = document.createElement('input');
            const info = document.createElement('small');

            // Add classes to each element
            formGroupRow.classList.add('form-group', 'row');
            col.classList.add('col-sm-9');
            label.classList.add('col-sm-2', 'col-form-label');
            hoursInput.classList.add('form-control');
            info.classList.add('text-muted', 'ml-2');

            // Add required attributes
            label.setAttribute('for', 'week');
            hoursInput.setAttribute('name', 'week');
            hoursInput.setAttribute('type', 'number');
            hoursInput.setAttribute('step', '0.01');
            hoursInput.setAttribute('min', '0.00');
            hoursInput.setAttribute('placeholder', 'Enter Hours');

            // Set relevant text for label and small tags
            label.innerText = `Hours: Week ${++weekNum}`;
            info.innerText =
                'Overtime is at 1.5x of base pay for weeks over 40 hours.';

            // Build the form field
            formGroupRow.append(label);
            formGroupRow.append(col);
            col.append(hoursInput);
            col.append(info);

            // Append form field to form
            weeksDiv.append(formGroupRow);
        } else {
            // Show if there are already 4 weeks added to gross pay calculator
            resultsDiv.innerText = 'Only a maximum of 4 weeks is allowed.';
        }
    });

    hourlyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const firstWeek = document.querySelector('input[name="week-1"]');
        const inputs = document.querySelectorAll('input[name="week"]');
        const payRateInput = document.querySelector('#pay-rate');

        // Reinitialize number of weeks and hours array
        weekNum = 1;
        let hours = [];

        // Save payrate and push first week's hours to hours array
        const payRate = payRateInput.value;
        hours.push(firstWeek.value);

        // Push all additional week hours to hours array
        for (const input of inputs) {
            hours.push(input.value);
        }

        // Remove all dynamically added inputs from page
        firstWeek.value = '';
        payRateInput.value = '';
        weeksDiv.innerHTML = '';

        // Make an AJAX call to backend to calculate api and save response
        const { data } = await axios.post('/user/pay/gross/calculate', {
            payRate,
            hours,
        });

        // Display gross pay results on page
        resultsDiv.innerText = `Your total gross pay is: $${data['gross']}`;
    });

    /* ####### Salary Calculator Logic ########### */
    const salaryForm = document.querySelector('#salary_form');
    const salaryResults = document.querySelector('#salary_results');
    const salaryInput = document.querySelector('#salary');
    const payFrequencyOptions = document.querySelectorAll(
        'input[name="pay_frequency"]'
    );

    salaryForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const salary = salaryInput.value;
        let payFrequencyWeeks = 0;
        let payFrequencyText = '';
        for (const option of payFrequencyOptions) {
            if (option.checked) {
                payFrequencyWeeks = Number(option.value);
                payFrequencyText = option.nextElementSibling.innerText;
            }
        }
        if (payFrequencyWeeks === 0) {
            salaryResults.innerText = 'You must select a pay frequency.';
        } else {
            const grossPayResult = (salary / payFrequencyWeeks).toFixed(2);
            salaryResults.innerText = `Your total ${payFrequencyText} gross pay is: $${grossPayResult}`;
        }
    });

    /* ###### Delete paycheck handlers ###### */
    const confirmDeleteBtns = document.querySelectorAll('.confirm-delete');
    const cancelDeleteBtns = document.querySelectorAll('.cancel-delete');
    const paystubsDiv = document.querySelector('.paystubs');

    if (paystubsDiv) {
        paystubsDiv.addEventListener('click', (e) => {
            if (e.target.tagName === 'BUTTON') {
                e.target.parentElement.parentElement.parentElement.nextElementSibling.classList.remove(
                    'd-none'
                );
            } else if (e.target.tagName === 'I') {
                e.target.parentElement.parentElement.parentElement.parentElement.nextElementSibling.classList.remove(
                    'd-none'
                );
            }
        });
    }

    for (const confirmDeleteBtn of confirmDeleteBtns) {
        confirmDeleteBtn.addEventListener('click', async () => {
            const paycheckId = confirmDeleteBtn.getAttribute(
                'data-paycheck-id'
            );

            const { data } = await axios.post('/user/pay/delete', {
                paycheckId,
            });

            if (data['msg'] === 'success') {
                location.reload();
            }
        });
    }

    for (const cancelDeleteBtn of cancelDeleteBtns) {
        cancelDeleteBtn.addEventListener('click', (e) => {
            e.target.parentElement.parentElement.parentElement.classList.add(
                'd-none'
            );
        });
    }
});
