import sys
def str_to_list(s,index,newvar):
    l=list(s)
    l[index] = newvar
    temp=""
    for j in l:
        temp+=j
        
    return temp
register_num_list=[0,1,2,3,4,5,6]
def binaryToDecimal(binary):
    decimal=0
    pow=0
    for i in range(-1,-1*len(binary)-1,-1):
        decimal=decimal+int(binary[i])*(2**pow)
        pow=pow+1
    return(decimal)
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
def DecimalToBinary(num) : #This will return string of the binary conversion
    if num<1 :
        return ""
    ans = DecimalToBinary(num//2)
    return ans+str(num%2)
disc_reg = {"R0" : "000","R1" : "001", "R2" : "010" , "R3" : "011" , "R4" : "100" , "R5" : "101" , "R6" :"110", "FLAGS" : "111"}
reg_values={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":"0000000000000000"}
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
            "hlt" : {"opcode" : "11010", "type" : "f"},
            "addf" : {"opcode" : "10000", "type" : "a"},
            "subf" : {"opcode" : "00001", "type" : "a"},
            "movf" : {"opcode" : "10010", "type" : "b"}}
#f=open("test01.txt","r")
#opcode_list=f.read().splitlines()
opcode_list=sys.stdin.readlines()
opcode_list==[line.strip() for line in sys.stdin.readlines()]
pc={}
opcode=[]
counter=0
while counter<len(opcode_list):
    temp_bin=DecimalToBinary(counter)
    temp_bin=(7-len(temp_bin))*"0"+temp_bin
    pc[opcode_list[counter-1]]=temp_bin
    counter+=1
counter=0
halted=False
def reg_checker(str):
    for i in disc_reg:
        if disc_reg[i]==str:
            return i
'''def label_checker(str):
    for i in labels:
        if labels[i]==str:
            return i'''
g=opcode_list[counter]
new_var=[]
while halted!=True:
    #if reg_values["FLAGS"]!="0000000000000000":
        #reg_values["FLAGS"]="0000000000000000"
    inst=''
    for i in disc_isa:
        if disc_isa[i]["opcode"]==g[0:5]:
            inst=i
    if disc_isa[inst]["type"]=="a":
        x1=reg_checker(g[7:10])
        x2=reg_checker(g[10:13])
        x3=reg_checker(g[13:16])
        if inst=="add":
            u=reg_values[x2]+reg_values[x3]
            if u>2**16:
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -4, "1")
                reg_values[x1]=0
                counter+=1
            else:
                reg_values[x1]=u
                counter+=1
        if inst=="sub":
            u=reg_values[x2]-reg_values[x3]
            if u<0:
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -4, "1")
                reg_values[x1]=0
                counter+=1
            else:
                reg_values[x1]=u
                counter+=1
        if inst=="mul":
            u=reg_values[x2]*reg_values[x3]
            if u>2**16:
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -4, "1")
                reg_values[x1]=0
                counter+=1
            else:
                reg_values[x1]=u
                counter+=1
        #if reg_values["FLAGS"]!="0000000000000000":
            #reg_values["FLAGS"]="0000000000000000"
    if disc_isa[inst]["type"]=="b":
        x1=reg_checker(g[6:9])
        if inst=="mov1":
            reg_values[x1]=binaryToDecimal(g[9:16])
            counter+=1
        if reg_values["FLAGS"]!="0000000000000000":
            reg_values["FLAGS"]="0000000000000000"
    if disc_isa[inst]["type"]=="c":
        if inst=="mov2":
            x1=reg_checker(g[10:13])
            x2=reg_checker(g[13:16])
            if x2=="FLAGS":
                reg_values[x1]=binaryToDecimal(reg_values["FLAGS"])
            else:
                reg_values[x1]==reg_values[x2]
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
            counter+=1
        if inst=='div':
            x1=reg_checker(g[10:13])
            x2=reg_checker(g[13:16])
            if reg_values[x2]==0:
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -4, "1")
                reg_values["R0"]=0
                reg_values["R1"]=0
                counter+=1
            else:
                if reg_values["FLAGS"]!="0000000000000000":
                    reg_values["FLAGS"]="0000000000000000"
                reg_values[x1]=reg_values[x1]/reg_values[x2]
                counter+=1
        if inst=="not":
            x1=reg_checker(g[10:13])
            x2=reg_checker(g[13:16])
            bin=DecimalToBinary(x2)
            bin=(16-len(bin))*"0"+bin
            for i in range(len(bin)):
                if bin[i]=="1":
                    bin=str_to_list(bin, i, "0")
                elif bin[i]=="0":
                    bin=str_to_list(bin, i, "1")
            reg_values[x1]=binaryToDecimal(bin)
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
            counter+=1
        if inst=="cmp":
            x1=reg_checker(g[10:13])
            x2=reg_checker(g[13:16])
            if reg_values[x1]<reg_values[x2]:
                #reg_values["FLAGS"][-3]="1"
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -3, "1")
                counter+=1
            if reg_values[x1]>reg_values[x2]:
                #reg_values["FLAGS"][-2]="1"
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -2, "1")
                counter+=1
            if reg_values[x1]==reg_values[x2]:
                #reg_values["FLAGS"][-1]="1"
                reg_values["FLAGS"]=str_to_list(reg_values["FLAGS"], -1, "1")
                counter+=1
    if disc_isa[inst]["type"]=="d":
        x1=reg_checker(g[6:9])
        if inst=="ld":
            temp=binaryToDecimal(g[9:16])
            reg_values[x1]=temp
            counter+=1
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
        if inst=="st":
            temp=DecimalToBinary(reg_values[x1])
            temp=(7-len(temp))*"0"+temp
            '''for i in labels:
                if labels[i]==g[9:16]:
                    labels[i]=temp
            for i in variables:
                if variables[i]==g[9:16]:
                    variables[i]=temp'''
            new_var.append(temp)
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
            counter+=1
    if disc_isa[inst]["type"]=="e":
        #x1=label_checker(g[9:16])
        if inst=="jmp":
            for i in range(len(opcode_list)):
                '''if opcode_list[i]==label_code[x1]:
                    counter=i'''
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
            counter+=1
        if inst=="jlt":
            if reg_values["FLAGS"][-3]=="1":
                for i in range(len(opcode_list)):
                    '''if opcode_list[i]==label_code[x1]:
                        counter=i'''
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
            else:
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
        if inst=="jgt":
            if reg_values["FLAGS"][-2]=="1":
                for i in range(len(opcode_list)):
                    '''if opcode_list[i]==label_code[x1]:
                        counter=i'''
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
            else:
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
        if inst=="je":
            if reg_values["FLAGS"][-1]=="1":
                for i in range(len(opcode_list)):
                    '''if opcode_list[i]==label_code[x1]:
                        counter=i'''
            if reg_values["FLAGS"]!="0000000000000000":
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
            else:
                reg_values["FLAGS"]="0000000000000000"
                counter+=1
    if disc_isa[inst]["type"]=="f":
        counterbin=(DecimalToBinary(counter))
        counterbin=(7-len(counterbin))*"0"+counterbin
        print(counterbin,end=" ")
        for i in range(7):
            temp=DecimalToBinary(reg_values["R"+str(i)])
            temp=(16-len(temp))*"0"+temp
            print(temp,end="        ")
        print(reg_values["FLAGS"])
        halted=True
        break
    counterbin=(DecimalToBinary(counter-1))
    counterbin=(7-len(counterbin))*"0"+counterbin
    print(counterbin,end="        ")
    for i in range(7):
        temp=DecimalToBinary(reg_values["R"+str(i)])
        temp=(16-len(temp))*"0"+temp
        print(temp,end=" ")
    print(reg_values["FLAGS"])
    opcode.append(g)
    g=opcode_list[counter]
for i in range(len(opcode_list)):
    print(opcode_list[i])
for i in new_var:
    temp=i
    temp=(16-len(i))*"0"+temp
    print(temp)
for i in range(128-len(opcode_list)):
    print("0000000000000000")

            
            
            
            
        
        
            
    
    
    
    
   
