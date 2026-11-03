import Lab2


def test_calc_average_temperature():
    input_list = [10, 20, 30, 40]

    result = Lab2.calc_average_temperature(input_list)

    assert (result == 25)


def test_calc_min_max_temperature():
    input_list = [25.5, 30.1, 18.2, 27.0]

    result = Lab2.calc_min_max_temperature(input_list)

    assert (result == [18, 30])


def test_calc_min_max_temperature_negative():
    input_list = [3, -5, 0, 12]

    result = Lab2.calc_min_max_temperature(input_list)

    assert (result == [-5, 12])


def test_calc_median_temperature_odd():
    input_list = [30, 10, 20]

    result = Lab2.calc_median_temperature(input_list)

    assert (result == 20)


def test_calc_median_temperature_even():
    input_list = [40, 10, 30, 20]

    result = Lab2.calc_median_temperature(input_list)

    assert (result == 25)