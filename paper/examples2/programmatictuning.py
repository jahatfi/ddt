if percent_coverage and \
   percent_coverage <= this_metadata.get_percent_covered():
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