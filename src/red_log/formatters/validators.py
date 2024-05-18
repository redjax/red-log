import typing as t


def validate_str_input(
    _str: str = None, valid_inputs: list[t.Any] | None = None
) -> str:
    assert _str, ValueError("_str cannot be None")
    assert isinstance(_str, str), TypeError(
        f"Invalid type for _str, must be a string. Got type: ({type(_str)})"
    )

    if valid_inputs:
        ## Ensure input string is in list of valid inputs.
        assert _str in valid_inputs, ValueError(
            f"Invalid input '{_str}'. Must be one of: {valid_inputs}"
        )

    return _str
