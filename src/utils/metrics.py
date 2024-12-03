def calculate_roi(initial_balance, final_balance):
    return (final_balance - initial_balance) / initial_balance * 100

def calculate_win_rate(win_count, trade_count):
    if trade_count == 0:
        return 0
    return win_count / trade_count * 100
