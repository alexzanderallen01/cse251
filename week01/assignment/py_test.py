class MyParentClass():
    def __init__(obj, value: int, values: list, name: str):
        obj.value = value
        obj.values = values
        obj.name = name
    def get_value_using_index(obj, key):
        return obj.values[key]

obj = MyParentClass(1, [5, 6, 7], "3")

# 8) TODO write a class called 'MyChildClass'. The class should extend the MyParentClass.
#      The constructor should take four parameters:
#      - value: int
#      - values: list
#      - name: str
#      - age: int
#      The constructor should call super and pass in the appropriate parameters
#      Delete these instructions and replace with your own description of that the function does.
class MyChildClass(MyParentClass):
    def __init__(childObj, value: int, values: list, name: str, age: int):
        super().__init__(value, values, name)
        childObj.age = age






# //14) TODO instantiate an object using MyChildClass with the following four parameters: (1, [5, 6, 7], "3", 10).
    # 15) TODO: do NOT duplicate the code in the parent class when writing the child class. For example, the parent
    # class constructor already creates the value, values, and name parameters. Do not write these in the child
    # class. Instead, the child constructor should call the parent constructor. Same for the 'get_value_using_index'
    # function, do not rewrite this in the child class.
childObj = MyChildClass(1, [5, 6, 7], "3", 10)
assert childObj.value == 1
assert childObj.values == [5, 6, 7]
assert childObj.name == "3"
assert childObj.age == 10
assert childObj.get_value_using_index(0) == 5
assert childObj.get_value_using_index(1) == 6
assert childObj.get_value_using_index(2) == 7
assert isinstance(childObj, MyParentClass) == True