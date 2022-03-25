def swapFileData():
    file1=input("Enter Your First File Name")
    file2=input("Enter Your Second File Name")
    with open(file1,"r") as A1:
      data_A1=A1.read()

    with open(file2,'r') as B1:
      data_B1 =B1.read()

    with open(file1,"w") as A1 :
      A1.write(data_B1)

    with open(file2,"w") as B1 :
      B1.write(data_A1)    

swapFileData()