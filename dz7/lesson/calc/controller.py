import model_int_operators as model_int
import view
import model_complex_operators as complex

def button_click():
    flag_int_or_complex = view.get_int_or_complex()
    if flag_int_or_complex:
        value_operator = view.get_value_operator(flag_int_or_complex)
        value_a = view.get_value()
        value_b = view.get_value()
        model_int.init(value_a, value_b)
        result = model_int.do_it(value_operator)
    else:
        value_operator = view.get_value_operator(flag_int_or_complex)
        value_a = view.get_value_complex()
        value_b = view.get_value_complex()
        complex.init(value_a, value_b)
        result = complex.do_it(value_operator)
    view.view_data(result, "result")