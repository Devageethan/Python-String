def my():
    x=10
    print(x)

my()

def fun():
    c=12
    f=33
    def fun1():
        print(c)
        print(f)

    fun1()
fun()

a=45 #global fun
def h():
    print(a)
h()