from mock import (
    Mock,
    patch,
)

from ducker import main

@patch('ducker.main.prompt_for_text', return_value="Great!")
def test_main_loop_no_input(mocked_input):
    main.run()
    pass
