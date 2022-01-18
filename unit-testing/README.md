# Unit Testing in Python

## Introduction to Testing

The goal of testing isn't just to find bugs but to find them quickly. Leaving bugs unfound and unresolved can lead to massive consequences. [Some of the most infamuos bugs that have ever been found in software](https://en.wikipedia.org/wiki/List_of_software_bugs)

## Assert Statement

The `assert` statement provided by python makes it easy to test code. It's used to test whether a condition is met or not. If not, an `AssertionError` is raised by this statement with an optional error message.

The syntax looks as follows:

```py
assert <condition>, "Message if condition is not met"
```

Eg:

```py
def times_ten(num: int) -> int:
  return num * 100

result = times_ten(20)
assert result === 200, "Expected times_ten(20) to be equal to 200, instead got" + str(result)
```

An `assert` statement is a quick and powerful way to verify that a program is in the correct state.

## Unit Testing

In programming, unit tests are used to test multiple small units of code. These units could be functions, loops, conditionals, or even variables. A unit test validates a single behavior and will make sure that all the units of a program are functioning correctly.

Let's say we wanted to test a function(a single unit). A unit test may contain multiple test cases. A **test case** validates that a specific set of inputs produces some specific output for a unit that we are trying to test.

Eg:

```py
# The unit we want to test
def times_ten(number):
    return number * 100

# A unit test function with a single test case
def test_multiply_ten_by_zero():
    assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'

# Other test cases
def test_multiply_ten_by_one_million():
    assert times_ten(1000000) == 10000000, 'Expected times_ten(1000000) to return 10000000

def test_multiply_ten_by_negative_number():
    assert times_ten(-10) == -100, 'Expected times_ten(-10) to return -100'
```

Now we have several test cases for a wide variety of inputs: a large number, a negative number, and zero. We can create as many test cases as we see fit for a single unit, and we should try to test all the unique types of inputs our unit will work with.

## Python's unittest Framework

The above described method of writing tests is not only tedious but also not concentrated and atomic. Each function needs to be called individually to run every single test case. Also, if one test failed, none of the other tests following it will be run.

Python provides a framework which solves all these problems with writing tests. This framework lives in the `unittest` module which is part of the standard library.

```py
import unittest

# The rest of our program...
```

The `unittest` module provides us with a test runner. A test runner is a component which collects and executes all the tests and then provides the results to the user. The framework also provides many other tools such as grouping, setup, teardown, skipping and other features.

It follows the syntax given below:

```py
# Importing unittest framework
import unittest

# Function that gets tested
def times_ten(number):
    return number * 100

# Test class
class TestTimesTen(unittest.TestCase):
    def test_multiply_ten_by_zero(self):
        self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

    def test_multiply_ten_by_one_million(self):
        self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

    def test_multiply_ten_by_negative_number(self):
        self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')

# Run the tests
unittest.main()
```

## Assert Methods

1. `assertEqual()` -- takes two arguments and checks if they're equal else fails.
2. `assertIn()` -- takes two arguments and checks if one is part of the other, `self.assertIn(value, container)`
3. `assertTrue()` -- takes one argument and checks if it evaluates to `True`, else fails.
4. `assertLess()` -- takes two arguments and checks the first argument is less then the second else fails
5. `assertAlmostEqual()` -- takes two arguments and checks that their difference when rounded to 7 decimal places is zero. In terms of `assert` statement: `assert round(.22 - .225, 7) == 0`
6. `assertRaises()` -- takes a specific exception as the first argument, takes a function as the second, and an arbitrary number of arguments as the rest.

It calls the function and checks if an exception is raised as a result. The test passes if an exception is raised, is an error if another exception is raised or fails if there is no exception raised. This method can also be used with user defined exceptions.

7. `assertWarns()` -- takes a warning as the first argument, a function as the second, and an arbitrary number for the rest. It calls the function and checks if the warning occures else fails.

## Parameterizing Tests

To decrease repetition, python can allow passing params to the test. By parameterizing, we can test a large number of inputs for a single test.

To accomplish test parameterization, the `unittest` framework provides us with the `subTest` context manager.

