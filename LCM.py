div_number_list=[2, 3, 5, 7]
lcm_number_list=[]
def lcm(input):
    flag = False
    for i in range(0, len(input)):
        for j in range(0, len(div_number_list)):
            if input[i]%div_number_list[j]==0:
                flag=True
        if flag==False and input[i]!=1:
            if input[i] not in lcm_number_list:
                lcm_number_list.append(input[i])
            input[i] = 1
        flag=False
    for i in range(0,len(div_number_list)):
        for j in range(0,len(input)):
            if input[j]!=1 and input[j]%div_number_list[i]==0:
                flag=True
                input[j]=input[j]//div_number_list[i]
        if flag==True:
            lcm_number_list.append(div_number_list[i])
            flag=False
    return input


def check_lcm():
    input_list=[]
    print("\t\t\t-->  Enter only non_zero numbers !  <--")
    ask=int(input("Total number for LCM:\n\t\t"))
    while ask!=0:
        number=int(input("Enter number:\t"))
        if number!=0:
            input_list.append(number)
            ask-=1
        else:
            print("\t-->  Enter only non_zero number !  <--")
    print("List of input LCM numbers:\t",input_list)
    flag1 = False
    while flag1!=True:
        flag1=True
        for i in input_list:
            if i!=1:
                flag1=False
                input_list=lcm(input_list)
    print("Diviser numbers:\t",lcm_number_list)
    LCM=1
    for i in lcm_number_list:
        LCM*=i
    print("LCM is:",LCM)

check_lcm()
