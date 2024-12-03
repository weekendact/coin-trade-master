import matplotlib.pyplot as plt

def plot_profit_distribution(profits):
    plt.hist(profits, bins=50, alpha=0.7, color="blue")
    plt.title("Profit Percentage Distribution")
    plt.xlabel("Profit (%)")
    plt.ylabel("Frequency")
    plt.show()
