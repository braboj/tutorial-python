# Framework: hypothesis
# -----------------------
#
# Check that addition is commutative using property based testing.

from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_addition_is_commutative(a, b):
    assert a + b == b + a
