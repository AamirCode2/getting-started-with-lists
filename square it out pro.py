num1 = int(input("What is the beginning range of your number list: "))
num2 = int(input("What is the ending range of your number list: "))

user_list = []
even_list = []
odd_list = []

for i in range(num1,num2+1):
    user_list.append(i*i)

for item in user_list:
   if item%2==0:
       even_list.append(item)
   else:
        odd_list.append(item)

print("Even exponentiated numbers: \n", even_list)
print("Odd exponentiated numbers: \n", odd_list)