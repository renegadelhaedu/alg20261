djows = ['jose','pedro','marcos','eric']
contra = []

#for i in range(len(djows)):
#    contra.insert(0,djows[i])
#    print(contra)

for i in range(len(djows)-1, -1, -1):
    contra.append(djows[i])
print(contra)