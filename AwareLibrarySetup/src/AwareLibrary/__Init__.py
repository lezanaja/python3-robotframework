from .Face import Face
from .LeftHand import LeftHand


class AwareLibrary(Face, LeftHand):
    def __init__(self):
        Face.__init__(self)
        LeftHand.__init__(self)

    def get_hello_world(self):
        """Verifies that element ``locator`` is found on the current page.

        See the `Locating elements` section for details about the locator
        syntax.

        The ``message`` argument can be used to override the default error
        message.

        The ``limit`` argument can used to define how many elements the
        page should contain. When ``limit`` is ``None`` (default) page can
        contain one or more elements. When limit is a number, page must
        contain same number of elements.

        See `Page Should Contain` for explanation about the ``loglevel``
        argument.

        Examples assumes that locator matches to two elements.
        | `Page Should Contain Element` | div_name | limit=1    | # Keyword fails.                  |
        | `Page Should Contain Element` | div_name | limit=2    | # Keyword passes.                 |
        | `Page Should Contain Element` | div_name | limit=none | # None is considered one or more. |
        | `Page Should Contain Element` | div_name |            | # Same as above.                  |

        The ``limit`` argument is new in SeleniumLibrary 3.0.
        """
        return "Helloworld"

    def get_method_void(self):
        print('Void')

    def get_method_with_parameter(self, id):
        print('id:' + str(id))

    def get_method_with_return(self):
        return 'Aware'
