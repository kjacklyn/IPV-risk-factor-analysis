from analysis import (
    create_dataset,
    calculate_statistics,
    interpret_results,
    save_results
)

print("Starting IPV Risk-Factor Analysis...")

df = create_dataset()

stats = calculate_statistics(df)

interpretation = interpret_results(
    stats["correlation"],
    stats["sample_size"]
)

print("\nResults")

print("Sample Size:", stats["sample_size"])
print("Average Support:", round(stats["avg_support"], 2))
print("Average Stress:", round(stats["avg_stress"], 2))
print("Correlation:", round(stats["correlation"], 2))

print("\nInterpretation:")
print(interpretation)

save_results(stats, interpretation)

print("\nResults saved to results/ipv_summary.csv")