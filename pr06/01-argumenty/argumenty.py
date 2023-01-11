"""
@author: SaltyCrane
@source: http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
"""

def test_var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)

def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key, value in kwargs.items():
        print("another keyword arg: %s: %s" % (key, value))

def test_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

if __name__ == '__main__':
    fields = {"arg3": 3, "arg2": "two", "arg1": 44}
    args = (1000, 2000, 30)
    #test_var_kwargs(fields, ab=30, cd=40, ef='pokus')
    test_var_kwargs(args, **fields)
    #test_var_args_call(*args)
    #test_var_args("ukazka", args, 10, 20, 30, 40, 599)
    #test_var_args("ukazka", *args)
    