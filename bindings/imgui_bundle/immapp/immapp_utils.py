# Part of ImGui Bundle - MIT License - Copyright (c) 2022-2023 Pascal Thomet - https://github.com/pthom/imgui_bundle
from typing import Callable, Any, Tuple, Optional
import imgui_bundle
from imgui_bundle import immapp, hello_imgui


def static(**kwargs: Any) -> Any:
    """A decorator that adds static variables to a function
    :param kwargs: list of static variables to add
    :return: decorated function

    Example:
        @static(x=0, y=0)
        def my_function():
            # static vars are stored as attributes of "my_function"
            # we use static as a more readable synonym.
            static = my_function

            static.x += 1
            static.y += 2
            print(f"{static.f.x}, {static.f.x}")

        invoking f three times would print 1, 2 then 2, 4, then 3, 6

    Static variables are similar to global variables, with the same shortcomings!
    Use them only in small scripts, not in production code!
    """

    def wrapper(function: Callable[[Any], Any]):
        for key, value in kwargs.items():
            setattr(function, key, value)
        return function

    return wrapper


def run_anon_block(function: Callable[[], None]):
    """Decorator for anonymous block

    This enables you to emulate CC++ anonymous blocks.
    In the example below, _win_code() is an anonymous block which is evaluated right after its definition.
    Its presence makes it possible to indent parts of the code (for example, the code responsible for the widgets
     inside a window)

        imgui.begin("My window")
        @run_anon_block
        def _win_code():
            imgui.text("What is your name")
            changed_f, first_name = imgui.input_text("First name")
            changed_l, last_name = imgui.input_text("Last name")
            # ...
        imgui.end()

    """
    function()  # type: ignore
