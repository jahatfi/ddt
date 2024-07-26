class RandomSamplingStrategy(TestGenerationStrategy):
  def generate_tests(self):
    self.before_search_start()
    solution = self._chromosome_factory.get_chromosome()
    self._archive.update([solution])
    test_suite = self.create_test_suite(
        self._archive.solutions
    )
    self.before_first_search_iteration(solution)

    while (
        self.resources_left()
        and test_suite.get_fitness() != 0.0
    ):
      new = self._chromosome_factory.get_chromosome()
      self._archive.update([new])
      test_suite = self.create_test_suite(
          self._archive.solutions
      )
      self.after_search_iteration(test_suite)

    self.after_search_finish()
    return self.create_test_suite(
        self._archive.solutions
    )
