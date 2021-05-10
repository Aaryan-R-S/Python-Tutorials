# TO GET DATE TIME USE --
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("Date: %d/%m/%Y  Time: %X %p  Time: %H[%I]:%M:%S  Day: %A[%a]  Month: %B[%b]"))   

# FREEZE TIME --
import time
k=0
while k<2 :
    time.sleep(1)      # Freeze Time
    print('Hi')
    k+=1

# import time

# a = time.time()

# for i in range(10):
#     print('Hi')
# print(f"Time : {time.time()-a}")


# b = time.time()

# k=0
# while k<10 :
#     print('Hi')
#     k+=1
# print(f"Time : {time.time()-b}")


# dT = time.asctime(time.localtime(time.time()))
# print(dT)





