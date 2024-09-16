if "pytest" in sys.modules:
    logger.debug("pytest is loaded; don't decorate when under a test")
    result = func(*args, **kwargs)
    return result

function_calls: dict[str, int] = defaultdict(int)

# The code blocks below (before the call to do_the_decorator_thing)
# prevent application of this decorator in cyclical calls, e.g.
# A -> B -> A # Does not apply to decorator in 2nd call to A
for f in inspect.stack()[::-1]:
    this_frame = inspect.getframeinfo(f[0])
    function_calls[this_frame.function] += 1

max_func_call_vals = max(function_calls.values())
if function_name not in recursion_depth_per_decoratee:
    recursion_depth_per_decoratee[function_name] = max_func_call_vals

elif 1 < max_func_call_vals >= recursion_depth_per_decoratee[function_name]:
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.critical(e)
        raise e

# At this point we know we aren't in a function call graph cycle.