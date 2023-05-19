import sys
register_num_list=[0,1,2,3,4,5,6]
def list_convert(s):
   k=[]
   ret=[]
   k.clear()
   ret.clear()
   k=s.split()
   for i in k:
       if i.strip()!="":
           ret.append(i.strip())
   return ret
def syntax_checker(command,i,flag_variable):
        # print(command)
        if (flag_variable and command[0]=="var"):
            print("Variable declared in the middle of the code at line",i+1)
            flag = True
        if (command[0]!="var"):
            flag_variable = True
        if (command[0].lower() in disc_isa):
            if (disc_isa[command[0].lower()]["type"]=="a"):
                if (len(command)!=4):
                    print("Syntax Error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or len(command[2])!=2 or command[1][0].lower()!='r' or command[2][0].lower()!='r' 
                    or not(command[1][1].isdigit()) or not(command[2][1].isdigit()) or not(str(len(command[3])) in '234')
                    or len(command[3])!=2 or command[3][0].lower()!='r' or not(command[3][1].isdigit())):
                    print("Register/Immediate Defined Incorrectly at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="b"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command)[1]!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
                elif (len(command[2])==2):
                    if (command[2][0]!='$' or not(command[2][1].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command)[2]==3):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])==4):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())
                        or not(command[2][3].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])!=2 and len(command[2])!=3 and len(command[2])!=4):
                    print("Wrong Immediate Value/Syntax at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="c"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit()) or
                    len(command[2])!=2 or command[2][0].lower()!='r' or not(command[2][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="d"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
                elif (command[2] not in variables):
                    print("Variable not declared at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="e"):
                if (len(command)!=2):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (command[1] not in labels):
                    print("Label not declared at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="f"):
                if (i==len(k)-1):
                    pass
                else:
                    print("Halt not at desired location")
                flag = True
                return
        elif (command[0].lower()=="mov"):
            if (len(command)!=3):
                print("Syntax error at line",i+1)
                flag = True
            elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                print("Register defined incorrectly at line",i+1)
                flag = True
            elif (len(command[2])==2):
                if (command[2][0]!='$' or not(command[2][1].isdigit())):
                    print("Wrong Immediate Value at line",i+1)
                    flag = True
            elif (len(command[2])==3):
                if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())):
                    print("Wrong Immediate Value at line",i+1)
                    flag = True
            elif (len(command[2])==4):
                if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())
                    or not(command[2][3].isdigit())):
                    print("Wrong Immediate Value at line",i+1)
                    flag = True
            elif (len(command[2])!=2 and len(command[2])!=3 and len(command[2])!=4):
                print("Wrong Immediate Value/Syntax at line",i+1)
                flag = True      
        else:
            print("Syntax Error at line",i+1) 
def error_checker():
    flag_haltt = False
    flag = False # It will be true when error occurs and the function will return 0
    flag_variable = False
    i=0
    while (i<len(k)):
        command = k[i].split()
        if (len(command)>4 and command[0][-1]!=':'):
            print("Syntax Error at line",i+1)
            flag = True
        if (len(command)==0):
            i+=1
            continue
        if (flag_variable and command[0]=="var"):
            print("Variable declared in the middle of the code at line",i+1)
            flag = True
        if (command[0]!="var"):
            flag_variable = True
        if (command[0].lower() in disc_isa):
            if (disc_isa[command[0].lower()]["type"]=="a"):
                if (len(command)!=4):
                    print("Syntax Error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or len(command[2])!=2 or command[1][0].lower()!='r' or command[2][0].lower()!='r' 
                    or not(command[1][1].isdigit()) or not(command[2][1].isdigit()) or not(str(len(command[3])) in '234')
                    or len(command[3])!=2 or command[3][0].lower()!='r' or not(command[3][1].isdigit())):
                    print("Register/Immediate Defined Incorrectly at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="b"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
                elif (len(command[2])==2):
                    if (command[2][0]!='$' or not(command[2][1].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command)[2]==3):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])==4):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())
                        or not(command[2][3].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])!=2 and len(command[2])!=3 and len(command[2])!=4):
                    print("Wrong Immediate Value/Syntax at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="c"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit()) or
                    len(command[2])!=2 or command[2][0].lower()!='r' or not(command[2][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="d"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
                elif (command[2] not in variables):
                    print("Variable not declared at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="e"):
                if (len(command)!=2):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (command[1] not in labels):
                    print("Label not declared at line",i+1)
                    flag = True
            elif (disc_isa[command[0].lower()]["type"]=="f"):
                if (i==len(k)-1):
                    flag_haltt = True
                    break
                else:
                    print("Halt not at desired location")
                    return
                flag = True
                break
        elif (command[0].lower()=="mov"):
                if (len(command)!=3):
                    print("Syntax error at line",i+1)
                    flag = True
                elif (len(command[1])!=2 or command[1][0].lower()!='r' or not(command[1][1].isdigit())):
                    print("Register defined incorrectly at line",i+1)
                    flag = True
                elif (len(command[2])==2):
                    if (command[2][0].lower()=='r' and command[2][1].isdigit()):
                        i+=1
                        continue
                    if (command[2][0]!='$' or not(command[2][1].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])==3):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                elif (len(command[2])==4):
                    if (command[2][0]!='$' or not(command[2][1].isdigit()) or not(command[2][2].isdigit())
                        or not(command[2][3].isdigit())):
                        print("Wrong Immediate Value at line",i+1)
                        flag = True
                
                elif (len(command[2])!=2 and len(command[2])!=3 and len(command[2])!=4):
                    if (command[2]=="FLAGS"):
                        i+=1
                        continue
                    print("Wrong Immediate Value/Syntax at line",i+1)
                    flag = True
                
        else:
            if (command[0].lower()=="var"):
                i+=1
                continue
            if (command==""):
                i+=1
                continue
