class A:
    def __init__(this, fname, lname):
        this.fname = fname
        this.lname = lname
        # this.email = f'{fname} {lname} : {email}'

    def info(this):
        return f"The Employee is {this.fname} {this.lname}"

# Property -- [is func but used as attribute] means set email attribute on basis of fname & laname
    @property
    def email(this):
        if this.fname == None or this.lname == None :
            return 'Email is not set. Please set it using setter!'
        return f'{this.fname}.{this.lname}@gmail.com'

# Decorators --
    @email.setter   # means set fname & lname on basis of email 
    def email(this, string):
        print('Setting Now...')
        names = string.split('@')[0]
        this.fname = names.split('.')[0]
        this.lname = names.split('.')[1]

    @email.deleter  # means del email attribute setting fname & lname as none
    def email(this):
        print('Deleting Now...')
        this.fname = None
        this.lname = None

x = A('Nik', 'Pik')
print(x.email)

x.fname = 'Joe'
print(x.email) 

x.email = 'this.that@gmail.com'
print(x.fname)
print(x.lname)
print(x.email)

del x.email
print(x.fname)
print(x.lname)
print(x.email)

# -- deleting anything ---

print(x)
print(A)

del x
del A

# print(x)
# print(A)