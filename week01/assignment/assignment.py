'''
Time Guesstimate to complete:
Proficient with all the "Know how to" statements:                       1 hour
Familiar with the "Know how to" statements, but need to review a few:   1 - 4 hours
Need to review most the "Know how to" statements:                       4 - 8 hours
Need to review/relearn all the "Know how to" statements:                8+ hours

All ASSERTS must pass. Everything in this assignment should have been learned
previously. If there are holes in your knowledge, then this is the time to 
fill them (meaning learn the concepts). Take the time to learn by reading
the provided links. There are no group "prove" assignments in this class.

Make sure to write comments above your functions, explaining in your own
words what the functions does. Your comments are your "digital signature",
showing that you both wrote the code and understand how it works.

Grading:
Not passing an assert or answering #10 and #12: 0 points (code must pass all asserts--this is only true of this first assignment)
'''

from unittest import TestCase
from cse251functions import *

#Created a function that requires the three parameters: initial_value, value, & operation
def perform_math(initial_value, value, operation):
    #Created a series of if & elif to check all possible operations to determ what type of math should be used.
    if operation == "+":
        #Return the sum of determed operation & its sums
        return initial_value + value
    elif operation == "-":
        return initial_value - value
    elif operation == "*":
        return initial_value * value
    elif operation == "/":
        return initial_value / value
    elif operation == "//":
        return initial_value // value
    elif operation == "**":
        return initial_value ** value
    
#Created a function that requires the two parameters: word_to_find & words.
def find_word_index(word_to_find, word_dict):
    #Returns the value in the list at the index provided by word_to_find
    return word_dict.index(word_to_find)
        
#Created a function that requires the two parameters: key & ord_dict.
def get_value_from_dict_using_key(key, ord_dict):
    #Returns the value in the dictionary using the key provided by the varible called key
    return ord_dict[key]

#Created a function that requires the two parameters: key & url_dict.
def get_list_of_urls_from_dict(key, url_dict):
    #Returns the list in the dictionary using the key provided by the varible called key
    return url_dict[key]

#Created a function that requires the two parameters: urls & name.
def find_url(urls, name):
    #used a for loop to iterate through the list urls. Stored each part of the list in i one at a time while iterating.
    for i in urls:
        #Used if condition to check if item in name is also in the current url
        if i.find(name) == name:
            #returned url if it contend name
            return i
        else:
            #return empty string if no url had name
            return ""

#Created a function that requires the two parameters: filename & str_to_find.
def find_str_in_file(filename, str_to_find):
    #opened file given to the function & stored it in a varible
    file = open(filename)
    #stored first line of the stored file
    line = file.readline()
    #Used condition while to loop through every line in the file one line at a time
    while line:
        #determed weather or not current line in file is "str_to_find"
        if line.strip() == str_to_find:
            #closed file
            file.close()
            #return true if "str_to_find" is found
            return True
        else:
            #put next line into varible
            line = file.readline()
    #extra closed file in case no "str_to_find" Could have used with, but short on time
    file.close()
    return False

#Created a class.
class MyParentClass():
    #Created a constructor function that requires the four parameters.
    def __init__(obj, value: int, values: list, name: str):
        #set all varibles in the object varible to needed values given to constructor
        obj.value = value
        obj.values = values
        obj.name = name
    #Created a function that requires the two parameters: obj & key.
    def get_value_using_index(obj, key):
        #Returns the value in the list at the index provided by key
        return obj.values[key]

#Created a class that inherits the MyParentClass class.
class MyChildClass(MyParentClass):
    #Created a constructor function that requires the five parameters.
    def __init__(childObj, value: int, values: list, name: str, age: int):
        #used super to used constructor to set all varibles in the object varible to needed values given to constructor
        super().__init__(value, values, name)
        #set final varible in the object varible to needed value
        childObj.age = age

#      10) TODO: Provide a quick explanation of what pass-by-reference means. Also, what does mutable mean?
        #Pass means to provide an argument to a function. By reference means that the argument you're passing to the function is a reference to a variable that already exists in memory rather than an independent copy of that variable. (Found on google, but I currently think it is right)
        #mutable means has the ability to change
#Created a function that requires the two parameters: lists_are_passed_by_reference_and_mutable & str_to_add
def pass_by_reference_mutable_example(lists_are_passed_by_reference_and_mutable, str_to_add):
    #returned list with varible appended to the end
    return lists_are_passed_by_reference_and_mutable.append(str_to_add)

#      12) TODO: What does immutable mean?
        #immutable means does not have the ability to change
#Created a function that requires the two parameters: strings_are_pass_by_reference_and_immutable & str_to_add
def pass_by_reference_immutable_example(strings_are_pass_by_reference_and_immutable, str_to_add):
    #makes string varible that equal both strings added together
    string = strings_are_pass_by_reference_and_immutable + str_to_add
    #returns string varible
    return string

