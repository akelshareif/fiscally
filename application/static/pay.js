const weeks_div = document.querySelector('#append-to');
const add_hours_btn = document.querySelector('#add-hours');
const gross_form = document.querySelector('#gross_form');
const results_div = document.querySelector('#results');
let week_num = 1;

add_hours_btn.addEventListener('click', (e) => {
    e.preventDefault();

    if (week_num < 4) {
        const row = document.createElement('div');
        const col = document.createElement('div');
        const label = document.createElement('label');
        const input = document.createElement('input');
        const info = document.createElement('small');

        row.classList.add('form-group', 'row');
        col.classList.add('col-sm-9');
        label.classList.add('col-sm-2', 'col-form-label');
        input.classList.add('form-control');
        info.classList.add('text-muted', 'ml-2');

        label.setAttribute('for', 'week');
        input.setAttribute('name', 'week');
        input.setAttribute('type', 'number');
        input.setAttribute('step', '0.01');
        input.setAttribute('min', '0.00');

        label.innerText = `Week ${++week_num} Hours`;
        info.innerText =
            'Overtime is added at a rate of 1.5x of base pay for weeks over 40 hours.';

        col.append(input);
        col.append(info);
        row.append(label);
        row.append(col);

        weeks_div.append(row);
    } else {
        results_div.innerText = 'Only a maximum of 4 weeks is allowed.';
    }
});

gross_form.addEventListener('submit', async (e) => {
    e.preventDefault();
    week_num = 1;
    const first_input = document.querySelector('input[name="week-1"]');
    const inputs = document.querySelectorAll('input[name="week"]');
    const pay_rate_input = document.querySelector('#pay-rate');
    let hours = [];
    pay_rate = pay_rate_input.value;
    hours.push(first_input.value);
    first_input.value = '';
    pay_rate_input.value = '';
    for (const input of inputs) {
        hours.push(input.value);
        input.parentElement.parentElement.remove();
    }
    const { data } = await axios.post('/user/pay/gross/calculate', {
        pay_rate,
        hours,
    });
    results_div.innerText = `Your total gross pay is: $${data['gross']}`;
});
