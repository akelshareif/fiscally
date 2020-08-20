from application import db
from ..models import SavingsEntry, SavingsTotal


def recalculate_totals(curr_user):
    """ Recalculates totals for each savings_total entry """

    user_savings_totals = SavingsTotal.query.filter(
        SavingsTotal.user_id == str(curr_user.id)).all()

    running_total = 0

    for total in user_savings_totals:
        savings_entry = SavingsEntry.query.get(total.savings_id)
        if savings_entry.transaction_type == '+':
            running_total += savings_entry.amount
            total.total = running_total
            db.session.commit()

        elif savings_entry.transaction_type == '-':
            running_total += (-1*savings_entry.amount)
            total.total = running_total
            db.session.commit()


def savings_progress_percentage(savings_goal, curr_user):
    """ Calculates total savings progress percentage """

    # Get current total, get savings goal, divide, return
    fresh_savings_entries = SavingsEntry.query.filter_by(
        user_id=str(curr_user.id)).all()

    calculated_total = sum([savings.amount if savings.transaction_type ==
                            '+' else (-1*savings.amount) for savings in fresh_savings_entries])

    goal_percentage = 0.00
    if savings_goal:
        goal_percentage = round((calculated_total/savings_goal.amount)*100, 2)

    return goal_percentage


def get_calculated_total(curr_user):
    """ Calculates total from savings """

    fresh_savings_entries = SavingsEntry.query.filter_by(
        user_id=str(curr_user.id)).all()

    calculated_total = sum([savings.amount if savings.transaction_type ==
                            '+' else -savings.amount for savings in fresh_savings_entries])

    return calculated_total
