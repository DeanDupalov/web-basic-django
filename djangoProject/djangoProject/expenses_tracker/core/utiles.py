from expenses_tracker.app.models import Profile, Expense


def get_profile():
    profile = Profile.objects.first()
    if profile:
        expenses = Expense.objects.all()
        expenses_cost = sum([ex.price for ex in expenses])
        profile.budget_left = profile.budget - expenses_cost
    return profile