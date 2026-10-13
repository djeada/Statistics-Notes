import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

SEED = 42


def generate_apple_weights(rng, mean, std_dev, size):
    """Generate random apple weights (grams) for one farm from a normal distribution."""
    return rng.normal(loc=mean, scale=std_dev, size=size)


def anova_table(*groups):
    """Return SST (treatment), SSE, SSTotal, MST, MSE, F and p-value computed by hand."""
    all_y = np.concatenate(groups)
    grand_mean = all_y.mean()
    k, n_total = len(groups), all_y.size
    sst = sum(g.size * (g.mean() - grand_mean) ** 2 for g in groups)
    sse = sum(((g - g.mean()) ** 2).sum() for g in groups)
    mst, mse = sst / (k - 1), sse / (n_total - k)
    f_stat = mst / mse
    p_value = stats.f.sf(f_stat, k - 1, n_total - k)
    return sst, sse, sst + sse, mst, mse, f_stat, p_value


def main():
    rng = np.random.default_rng(SEED)

    farm_a = generate_apple_weights(rng, 148, 10, 50)
    farm_b = generate_apple_weights(rng, 150, 10, 50)
    farm_c = generate_apple_weights(rng, 152, 10, 50)

    # One-way ANOVA with scipy, cross-checked against the sums-of-squares table
    f_stat, p_value = stats.f_oneway(farm_a, farm_b, farm_c)
    sst, sse, sstotal, mst, mse, f_hand, p_hand = anova_table(farm_a, farm_b, farm_c)
    assert np.isclose(f_stat, f_hand) and np.isclose(p_value, p_hand)

    print(f"SST = {sst:.1f}, SSE = {sse:.1f}, SSTotal = {sstotal:.1f}")
    print(f"MST = {mst:.1f}, MSE = {mse:.1f}")
    print(f"F-statistic: {f_stat:.2f}")
    print(f"p-value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print("Result: Reject the null hypothesis.")
        print("There is a significant difference in the average apple weights between the farms.")
    else:
        print("Result: Fail to reject the null hypothesis.")
        print("There is no significant difference in the average apple weights between the farms.")

    # Boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot([farm_a, farm_b, farm_c], patch_artist=True,
                boxprops=dict(facecolor="skyblue"))
    plt.xticks([1, 2, 3], ["Farm A", "Farm B", "Farm C"])
    plt.title("Boxplots of Apple Weights for Three Farms", fontsize=14)
    plt.ylabel("Weight (g)", fontsize=12)
    plt.grid(True, axis="y", linestyle="--", alpha=0.7)
    plt.show()

    # Histograms
    plt.figure(figsize=(10, 6))
    plt.hist(farm_a, bins=10, alpha=0.5, label="Farm A", color="blue")
    plt.hist(farm_b, bins=10, alpha=0.5, label="Farm B", color="green")
    plt.hist(farm_c, bins=10, alpha=0.5, label="Farm C", color="red")
    plt.title("Histogram of Apple Weights by Farm", fontsize=14)
    plt.xlabel("Weight (g)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.legend(loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()


if __name__ == "__main__":
    main()
