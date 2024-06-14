# raise allows you to throw an exception at any time.
# assert enables you to verify if a certain condition is met and throw an exception
# if it isn't.
# In the try clause, all statements are executed until an exception is encountered.
# except is used to catch and handle the exception(s) that are encountered in the
# try clause.
# ⚫else lets you code sections that should run only when no exceptions are
# encountered in the try clause.
# finally enables you to execute sections of code that should always run, with or
# without any previously encountered exceptions.


# Exception->
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

def zerodivision():
    x=4/0
#Exception Handling
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')


try:
    with open('file.log') as file:
        read_data= file.read()
except FileNotFoundError as fnf_error:
    print (fnf_error)

try:
    zerodivision()                          #first this is read and since this gives an error its exception is raised
    # and next error isnt informed
    with open('file.log') as file:
        read_data= file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except ZeroDivisionError as error:
    print(error)

#ELSE CLAUSE->used if there is no exception
try:
    zerodivision()
except ZeroDivisionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data= file.read()
    except FileNotFoundError as fnf_error:
        print (fnf_error)

#finally -> used even if there was an exception or  not
try:
    zerodivision()
except ZeroDivisionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data =file.read()
    except FileNotFoundError as fnf_error:
        print (fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')