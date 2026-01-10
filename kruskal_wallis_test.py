"""
Lean Six Sigma - Kruskal-Wallis Test

This script performs a Kruskal-Wallis test to analyze the impact of
training on warehouse operators' productivity.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from bioinfokit.analys import stat
import statsmodels.graphics.gofplots as sm
import pingouin as pg


def load_data():
    """Load sewing/VAS data from Excel file."""
    df = pd.read_excel('data/df_sewing.xlsx')
    return df


def create_sample_data():
    """Create sample data for demonstration."""
    np.random.seed(42)

    # Trained operators are faster (lower time)
    trained_times = np.random.normal(85, 10, 28).astype(int)
    untrained_times = np.random.normal(95, 12, 28).astype(int)

    data = []
    for i, t in enumerate(trained_times):
        data.append({'Operator': f'Op{i+1}', 'Training': 'Yes', 'Time': t})
    for i, t in enumerate(untrained_times):
        data.append({'Operator': f'Op{i+29}', 'Training': 'No', 'Time': t})

    return pd.DataFrame(data)


def plot_boxplot(df):
    """Create and save boxplot of time distribution by training status."""
    plt.figure(figsize=(8, 6))
    ax = sns.boxplot(x='Training', y='Time', data=df, color='#99c2a2')
    ax = sns.swarmplot(x="Training", y="Time", data=df, color='#7d0013')
    plt.ylabel('Time per batch of 30 labels (sec)')
    plt.title('Productivity by Training Status')
    plt.tight_layout()
    plt.savefig('boxplot_training.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: boxplot_training.png")


def plot_residuals(df):
    """Create and save residual plots for ANOVA."""
    # ANOVA model
    res = stat()
    res.anova_stat(df=df, res_var='Training', anova_model='Time ~ C(Training)')

    # QQ-plot
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # QQ plot
    sm.qqplot(res.anova_std_residuals, line='45', ax=axes[0])
    axes[0].set_xlabel("Theoretical Quantiles")
    axes[0].set_ylabel("Standardized Residuals")
    axes[0].set_title("Q-Q Plot")

    # Histogram
    axes[1].hist(res.anova_model_out.resid, bins='auto', histtype='bar', ec='k')
    axes[1].set_xlabel("Residuals")
    axes[1].set_ylabel('Frequency')
    axes[1].set_title("Histogram of Residuals")

    # Residuals plot
    axes[2].plot(res.anova_model_out.resid, '-o')
    axes[2].set_xlabel("Observation")
    axes[2].set_ylabel('Residuals')
    axes[2].set_title("Residuals vs Order")

    plt.tight_layout()
    plt.savefig('residual_plots.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: residual_plots.png")


def perform_analysis(df):
    """Perform statistical analysis."""
    # Split data by training status
    train_yes = df[df['Training'] == 'Yes']['Time'].values
    train_no = df[df['Training'] == 'No']['Time'].values

    # Descriptive statistics
    df_analysis = df[df['Training'] == 'Yes'][['Time']].describe()
    df_analysis.columns = ['Yes']
    df_analysis['No'] = df[df['Training'] == 'No'][['Time']].describe()
    df_analysis.to_csv('data/df_test.csv')

    # Welch's ANOVA
    welch_result = pg.welch_anova(dv='Time', between='Training', data=df)

    # Kruskal-Wallis test
    kruskal_stat, kruskal_p = stats.kruskal(train_no, train_yes)

    return {
        'descriptive': df_analysis,
        'welch_anova': welch_result,
        'kruskal_stat': kruskal_stat,
        'kruskal_p': kruskal_p,
        'train_yes': train_yes,
        'train_no': train_no
    }


def display_results(df, results):
    """Display analysis results."""
    print("=" * 60)
    print("KRUSKAL-WALLIS TEST - TRAINING IMPACT ANALYSIS")
    print("=" * 60)

    print(f"\n--- DATA SUMMARY ---")
    print(f"Total Records: {len(df):,}")
    print(f"Trained: {len(results['train_yes'])}")
    print(f"Not Trained: {len(results['train_no'])}")

    print(f"\n--- DESCRIPTIVE STATISTICS ---")
    print(results['descriptive'])

    print(f"\n--- MEAN COMPARISON ---")
    print(f"Trained Mean: {results['train_yes'].mean():.2f} seconds")
    print(f"Not Trained Mean: {results['train_no'].mean():.2f} seconds")
    diff = results['train_no'].mean() - results['train_yes'].mean()
    print(f"Difference: {diff:.2f} seconds")

    print(f"\n--- WELCH'S ANOVA ---")
    print(results['welch_anova'].to_string(index=False))

    print(f"\n--- KRUSKAL-WALLIS TEST ---")
    print(f"H-statistic: {results['kruskal_stat']:.4f}")
    print(f"p-value: {results['kruskal_p']:.6f}")

    alpha = 0.05
    print(f"\n--- CONCLUSION (α = {alpha}) ---")
    if results['kruskal_p'] < alpha:
        print("REJECT the null hypothesis.")
        print("There IS a statistically significant difference in productivity")
        print("between trained and untrained operators.")
        if diff > 0:
            print(f"Training REDUCES time by {diff:.1f} seconds on average.")
    else:
        print("FAIL TO REJECT the null hypothesis.")
        print("There is NO statistically significant difference in productivity")
        print("between trained and untrained operators.")


def main():
    """Main function for Kruskal-Wallis analysis."""
    # Load or create data
    try:
        df = load_data()
        print("Data loaded from file.")
    except FileNotFoundError:
        print("Data file not found. Using sample data.")
        df = create_sample_data()

    # Create visualizations
    plot_boxplot(df)
    plot_residuals(df)

    # Perform analysis
    results = perform_analysis(df)

    # Display results
    display_results(df, results)


if __name__ == "__main__":
    main()
