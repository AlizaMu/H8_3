s = 'Hacktiv8-PTP Python for Data SCience'
a = [100, 300, 300]

def foo(arg):
    print(f'arg = {arg}')


class Foo:
    pass

if (__name__=='__main__'):
    print('Executing as standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)