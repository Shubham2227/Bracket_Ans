#shubham kuamr maurya
#shubh27296@gmail.com
#9936717419


input_user = input()
n = -1
while(len(input_user) != n):
    n = len(input_user)
    input_user = input_user.replace('()',"")
    input_user = input_user.replace('[]',"")
    input_user = input_user.replace('{}',"")
if (len(input_user) == 0):
    print("YES")
else:
    print("NO")

