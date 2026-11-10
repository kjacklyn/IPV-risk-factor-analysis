import pandas as pd


def create_dataset():
    data = {
        "Participant": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Support_Score": [8, 7, 6, 5, 4, 3, 8, 2, 7, 5],
        "Stress_Score": [3, 4, 5, 6, 7, 9, 2, 8, 3, 6]
    }

    return pd.DataFrame(data)


def calculate_statistics(df):

    sample_size = len(df)

    avg_support = df["Support_Score"].mean()
    avg_stress = df["Stress_Score"].mean()

    correlation = df["Support_Score"].corr(
        df["Stress_Score"]
    )

    return {
        "sample_size": sample_size,
        "avg_support": avg_support,
        "avg_stress": avg_stress,
        "correlation": correlation
    }


def interpret_results(correlation, sample_size):

    if correlation < -0.7:
        return (
            f"In this hypothetical sample of {sample_size} participants, "
            f"higher social support was associated with lower stress."
        )

    elif correlation > 0.7:
        return (
            f"In this hypothetical sample of {sample_size} participants, "
            f"higher social support was associated with higher stress."
        )

    else:
        return (
            f"In this hypothetical sample of {sample_size} participants, "
            f"the relationship between support and stress was relatively weak."
        )


def save_results(stats, interpretation):

    results = pd.DataFrame({
        "Statistic": [
            "Sample Size",
            "Average Support Score",
            "Average Stress Score",
            "Correlation",
            "Interpretation"
        ],
        "Value": [
            stats["sample_size"],
            stats["avg_support"],
            stats["avg_stress"],
            stats["correlation"],
            interpretation
        ]
    })

    results.to_csv(
        "results/ipv_summary.csv",
        index=False
    )