```py
import unittest

# The function we want to test
def times_ten(number):
    return number * 100

# Our test class
class TestTimesTen(unittest.TestCase):

    # A test method
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest():
          # with self.subTest(num) can also be used for more clear test results since it'll
          # show where exactly the test broke
                expected_result = num * 10
                message = 'Expected times_ten(' + str(num) + ') to return ' + str(expected_result)
                self.assertEqual(times_ten(num), expected_result, message)

```

By using `subTest`, each loop iteration is considered as it's own individual test. Python will run the code inside the context manager on each iteration and if one fails, it will return the failure as a separate test case failure.

NOTE: Now, if we want to modify the test coverage, we can simply modify the list that the loop iterates over.

## Test Fixtures

One of the most important principles of testing is that the tests occur in known state. If the condition in which a test runs are not controlled, then our results could turn out to be false negatives(invalid failed results) or false positives(invalid passed results).

To solve this problem, Test Fixtures are used. A test fixture is a mechanism for ensuring proper test setup (putting tests in a known state) and test teardown (restoring the state prior to the test running). Test fixtures guarantee that our tests are running in known conditions, and thus the results are reliable.

The `unittest` framework automatically identifies setup and teardown methods based on their names. A method named `setUp` runs before each test case and a method named `tearDown` runs after each test case.

```py
def power_cycle_device():
    print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
    def setUp(self):
        power_cycle_device()

    def test_feature_a(self):
        print('Testing Feature A')

    def test_feature_b(self):
        print('Testing Feature B')

    def tearDown(self):
        power_cycle_device()

# output
# Power cycling ...
# Testing Feature A
# Power cycling ...
# Power cycling ...
# Testing Feature B
# Power cycling ...
```

Another scenario could be that the setup and teardown methods needs to be run only once: once before all the tests start and once after all the tests are done. In that case, declare the `setUp` and `tearDown` methods as Class Methods.

```py
def power_cycle_device():
    print('Power cycling bluetooth device...')

class BluetoothDeviceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        power_cycle_device()

    def test_feature_a(self):
        print('Testing Feature A')

    def test_feature_b(self):
        print('Testing Feature B')

    @classmethod
    def tearDownClass(cls):
        power_cycle_device()


# output
# Power cycling ...
# Test Feature A
# Test Feature B
# Power cycling ...
```

## Skipping Tests

Sometimes some tests need to be skipped due to environment changes or to be run in some particular context. Eg: a test might only have to be run on Windows or only on Linux. So, a windows test should be skipped on Linux.

The `unittest` framework provides two different ways to skip tests:

1. The `@unittest` skip decorator
2. The `skipTest()` method

### `@unittest` skip decorator

```py
import sys

class LinuxTests(unittest.TestCase):

    @unittest.skipUnless(sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_linux_feature(self):
        print("This test should only run on Linux")

    @unittest.skipIf(not sys.platform.startswith("linux"), "This test only runs on Linux")
    def test_other_linux_feature(self):
        print("This test should only run on Linux")
```

The `skipUnless()` option skips the test if the condition evaluates to `False`.
The `skipIf()` options skips the test if the condition evaluates to `True`.

Both share common requirements. Firstly, both of these skip decorators are prefaced with `@unittest` to denote the decorator pattern. They both take a condition as a first argument, followed by a string message as the second.

### `skipTest()` method

```py
import sys

class LinuxTests(unittest.TestCase):

    def test_linux_feature(self):
        if not sys.platform.startswith("linux"):
            self.skipTest("Test only runs on Linux")
```

Here we call `self.skipTest()` from within the test function itself. It takes a single string message as its argument and always causes the test to be skipped when called.

Skip decorators are slightly more convenient and make it easy to see under what conditions the test is skipped. When the conditions for skipping a test are too complicated to pass into a skip decorator, the skipTest method is the recommended alternative

## Expected Failures

Sometimes we have a test that we know will fail. This could happen when a feature has a known bug or is designed to fail on purpose. In this case, we wouldn’t want an expected failure to cloud our test results. Rather than simply skipping the test, `unittest` provides a way to mark tests as expected failures. Expected failures are counted as passed in our test results. If the test passes when we expected it to fail, then it is marked as failed in test results.

So, the tests is counted as pass if it failed and failed if the test passes.

```py
class FeatureTests(unittest.TestCase):

    @unittest.expectedFailure
    def test_broken_feature(self):
        raise Exception("This test is going to fail")
```
