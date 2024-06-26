"""Unit tests for Reflexion eval."""

from agential.cog.eval.reflexion import EM


def test_em() -> None:
    """Test EM function."""
    sample_answer = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )
    sample_key = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )
    result = EM(sample_answer, sample_key)
    assert result

    sample_answer = (
        "1A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )
    sample_key = (
        "A fox jumped over the fence. An apple was on the table. The quick brown fox."
    )
    result = EM(sample_answer, sample_key)
    assert not result
