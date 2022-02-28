
class Finance:
    """
    This is a class which implements several
    finance formulas using the TDD
    approach:
    """

    def cash_flow(self, income, expenses):
        if income < 0:  
            return
        return income - expenses
