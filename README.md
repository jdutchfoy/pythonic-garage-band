# README.md

## LAB 4
Project: pythonic-garage-band
- Author: Dutch Foy

Links and Resources

- [README.md](/Users/dutchfoy/projects/401-Projects/pythonic-garage-band/README.md)

## Setup

- connect local repo to GitHub
.venv requirements
install package

## Initialize/run your application

python band.py
pytest-watch

## Tests
Here are the tests that need to be passed for this lab:

Band Tests

Make sure that a Band instance has a name attribute which is a string.
Check that a Band instance has a members attribute which is a list of instances that inherit from Musician base class.
Verify that a Band instance has a play_solos method that asks each member musician to play a solo, in the order they were added to band.
Ensure that a Band instance has appropriate str and repr methods.
Make sure that a Band has a class method to_list which returns a list of previously created Band instances.
Musician Subclass Tests

Verify that each kind of Musician instance has appropriate str and repr methods.
Check that each kind of Musician instance has a get_instrument method that returns a string.
Ensure that each kind of Musician instance has a play_solo method that returns a string.


- [Test code](/Users/dutchfoy/projects/401-Projects/pythonic-garage-band/tests/tests_band_test.py)


- [Test results]()![lab four test pass 2.png](..%2F..%2F..%2FDesktop%2Flab%20four%20test%20pass%202.png)


- [Code](/Users/dutchfoy/projects/401-Projects/pythonic-garage-band/band.py)


