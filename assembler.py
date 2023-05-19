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
            if (command[0][-1]==":"):
                if (len(command)==1):
                    i+=1
                    continue
                else:
                    syntax_checker(command[1:],i,flag_variable)
                    if (i==len(k)-1 and len(command[1:])==1 and command[1:][0]=="hlt"):
                        flag_haltt = True
                        break
                    i+=1
                    continue
            else :
                print("Syntax Error at line",i+1)
                flag = True
                i+=1
                continue
            # print("Syntax Error at line",i+1)     
        i+=1
    if (flag_haltt==False):
        print("Halt not declared")
        return 0
    if (flag):
        return 0
    return 1
disc_isa = {"add" : {"opcode" : "00000", "type" : "a"},
            "sub" : {"opcode" : "00001", "type" : "a"},
            "mov1" : {"opcode" : "00010", "type" : "b"},
            "mov2" : {"opcode" : "00011", "type" : "c"},
            "ld" : {"opcode" : "00100", "type" : "d"},
            "st" : {"opcode" : "00101", "type" : "d"},
            "mul" : {"opcode" : "00110", "type" : "a"},
            "div" : {"opcode" : "00111", "type" : "c"},
            "rs" : {"opcode" : "01000", "type" : "b"},
            "ls" : {"opcode" : "01001", "type" : "b"},
            "xor" : {"opcode" : "01010", "type" : "a"},
            "or" : {"opcode" : "01011", "type" : "a"},
            "and" : {"opcode" : "01100", "type" : "a"},
            "not" : {"opcode" : "01101", "type" : "c"},
            "cmp" : {"opcode" : "01110", "type" : "c"},
            "jmp" : {"opcode" : "01111", "type" : "e"},
            "jlt" : {"opcode" : "11100", "type" : "e"},
            "jgt" : {"opcode" : "11101", "type" : "e"},
            "je" : {"opcode" : "11111", "type" : "e"},
            "hlt" : {"opcode" : "11010", "type" : "f"}}
