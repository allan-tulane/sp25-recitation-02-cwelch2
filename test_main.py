from main import *

def test_simple_work():
    """ done. """
    assert simple_work_calc(10, 2, 2) == 36
    assert simple_work_calc(20, 3, 2) == 230
    assert simple_work_calc(30, 4, 2) == 650
    # Additional Test Cases
    assert simple_work_calc(15, 5, 3) == 65
    assert simple_work_calc(25, 4, 2) == 617
    assert simple_work_calc(40, 3, 2) == 730

def test_work():
    assert work_calc(10, 2, 2, lambda n: 1) == 15
    assert work_calc(20, 1, 2, lambda n: n * n) == 530
    assert work_calc(30, 3, 2, lambda n: n) == 300
    # Additional Tests Cases
    assert work_calc(16, 2, 2, lambda n: n + 1) == 111
    assert work_calc(8, 3, 2, lambda n: n) == 65
    assert work_calc(12, 4, 3, lambda n: n * 2) == 88



def test_compare_work():
    # curry work_calc to create multiple work
    # functions that can be passed to compare_work

    # Work function 1: f(n) = n^0.5
    work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x ** 0.5)

    # Work function 2: f(n) = n^2
    work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x ** 2)

    # Compare work for the two functions
    res = compare_work(work_fn1, work_fn2)
    print_results(res)
test_compare_work()


def test_compare_span():
    # Case 1: c < log_b 1 (Not very practical but included for completeness)
    span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x ** 0.5)

    # Case 2: c = log_b 1
    span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: x)

    # Case 3: c > log_b 1
    span_fn3 = lambda n: span_calc(n, 2, 2, lambda x: x ** 2)

    # Compare span for the three functions
    res = compare_work(span_fn1, span_fn2, sizes=[10, 100, 1000, 10000])
    print("Comparison for c < log_b 1 and c = log_b 1:")
    print_results(res)

    res = compare_work(span_fn2, span_fn3, sizes=[10, 100, 1000, 10000])
    print("\nComparison for c = log_b 1 and c > log_b 1:")
    print_results(res)


test_compare_span()
