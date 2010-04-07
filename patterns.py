#!/usr/bin/env python

"""
Python implementation of some
common design patterns
"""

## Singleton pattern
class Singleton(type):
    """
    It extends the class type and overloads the __call__ function
    """
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None 

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
            return cls.instance

class MyClass(object):
    "Using the metaclass attribute assigning to it the call to Singleton"
    __metaclass__ = Singleton

## Another singleton using a function
class _Singleton(object):

    def __init__(self):
        # just for the sake of information
        self.instance = "Instance at %d" % self.__hash__()


_singleton = _Singleton()

def Singleton():
    return _singleton

## Borg pattern (by Martelli)
class Borg:
    """
    Instead of forcing all the classes to have the same identity
    we only force them to share the same state.
    This is much easier and brings to similar results
    """
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state    

## Iterator pattern
class MyIterator(object):
    def __init__(self, args):
        self.args = args

    def __iter__(self):
        # do some sort of checking if the object is actually iterable or not
        return iter(self.args)


## State pattern
class State(object):
    # this is somehow the initial state
    # if something in this class is called and not implemented return False
    pass

class NoCoins(State):
    def insert_coin(self):
        self.state = Machine.coins

class Coins(State):
    def get_gum(self):
        if Machine.gums > 1:
            Machine.gums -= 1
            self.state = Machine.no_coins
        else:
            self.state = Machine.sold_out

class SoldOut(object):
    def recharge(self):
        self.state = Machine.no_coins

class Machine(object):
    no_coins = NoCoins()
    coins = Coins()
    sold_out = SoldOut()
    state = no_coins
    # initial state of the things
    gums = 10


class GumBall(object):
    # a state diagram could also be seen like this, with
    # transictions and functions called in some occasions
    d = {"no_coins" : ["coins"],
         "coins" : ["no_coins"]}
        
    def __init__(self):
        init = "no_coins"

## Testing functions to see if they're actually working
def test_iterator():
    m = MyIterator(range(10))
    # we can assert that the object is actually iterable
    print list(iter(m))

def test():
    b1 = Borg()
    b2 = Borg()
    b1.x = 10
    b2.y = 100
    assert(b2.x == 10)
    assert(b1.y == 100)
    
if __name__ == '__main__':
    # test_iterator()
    print "should execute some tests"
    # test_borg()
    import nose
    nose.run()


