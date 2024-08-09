# Use a global variable to test that unit_test_generator_decorator
# considers global variables when generating unit tests
error_code = 0

def main():
    """
    Call division function
    """
    start = time.perf_counter()
    a_list = [6, 3,"10", 8, [], {}, 4]
    b_list = [2, 0, 2, [], 2, 3, set()]
    global error_code  # pylint: disable=global-statement
    for a, b in zip(a_list, b_list):
        try:
            logger.info("-"*80)
            error_code = 0
            try:
                logger.info("Trying divide_ints(%s, %s)", repr(a), repr(b))
            except TypeError as e:
                logger.info(e)
            print(f"divide_ints({a}, {b})={divide_ints(a, b)}")
        except (ValueError, TypeError) as e:
            logger.error("%s: %s", type(e),str(e))
        logger.info("error_code=%d", error_code)

    generate_all_tests_and_metadata(Path('.'), Path('.'))
    print(f"Took {time.perf_counter()-start} seconds")

divide_ints = unit_test_generator_decorator(percent_coverage=110)(divide_ints)

main()    