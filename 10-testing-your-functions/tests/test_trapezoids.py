from trapezoids import trapezint

def hat(x):
    """Simple function that equals x between [0,1], 2-x between [1,2], and zero otherwise"""
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2-x
    return 0


def test_trapezint_hat04():
    """Can we integrate a hat function from 0 to 4 with four trapezoids?"""
    result = trapezint(hat, 0, 4)
    assert result == 1.0
