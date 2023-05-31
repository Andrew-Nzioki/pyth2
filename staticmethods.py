class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")
    @classmethod
    def class_method(cls):
        print(f" called a class mehod of {cls}")
    @staticmethod
    def static_method():
        print("called static_method")

test=ClassTest()
test.instance_method()

ClassTest.class_method()