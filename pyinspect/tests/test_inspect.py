import textwrap
from pyinspect.tests import TestCaseWithDebugLogging


class Tests(TestCaseWithDebugLogging):
    def _callFUT(self, cls):
        from io import StringIO
        from pyinspect.inspect import Options
        from pyinspect.inspect import inspect as target_function

        o = StringIO()
        target_function(cls, options=Options(), io=o)
        return o.getvalue()

    def test_shared(self):
        class F:
            def init(self, x, *, y=None):
                self.init_x(x)
                self.init_y(y=y)

            def init_x(self, x):
                self.init_shared()

            def init_y(self, *, y=None):
                self.init_shared()

            def init_shared(self, rec=False):
                if not rec:
                    self.init_shared(rec=True)

        got = self._callFUT(F)
        expected = textwrap.dedent(
            f"""\
        {__name__}:F <- builtins:object
            [method] init(self, x, *, y=None)
                [method] init_x(self, x)
                    [method] init_shared(self, rec=False)
                [method] init_y(self, *, y=None)
                    [method] init_shared(self, rec=False)
        """
        )
        self.assertEqual(got=got.strip("\n"), expected=expected.strip("\n"))

    def test_it(self):
        class F:
            def init(self, x, *, y=None):
                self.init_x(x)
                self.init_y(y=y)

            def init_x(self, x):
                self.init_x_z()

            def init_x_z(self, x):
                pass

            def init_y(self, *, y=None):
                pass

        got = self._callFUT(F)
        expected = textwrap.dedent(
            f"""\
        {__name__}:F <- builtins:object
            [method] init(self, x, *, y=None)
                [method] init_x(self, x)
                    [method] init_x_z(self, x)
                [method] init_y(self, *, y=None)
        """
        )
        self.assertEqual(got=got.strip("\n"), expected=expected.strip("\n"))


if __name__ == "__main__":
    import unittest
    import logging

    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
