from src.analysis import (
    create_dataset,
    calculate_statistics,
    interpret_results
)


def test_dataset_size():
    df = create_dataset()
    assert len(df) == 10


def test_average_support():
    df = create_dataset()
    stats = calculate_statistics(df)

    assert round(stats["avg_support"], 2) == 5.50


def test_average_stress():
    df = create_dataset()
    stats = calculate_statistics(df)

    assert round(stats["avg_stress"], 2) == 5.30


def test_correlation():
    df = create_dataset()
    stats = calculate_statistics(df)

    assert round(stats["correlation"], 2) == -0.96


def test_interpretation():
    interpretation = interpret_results(-0.96, 10)

    assert "lower stress" in interpretation