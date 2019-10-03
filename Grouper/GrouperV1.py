########################
### Grouping Program ###
########################

### Imports ###
from collections import Counter
import random

### Variable Declaration ###

student=[]
students=[]
students2=[]
pairs=[]
pairs2=[]
groups=[]
groups_info=[]
inputs=""
count=1
number_groups=input("How many groups can there be? ")
students=[["a","c","k","g","0"],["b","n","j","k","0"],["c","l","i","m","0"],["d","e","f","k","0"],
["e","f","d","k","0"],["f","d","e","k","0"],["g","b","l","m","0"],["h","k","o","l","0"],["i","a","c","n","0"],
["j","m","n","k","0"],["k","l","a","n","0"],["l","k","a","m","0"],["m","o","n","b","0"],["n","m","o","j","0"]]
total_students=len(students)
print("Variable Declaration: Yes")

### Functions ###

def want1():
    for s1 in range(total_students):
        for s2 in range(s1+1,total_students):
            pairs.append([0, students[s1][0], students[s2][0]])
            if(students[s1][0] in students[s2][1]):
                pairs[-1][0]+=5
            elif(students[s1][0] in students[s2][2]):
                pairs[-1][0]+=3
            elif(students[s1][0] in students[s2][3]):
                pairs[-1][0]+=1
            elif(students[s1][0] in students[s2][4]):
                pairs[-1][0]-=4
            if(students[s2][0] in students[s1][1]):
                pairs[-1][0]+=5
            elif(students[s2][0] in students[s1][2]):
                pairs[-1][0]+=3
            elif(students[s2][0] in students[s1][3]):
                pairs[-1][0]+=1
            elif(students[s2][0] in students[s1][4]):
                pairs[-1][0]-=4

def want2():
    for g in range(len(groups)):
        for s in range(total_students):
            pairs.append([0, groups[g], students[s][0]])
            for g2 in range(len(groups_info[g])):
                if(students[s][0] == groups_info[g][g2][1]):
                    pairs[-1][0]+=2.5
            for g2 in range(len(groups_info[g])):
                if(students[s][0] == groups_info[g][g2][2]):
                    pairs[-1][0]+=1.5
            for g2 in range(len(groups_info[g])):
                if(students[s][0] == groups_info[g][g2][3]):
                    pairs[-1][0]+=0.5
            for g2 in range(len(groups_info[g])):
                if(students[s][0] == groups_info[g][g2][4]):
                    pairs[-1][0]+=-2
            if(groups[g][1] in students[s][1] or groups[g][2] in students[s][1]):
                pairs[-1][0]+=5
            elif(groups[g][1] in students[s][2] or groups[g][2] in students[s][2]):
                pairs[-1][0]+=3
            elif(groups[g][1] in students[s][3] or groups[g][2] in students[s][3]):
                pairs[-1][0]+=1
            elif(groups[g][1] in students[s][4] or groups[g][2] in students[s][4]):
                pairs[-1][0]-=4
                
def placer1():
    g=0
    p=0
    while(len(groups)<number_groups):
        if(pairsg[g]+len(groups)<=number_groups):
            for i in range(pairsg[g]):
                groups.append(pairs2[p+i])
        else:
            for i in range(number_groups-len(groups)):
                groups.append(pairs2[p+random.randrange(0,pairsg[g])]) ### WHY YOU GOTTA DO THIS TO ME ###
        p+=pairsg[g]
        g+=1
    for g in range(len(groups)):
        groups_info.append([])
        for g2 in groups[g]:
            num=0
            while num<len(students):
                if(g2==students[num][0]):
                    groups_info[g].append(students[num])
                    num=len(students)
                num+=1
    
def placer2():
    if len(groups) <= len(pairs2):
        g=0
        p=0
        while(p<len(groups)):
            if(pairsg[g]+p<=number_groups):
                for i in range(pairsg[g]):
                    group=groups.index(pairs2[p+i][1])
                    groups[group].append(pairs2[p+i][2])
                    groups[group][0]+=pairs2[p+i][0]
            else:
                for i in range(number_groups-len(groups)):
                    randompair = random.randrange(0,pairsg[g]) + p
                    group=groups.index(pairs2[randompair][1])
                    groups[group].append(pairs2[randompair][2])
                    groups[group][0]+=pairs2[randompair][0]
            p+=pairsg[g]
            g+=1
    else:
        for s in range(len(pairs2)):
            group=groups.index(pairs2[s][1])
            groups[group].append(pairs2[s][2])
            groups[group][0]+=pairs2[s][0]
    for g in range(len(groups)):
        num=0
        while num<len(students):
            if(groups[g][-1]==students[num][0]):
                groups_info[g].append(students[num])
                num=len(students)
            num+=1

print("Functions: Yes")

### Algorithm ###
while total_students!=0:
    
    ### Calculates Want Values of Pairs ### ### Fix ###
    if(count==1):
        want1()
    else:
        want2()
    print pairs
    print("Calculates Want Values of Pairs: Yes")
    
    ### Duplicate Person Deleter ###
    pairs=sorted(pairs, key=lambda student: student[0], reverse=True)
    for i in range(len(pairs)):
        tf=True
        for pair in pairs2:
            if((pairs[i][1] in pair) or (pairs[i][2] in pair)):
                tf=False
        if(tf==True):
            pairs2.append(pairs[i])
    print pairs2
    print("Duplicate Person Deleter: Yes")
    
    ### Groups Equal Want Pairs ###
    pairsg = Counter(sub[0] for sub in pairs2).values()
    print pairsg
    print("Groups Equal Want Pairs: Yes")
    
    ### Places Into Final Groups ###
    if(count==1):
        placer1()
    else:
        placer2()
    print groups
    print("Places Into Final Groups: Yes")
    
    ### Deletes Students in Groups From Students List ###
    if(count==1):
        for g in groups:
            for g2 in g:
                student.append(g2)
    else:
        for g in groups:
            student.append(g[-1])
    
    for i in range(len(students)):
        if(students[i][0] not in student):
            students2.append(students[i])
    students=students2
    print(students)
    print("Students Deleted")
    
    ### Variable Refresher ###
    pairs=[]
    pairs2=[]
    student=[]
    students2=[]
    total_students=len(students)
    print("Varibles Refreshed")
    
    ### End of Loop ###
    print(str(count) + " loops done!")
    count+=1

### Group Want Values Average ###

for g in groups:
    g[0]=(round((g[0]/(len(g)-1))*100))/100

### End of Program ###
print("Done!")
print groups