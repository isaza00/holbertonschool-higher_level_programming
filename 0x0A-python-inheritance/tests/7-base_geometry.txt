>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
>>> a = BaseGeometry()
>>> isinstance(a, BaseGeometry)
True

>>> a.integer_validator("width", 2)

>>> a.area()
Traceback (most recent call last):
Exception: area() is not implemented

>>> a.integer_validator("width", 0)
Traceback (most recent call last):
ValueError: width must be greater than 0

>>> a.integer_validator("width", -5)
Traceback (most recent call last):
ValueError: width must be greater than 0

>>> a.integer_validator()
Traceback (most recent call last):
TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'

>>> a.integer_validator("width")
Traceback (most recent call last):
TypeError: integer_validator() missing 1 required positional argument: 'value'

>>> a.integer_validator("width", "a")
Traceback (most recent call last):
TypeError: width must be an integer

>>> a.integer_validator("age", (7,))
Traceback (most recent call last):
TypeError: age must be an integer

>>> a.integer_validator("age", [3])
Traceback (most recent call last):
TypeError: age must be an integer

>>> a.integer_validator("age", False)
Traceback (most recent call last):
TypeError: age must be an integer

>>> a.integer_validator("age", {3,4})
Traceback (most recent call last):
TypeError: age must be an integer

>>> a.integer_validator("age", None)
Traceback (most recent call last):
TypeError: age must be an integer

>>> a.integer_validator("age", 5.54)
Traceback (most recent call last):
TypeError: age must be an integer
