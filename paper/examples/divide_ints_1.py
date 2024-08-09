def divide_ints(a: int, b: int):
    """
    Divide two numbers, raising TypeError or ValueError
    if not ints or denominator is 0, respectively.
    Set a global_error code on error, else return a string
    representing the operation.
    """
    global error_code # pylint: disable=global-statement
    logger.info("error_code=%d", error_code)
    if not isinstance(a, int):
        error_code = -1
        raise TypeError(f"TypeError: {a=} not an int!")
    if not isinstance(b, int):
        error_code = -2
        raise TypeError(f"TypeError: {b=} not an int!")
    if b == 0:
        error_code = -3
        raise ValueError("ValueError: Cannot divide by 0!")
    return f"{a}/{b}={a/b}"

