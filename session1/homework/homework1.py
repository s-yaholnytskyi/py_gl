class MyClass:
    def __new__(cls, *args):
        for item in args:
            if item not in {"A", "B"}:
                return object.__new__(object)
        return object.__new__(cls)

    def __init__(self, *args):
        self.args = args


if __name__ == "__main__":
    mc1 = MyClass("A")
    mc2 = MyClass("B")
    not_mc1 = MyClass("C")
    not_mc2 = MyClass("B", "C")
    assert isinstance(mc1, MyClass)
    assert isinstance(mc2, MyClass)
    assert not isinstance(not_mc1, MyClass)
    assert not isinstance(not_mc2, MyClass)
