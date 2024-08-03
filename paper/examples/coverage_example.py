import coverage
cov = coverage.Coverage(None)
with cov.collect():
    try:
        if kwargs:
            this_coverage_info.kwargs = kwargs
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
        else:
            start_time = time.perf_counter()
            result = func(*args)

        logger.debug("No exception :)")
    # There's no way to know ahead of time 
    # what kind of exception func might raise,
    # so catch any of them.
    # pylint: disable-next=broad-exception-caught
    except Exception as e:
        caught_exception = e
    finally:
        end_time = time.perf_counter()