fileFinal = open("file.txt",'r')

print("----------------Line---------------")
Tdata=fileFinal.readline()
print(Tdata)

print("-----------------Full--------------")
Fdata=fileFinal.read()
print(Fdata)
fileFinal.close()
print("----------------Write---------------")

fileFinal1 =open("file1.txt",'w')
fileFinal1.write("Maderchod bhadwa")
fileFinal1.close()

fileFinal2 =open("file1.txt",'a')
fileFinal2.write("\nMaderchod bhadwa hai tu")
fileFinal2.close()



