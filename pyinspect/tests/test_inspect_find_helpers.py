from pyinspect.tests import TestCaseWithDebugLogging


class Tests(TestCaseWithDebugLogging):
    def _callFUT(self, cls):
        from pyinspect.inspect import collect_methods, Options
        from pyinspect.inspect import find_calling_structure as target_function
        methods = collect_methods(cls, options=Options())
        return target_function(cls, methods)

    def test_simple(self):
        class F:
            def m(self, x, y):
                self.m_x(x, self.m_y(y))

            def m_x(self, x, my):
                pass

            def m_y(self, y):
                pass

        got = self._callFUT(F)
        expected = {"m": ["m_x", "m_y"], "m_x": [], "m_y": []}
        self.assertDictEqual(got=got, expected=expected)

    def test_nested(self):
        class F:
            def init(self, x, *, y=None):
                self.init_x(x)

            def init_x(self, x):
                self.init_x_z()

            def init_x_z(self, x):
                pass

        got = self._callFUT(F)
        expected = {"init": ["init_x"], "init_x": ["init_x_z"], "init_x_z": []}
        self.assertDictEqual(got=got, expected=expected)


if __name__ == "__main__":
    import unittest
    import logging
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