disc_reg = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
reg_values={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":"0000000000000000"}
opcode=[]
def DecimalToBinary(num) : #This will return string of the binary conversion
    if num<1 :
        return ""
    ans = DecimalToBinary(num//2)
    return ans+str(num%2)
opcode_list = []
unused={"a":2,"b":1,"c":5,"d":1,"e":4,"f":11}
length_opcode=[4,3,2,1]
k=sys.stdin.readlines()
#k==[line.strip() for line in sys.stdin.readlines()]
# print(len(k))
c=0
variables={}
labels={}
for i in range (len(k)):
    if k[i]!="":
        p=list_convert(k[i])
        if p[0] != "var":
            c=c+1
for i in range (len(k)):
    if k[i]!="":
        p=list_convert(k[i])
        if p[0]=="var":
                if len(p)==2:
                    if p[0] not in variables:
                        binary=DecimalToBinary(c)
                        binary=(7-len(binary))*"0"+binary
                        variables[p[1]]=binary
                        c=c+1
c_lab=0
for i in range(len(k)):
    if k[i]!="":
        p=list_convert(k[i])
        if p[0]!="var":
            if p[0][-1]==":":
                if len(p)==1:
                    if p[0] not in labels:
                        binary=DecimalToBinary(c_lab+1)
                        binary=(7-len(binary))*"0"+binary
                        labels [p[0]]=binary
                else:
                    if p[0] not in labels:
                        binary=DecimalToBinary(c_lab)
                        binary=(7-len(binary))*"0"+binary
                        labels[p[0][0:-1]]=binary
            c_lab+=1
count=0
if (not(error_checker())):
    pass
else:
    #print("Code executed successfully")
    for i in range(len(k)):
        if k[i]!=" ":
            z=list_convert(k[i])
            op=''
            bin=''
            if z[0][0:-1] in labels and len(z)==1:
                continue
                '''print(z[0][0:-1])
                op=op+labels[z[0][0:-1]]
                count=count+1
                opcode_list.append(op)'''
            elif z[0][0:-1] in labels and len(z)!=1:
                z.pop(0)
                if len(z) in length_opcode and z[0]!="var":
                    if z[-1]=="FLAGS":
                        if z[0]=="mov":
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+"00011"
                                op=op+5*"0"
                                op=op+disc_reg[z[1]]
                                op=op+"111"
                            
                    if z[-1][0]=="$":
                        if z[0]=="mov":
                            op=op+"00010"
                            op=op+'0'
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                if int(z[2][1:])>=0 and int(z[2][1:])<128:
                                    bin=DecimalToBinary(int(z[2][1:]))
                                    bin=(7-len(bin))*"0"+bin
                                    op=op+bin
                                else:
                                    op='Immediate value exceeded 127'
                            else:
                                op='Register not present'
                        else:
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+'0'
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                bin=DecimalToBinary(int(z[2][1:]))
                                bin=(7-len(bin))*"0"+bin
                                op=op+bin
                            else:
                                op='Register not present'
                    if [z[0][-1]]==":" and len(z)==1:
                        continue
                    #elif disc_isa[z[0][-1]]==":" and len(z)!=1:
                    if z[0]!="mov":
                        if disc_isa[z[0]]["type"]=="d":
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+"0"
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                if z[2] in labels:
                                    op=op+labels[z[2]]
                                elif z[2] in variables:
                                    op=op+str(variables[z[2]])
                            else:
                                op='Register not present'
                    if z[0]!="mov":
                        if disc_isa[z[0]]["type"]=="e":
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+"0000"
                            op=op+labels[z[1]]
                    if z[0]=="hlt" or z[-1]=="hlt":
                        op=str(11010)+unused["f"]*"0"
                    if z[0]=="mov" and z[-1][0]!="$" and z[-1]!="FLAGS":
                            op=op+"00011"
                            op=op+"00000"
                            for m in range(1,len(z)):
                                if int(z[1][-1])>=6 and int(z[1][-1])<=0:
                                    op='Register not present'
                                    break
                                else:
                                    op=op+disc_reg[z[m]]
                    elif z[0]!="hlt" and z[0]!="mov" and z[-1] not in variables:
                            op=op+str(disc_isa[z[0]]["opcode"])
                            op=op+unused[disc_isa[z[0]]["type"]]*"0"
                            for m in range(1,len(z)):
                                if int(z[1][-1])>=6 and int(z[1][-1])<=0:
                                    op='Register not present'
                                    break
                                else:
                                    op=op+disc_reg[z[m]]
                    count=count+1
                    print(op)
                
                '''for i in range(1,len(z)):

                    if z[i] in disc_isa:
                        op=op+disc_isa[z[i]]["opcode"]
                        op=op+unused[disc_isa[z[i]]["type"]]*"0"
                    elif z[i] in disc_reg:
                        op=op+disc_reg[z[i]]
                    


                count=count+1
                print(op)
                opcode_list.append(op)'''

            else:
                if len(z) in length_opcode and z[0]!="var":
                    if z[-1]=="FLAGS":
                        if z[0]=="mov":
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+"00011"
                                op=op+5*"0"
                                op=op+disc_reg[z[1]]
                                op=op+"111"
                            
                    if z[-1][0]=="$":
                        if z[0]=="mov":
                            op=op+"00010"
                            op=op+'0'
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                if int(z[2][1:])>=0 and int(z[2][1:])<128:
                                    bin=DecimalToBinary(int(z[2][1:]))
                                    bin=(7-len(bin))*"0"+bin
                                    op=op+bin
                                else:
                                    op='immediate value exceeds 127'
                            else:
                                op='Register not present'
                        else:
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+'0'
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                bin=DecimalToBinary(int(z[2][1:]))
                                bin=(7-len(bin))*"0"+bin
                                op=op+bin
                            else:
                                op='Register not present'
                    if [z[0][-1]]==":" and len(z)==1:
                        continue
                    if z[0]=="hlt" or z[-1]=="hlt":
                        op=str(11010)+unused["f"]*"0"
                    if z[0]!="mov":
                        if disc_isa[z[0]]["type"]=="d":
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+"0"
                            if int(z[1][-1])<=6 and int(z[1][-1])>=0:
                                op=op+disc_reg[z[1]]
                                if z[2] in labels:
                                    op=op+labels[z[2]]
                                elif z[2] in variables:
                                    op=op+str(variables[z[2]])
                            else:
                                op='Register not present'
                    if z[0]!="mov":
                        if disc_isa[z[0]]["type"]=="e":
                            op=op+disc_isa[z[0]]["opcode"]
                            op=op+"0000"
                            op=op+labels[z[1]]
                    if z[0]=="mov" and z[-1][0]!="$" and z[-1]!="FLAGS":
                            op=op+"00011"
                            op=op+"00000"
                            for m in range(1,len(z)):
                                if int(z[1][-1])>=6 and int(z[1][-1])<=0:
                                    op=''
                                    break
                                else:
                                    op=op+disc_reg[z[m]]
                    elif z[0]!="hlt" and z[0]!="mov" and z[-1] not in variables and z[-1] not in labels:
                            op=op+str(disc_isa[z[0]]["opcode"])
                            op=op+unused[disc_isa[z[0]]["type"]]*"0"
                            for m in range(1,len(z)):
                                if int(z[1][-1])>=6 and int(z[1][-1])<=0:
                                    op='Register not present'
                                    break
                                else:
                                    op=op+disc_reg[z[m]]
                    count=count+1
                    print(op)
