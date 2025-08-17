def get_dollar_exchange(amount):
   #if isinstance (amount, str):
    if not isinstance(amount, (int, float)):
        raise ValueError("amount must be number")
    if amount < 0:
        raise ValueError("Amount cannot be zero")
    conversion = amount * 1550
    changed_currency = "₦{:,.2f}".format(conversion)
    return changed_currency