from pages.inputs_page import InputsPage

def test_field(driver):
    inputs_page =  InputsPage(driver)
    inputs_page.open()
    inputs_page.enter_number("123")

    assert inputs_page.get_input_values() == "123"