def main():
    ''' Know how to:
        - Call a function
        - Pass in parameters to a function in the correct order
        - Use correct parameter data types
        - Return a value from a function
        - Return correct data type from a function
        - Return from all call paths in a a function
        - Write an IF statement
        - Reading: https://www.geeksforgeeks.org/python-functions/
    '''
    assert perform_math(10, 1, "+") == 11
    assert perform_math(1, 10, "+") == 11
    assert perform_math(10, 1, "-") == 9
    assert perform_math(1, 10, "-") == -9
    assert perform_math(10, 2, "*") == 20
    assert perform_math(2, 10, "*") == 20
    assert perform_math(10, 2, "/") == 5
    assert perform_math(2, 10, "/") == 0.2
    assert perform_math(10, 3, "//") == 3
    assert perform_math(3, 10, "//") == 0
    assert perform_math(10, 3, "**") == 1000
    assert perform_math(3, 10, "**") == 59049

    ''' Know how to:
        - Use a list
        - Use the index function on a list
        - Reading: https://www.geeksforgeeks.org/python-lists/
    '''
    assert find_word_index("a", ["a", "b", "c", "h"]) == 0
    assert find_word_index("b", ["a", "b", "c", "h"]) == 1
    assert find_word_index("c", ["a", "b", "c", "h"]) == 2
    assert find_word_index("h", ["a", "b", "c", "h"]) == 3

    ''' Know how to:
        - Use a dictionary
        - Use a key to get the value in a dictionary
        - Understand that a dictionary value can be list
        - Know how to get the list using a key
        - Know how to write a FOR loop
        - Know how to use "in" keyword
        - Reading: https://www.geeksforgeeks.org/python-dictionary/
    '''
    word_dict = {"k1": 1, "k2": 2, "k3": 3, "k4": 10}
    assert get_value_from_dict_using_key("k1", word_dict) == 1
    assert get_value_from_dict_using_key("k2", word_dict) == 2
    assert get_value_from_dict_using_key("k3", word_dict) == 3
    assert get_value_from_dict_using_key("k4", word_dict) == 10
    movie_dict = {"people": ["http://127.0.0.1:8790/1", "http://127.0.0.1:8790/2", "http://127.0.0.1:8790/3"], "films":
                  ["http://127.0.0.1:8790/film1", "http://127.0.0.1:8790/film2", "http://127.0.0.1:8790/film3"]}
    urls = get_list_of_urls_from_dict("films", movie_dict)
    url = find_url(urls, "film3")
    assert url != None

    '''
        - Know how to make a Python Class
        - Know how to write a constructor
        - Know how to make attributes in a constructor
        - Understand how to use "self" in Python
        - Know how to instantiate an object of a class (shown below)
        - Know how to obtain the value using the object's attribute (shown below)
        - Know what a method is and how to write one
        - Know how to return a value from a method
        - Know to obtain a value at a specific index in a list
        - Know how to extend a class
        - Understand that an extended/child class inherits everything from parent class
        - Readings: https://www.geeksforgeeks.org/python-classes-and-objects/, https://www.geeksforgeeks.org/extend-class-method-in-python/, https://realpython.com/python-super/
    '''
    # 13) TODO instantiate an object using MyParentClass with the following three parameters: (1, [5, 6, 7], "3")
    obj = MyParentClass(1, [5, 6, 7], "3")
    assert obj.value == 1
    assert obj.values == [5, 6, 7]
    assert obj.name == "3"
    assert obj.get_value_using_index(0) == 5
    assert obj.get_value_using_index(1) == 6
    assert obj.get_value_using_index(2) == 7

    # 14) TODO instantiate an object using MyChildClass with the following four parameters: (1, [5, 6, 7], "3", 10).
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

    '''
        - Know how to open a file
        - Know how to read lines from a file
        - Understand how to compare strings
        - Readings: https://www.geeksforgeeks.org/open-a-file-in-python/, https://www.geeksforgeeks.org/with-statement-in-python/
    '''
    assert find_str_in_file("data.txt", "g") == True
    assert find_str_in_file("data.txt", "1") == False

    '''
        - Know the difference between pass-by-reference and pass-by-value.
        - Reading: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference (read the first answer)
        - Technically python is pass-by-object-reference, if you are intested in the difference, read https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/
    '''
    l = ["abc", "def", "ghi"]
    pass_by_reference_mutable_example(l, "jkl")
    assert len(l) == 4
    assert l[3] == "jkl"
    s = "strings are immutable"
    new_string = pass_by_reference_immutable_example(
        s, " so adding to it creates a new object in memory")
    assert id(s) != id(new_string)
    assert len(new_string) != len(s)

    print("All tests passed!")


if __name__ == '__main__':
    main()
    create_signature_file("CSE251W25")
 