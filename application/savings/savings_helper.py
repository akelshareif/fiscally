def recalculate_totals(entries_model, totals_model, curr_user, db):
    user_savings_totals = totals_model.query.filter(
        totals_model.user_id == str(curr_user.id)).all()
    running_total = 0
    for total in user_savings_totals:
        savings_entry = entries_model.query.get(total.savings_id)
        if savings_entry.transaction_type == '+':
            running_total += savings_entry.amount
            total.total = running_total
            db.session.commit()
        else:
            running_total += -savings_entry.amount
            total.toal = running_total
            db.session.commit()
