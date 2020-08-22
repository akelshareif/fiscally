from decimal import Decimal


def calculate_gross_pay(pay_data):
    """ Calculates the total gross pay including overtime pay """

    rate = Decimal(pay_data['payRate']
                   ) if pay_data['payRate'] != '' else Decimal(0.00)
    hours_list = [hours for hours in pay_data['hours'] if hours != '']

    overtime_hours_list = [
        Decimal(hours)-40 for hours in hours_list if Decimal(hours)-40 >= 0]
    overtime_pay = [Decimal(hours)*rate*Decimal(1.5)
                    for hours in overtime_hours_list]

    base_pay = [
        40*rate if Decimal(hours) > 40 else Decimal(hours)*rate for hours in hours_list]

    base_total = sum(base_pay)
    overtime_total = sum(overtime_pay)

    pay_total = round(base_total+overtime_total, 2)
    return '{:.2f}'.format(pay_total)
