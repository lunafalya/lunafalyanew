# streamlit_calculator.py


def add(x, y):
    """Return the add of num1 and num2.
    >>> add(1,2)
    3.0
    >>> add(2.5, 3.0)
    5.5
    """
    return x + y


def subtract(x, y):
    """Return the subtract of num1 and num2.
    >>> subtract(4,2)
    2.0
    >>> subtract(3.5, 3.0)
    0.5
    """
    return x - y


def multiply(x, y):
    """Return the multiply of num1 and num2.
    >>> multiply(10,20)
    200.0
    >>> multiply(2.0, 3.0)
    6.0
    """
    return x * y


def divide(x, y):
    """Return the divide of num1 and num2.
    >>> divide(40.0,20.0)
    2.0
    >>> divide(6.0, 3.0)
    2.0
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

if __name__ == '_main_':
    import doctest
    doctest.testmod()
