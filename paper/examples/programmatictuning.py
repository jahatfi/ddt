# Check if this decorator should be applied based on the
# provided percent_coverage or sample_count variables
if percent_coverage and \
   percent_coverage <= this_metadata.percent_covered(0):
    # Desired percent coverage already achieved: skip
    # logging statements here
    # Since this decorator is effectively nullified now,
    # do NOT try/catch/raise any exceptions.
    return func(*args, **kwargs)

if sample_count and \
   sample_count <= len(this_metadata.coverage_io):
    # Desired number of samples already achieved: skip
    # logging statements here
    # Since this decorator is effectively nullified now,
    # do NOT try/catch/raise any exceptions.
    return func(*args, **kwargs)