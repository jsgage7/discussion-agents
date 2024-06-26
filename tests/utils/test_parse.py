"""Unit tests for parsing-related functions."""

from agential.utils.parse import (
    normalize_answer,
    parse_action,
    parse_list,
    parse_numbered_list,
    remove_articles,
    remove_name,
    remove_newline,
    remove_punc,
    white_space_fix,
)


def test_parse_list() -> None:
    """Test parse list function."""
    gt = ["Item 1", "Item 2", "Item 3", "Item 4"]

    x = "1. Item 1\n2. Item 2\n3. Item 3\n\n4. Item 4"
    out = parse_list(x)

    assert len(gt) == len(out)
    for i, j in zip(gt, out):
        assert i == j


def test_parse_numbered_list() -> None:
    """Test parse_numbered_list function."""
    gt = ["Item One", "Item Two", "Item Three"]

    input_text = "1) Item One.\n2) Item Two.\n3) Item Three,\n"
    out = parse_numbered_list(input_text)

    assert len(gt) == len(out)
    for i, j in zip(gt, out):
        assert i == j


def test_remove_name() -> None:
    """Test remove_name function."""
    gt = "Smith"

    x = "John Smith"
    out = remove_name(x, "John")

    assert out == gt


def test_parse_action() -> None:
    """Test parse_action function."""
    # Test with a valid action string.
    valid_string = "ActionType[Argument]"
    assert parse_action(valid_string) == ("ActionType", "Argument")

    # Test with an invalid action string (missing brackets).
    invalid_string = "ActionType Argument"
    assert parse_action(invalid_string) == ("", "")

    # Test with an invalid action string (no action type).
    invalid_string = "[Argument]"
    assert parse_action(invalid_string) == ("", "")

    # Test with an invalid action string (no argument).
    invalid_string = "ActionType[]"
    assert parse_action(invalid_string) == ("", "")


def test_remove_newline() -> None:
    """Test remove_newline function."""
    step = "\n  Step with extra spaces and newlines \n"
    assert remove_newline(step) == "Step with extra spaces and newlines"

    # Test with internal newlines.
    step = "Step\nwith\ninternal\nnewlines"
    assert remove_newline(step) == "Stepwithinternalnewlines"

    # Test with a string that doesn't require formatting.
    step = "Already formatted step"
    assert remove_newline(step) == "Already formatted step"


def test_remove_articles() -> None:
    """Test remove_articles function."""
    sample_text = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )

    result = remove_articles(sample_text)
    expected = (
        "A fox jumped over   fence. An apple was on   table. The quick brown fox."
    )
    assert result == expected, f"Test failed: Expected '{expected}', got '{result}'"


def test_white_space_fix() -> None:
    """Test white_space_fix function."""
    sample_text = "over   fence"
    result = white_space_fix(sample_text)
    assert result == "over fence"


def test_remove_punc() -> None:
    """Test remove_punc function."""
    sample_text = "abcd.,"
    result = remove_punc(sample_text)
    assert result == "abcd"


def test_normalize_answer() -> None:
    """Test normalize_answer function."""
    sample_text = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )

    result = normalize_answer(sample_text)
    expected = "fox jumped over fence apple was on table quick brown fox"
    assert result == expected
