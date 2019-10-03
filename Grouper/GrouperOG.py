########################
### Grouping Program ###
########################

### Imports ###
from collections import Counter
import random
import math

### Variable Declaration ###
Ostudents=[["a","c","k","g","0"],["b","n","j","k","0"],["c","l","i","m","0"],["d","e","f","k","0"],["e","f","d","k","0"],["f","d","e","k","0"],["g","b","l","m","0"],["h","k","o","l","0"],["i","a","c","n","0"],["j","m","n","k","0"],["k","l","a","n","0"],["l","k","a","m","0"],["m","o","n","b","0"],["n","m","o","j","0"]]
student=[]
groups=[[]]
group_info=[] ### Stores who the people in the group wants to be with ###
group_happy=[0]
inputs=""
penguin=0
total_students=0
highest=[0]
number_group=input("How many groups can there be? ")
num_per_group=math.ceil(total_students/number_group)
print("Variable Declaration: Yes")

### Inputs ###
while inputs != "no":
    name=raw_input("Type your name: ")
    number1=raw_input("Type your #1 preference: ")
    number2=raw_input("Type your #2 preference: ")
    number3=raw_input("Type your #3 preference: ")
    unwanted=raw_input("Type the name of a person you dont like: ")
    Ostudents.append([name,number1,number2,number3,unwanted])
    inputs=raw_input("do you want to input another student(yes or no): ")
students=Ostudents
print("Inputs: Yes")

### Functions ###

def want():
    if(len(group)==0):
        for s1 in range(total_students): ### Chooses first person of the pair ###
            for s2 in range(s1+1,total_students): ### Chooses second person of the pair ###
                pairs.append([0, students[s1][0], students[s2][0]]) ### Creates the pair ###
                if(students[s1][0] in students[s2][1]): ### If the second person is the first person of the other's list ###
                    pairs[-1][0]+=5
                elif(students[s1][0] in students[s2][2]):
                    pairs[-1][0]+=3
                elif(students[s1][0] in students[s2][3]):
                    pairs[-1][0]+=1
                elif(students[s1][0] in students[s2][4]):
                    pairs[-1][0]-=4
                if(students[s2][0] in students[s1][1]): ### If the first person is in the other's list ###
                    pairs[-1][0]+=5
                elif(students[s2][0] in students[s1][2]):
                    pairs[-1][0]+=3
                elif(students[s2][0] in students[s1][3]):
                    pairs[-1][0]+=1
                elif(students[s2][0] in students[s1][4]):
                    pairs[-1][0]-=4
    else:
        for g in range(len(group)): ### Chooses one of the groupings for pairing ###
            for s in range(total_students): ### Chooses a person for pairing ###
                pairs.append([0, group[g], students[s][0]])
                for g2 in range(len(group_info[g])):
                    if(students[s][0] == group_info[g][g2][1]):
                        pairs[-1][0]+=2.5
                for g2 in range(len(group_info[g])):
                    if(students[s][0] == group_info[g][g2][2]):
                        pairs[-1][0]+=1.5
                for g2 in range(len(group_info[g])):
                    if(students[s][0] == group_info[g][g2][3]):
                        pairs[-1][0]+=0.5
                for g2 in range(len(group_info[g])):
                    if(students[s][0] == group_info[g][g2][4]):
                        pairs[-1][0]+=-2
                if(group[g][0] in students[s][1] or group[g][1] in students[s][1]):
                    pairs[-1][0]+=5
                elif(group[g][0] in students[s][2] or group[g][1] in students[s][2]):
                    pairs[-1][0]+=3
                elif(group[g][0] in students[s][3] or group[g][1] in students[s][3]):
                    pairs[-1][0]+=1
                elif(group[g][0] in students[s][4] or group[g][1] in students[s][4]):
                    pairs[-1][0]-=4
    return pairs
                
def placer():
    g=0
    p=0
    s=0
    if(len(group) == 0):
        while(len(group)<number_group):
            pair_remover(pairs2[p:p+pairsg[g+1]])
            #if(pairsg[g]+len(group)<=number_group):
            #    for i in range(pairsg[g]):  
            #        group.append(pairs2[p+i][1:])
            #        group_happy[0]+=pairs2[p+i][0]
            #else:
            #    for desk in range(pairsg[g]):
            #        choices(number_group-len(group)-1,desk,pairsg[g]-1,p,1)
            p+=pairsg[g]
            g+=1
        for g in range(len(group)):
            group_info.append([])
            for g2 in group[g]:
                num=0
                while num<len(students):
                    if(g2==students[num][0]):
                        group_info[g].append(students[num])
                        num=len(students)
                    num+=1
    else:
        if len(pairs2)>len(group):
            while s<len(group):
                if(pairsg[g]+s<=len(group)):
                    for i in range(pairsg[g]):  
                        group_place=group.index(pairs2[s+i][1])
                        group[group_place].append(pairs2[s+i][2])
                        group_happy[penguin]+=pairs2[s+i][0]
                else:
                    for desk in range(pairsg[g]):
                        choices(len(group)-s-1,desk,pairsg[g]-1,s,0)
                s+=pairs2[g]
                g+=1    
        else:
            while s<len(pairs2):
                group_place=group.index(pairs2[s][1])
                group[group_place].append(pairs2[s][2])
                group_happy[penguin]+=pairs2[s][0]
                s+=1
        for g in range(len(group)):
            num=0
            while num<len(students):
                if(group[g][-1]==students[num][0]):
                    group_info[g].append(students[num])
                    num=len(students)
                num+=1
    return group

def pair_remover(pairs2):
    conflicts=conflictions(pairs2)
    final_pairs=[]
    while len(conflicts) != 0:
        conflicts=conflictions(pairs2)
        for i in range(len(conflicts)):
            if (conflicts[i] == []):
                conflicts.pop(i)
                final_pairs.append(pairs2[i])
                pairs2.pop(i)
        num_conflicts=Counter(conflict for pair in conflicts for conflict in pair).values()
        num_conflicts_o = sorted(num_conflicts)
        if (num_conflicts_o[0] != num_conflicts_o[1]):
            num_conflictions = num_conflicts_o[0]
            while num_conflictions != 0:
                conflicts.pop(num_conflicts.index(num_conflicts_o[0]))

def conflictions(pairs):
    conflicts=[]
    for pair in range(len(pairs)):
        conflicts.append([])
        for test in range(len(pairs)):
            if (pairs[pair] != pairs[test]):
                if (pairs[pair][1] in pairs[test] or pairs[pair][2] in pairs[test]):
                    conflicts[pair].append(test)
    print(conflicts)
    return conflicts

#def choices(spots,future_adds,num_pairs,num,new):
#    if(new == 1):
#        if(spots!=0):
#            for add in range(future_adds[-1],num_pairs):
#                choices(spots-1, future_adds.append(add),num_pairs,num,1)
#        else:
#            groupa=group
#            group_happy.append(group_happy[0])
#            for a in future_adds:
#                groupa.append(pairs2[num+a][1:])
#                group_happy[-1]+=pairs2[num+a][0]
#            groups.append(groupa)
#    else:
#        if(spots!=0):
#            for add in range(future_adds[-1],num_pairs):
#                choices(spots-1, future_adds.append(add),num_pairs,num,0)
#        else:
#            for i in future_adds:
#                place=group.index(pairs2[num+i][1])
#                group[place].append(pairs2[num+i][2])
#                group_happy[penguin]+=pairs2[num+i][0]

def consolidator():
    equalWantPair = Counter(sub[0] for sub in pairs).values().reverse()
    for i in range(len(pairs)): ### Loops through pairs ###
        adder = 0
        count = 0
        while i<adder:
            adder += equalWantPair[count]
            count += 1
        tf=True
        for pair in pairs2[adder+1:]: ### Loops through pairs 2
            if((pairs[i][1] in pair) or (pairs[i][2] in pair)): ### Checks if one of the people in the pairs is already used ###
                tf=False
                break
        if(tf==True): ### If both are new ###
            pairs2.append(i) ### Adds the pairs to the shortend list ###
    return pairs2

def deletor():
    student = []
    for g in group: ### Selects each grouping ###
        for g2 in g: ### Selects each person from the grouping ###
            student.append(g2)
    for i in students: ### Selects each student ###
        if(i[0] not in student): ### Sees if that student was used ###
            students.pop(students.index(i))
    return students
    
print("Functions: Yes")

### Algorithm ###

print penguin
print len(groups)

while penguin < len(groups): ### Loops through all groupings that were tied ###
    group = groups[penguin] ### Chooses the group to work on ###
    students = Ostudents ### Refreshing the students variable ###
    if(len(group) != 0): ### If it is not a new group ###
        students = deletor()
    total_students = len(students)
        
    while total_students != 0: ### Loops while there are students left ###
        
        ### Variable Refresher ###
        pairs=[]
        pairs2=[]
        student=[]
        print("Varibles Refreshed")
        
        pairs = want() ### Calculates Want Values of Pairs ###
        print pairs
        print("Calculates Want Values of Pairs: Yes")
        
        ### Duplicate Person Deleter ###
        pairs = sorted(pairs, key=lambda student: student[0], reverse=True) ### Sortes by want value ###
        pairs2 = consolidator()
        print pairs2
        print("Duplicate Person Deleter: Yes")
        
        ### group Equal Want Pairs ###
        pairsg = Counter(sub[0] for sub in pairs2).values().reverse() ### Counts how many of each want value there are ###
        print pairsg
        print("group Equal Want Pairs: Yes")
        
        ### Places Into Final group ###
        group = placer()
        print group
        print("Places Into Final group: Yes")
        
        ### Deletes Students in group From Students List ###
        students = deletor()
        total_students=len(students)
        print(students)
        print("Students Deleted")
        
        ### End of Loop ###
        print("Loop Done!")
    penguin+=1

for i in range(1,len(group_happy)):
    if(group_happy[i]>group_happy[highest[0]]):
        highest=[i]
    elif(group_happy[i]==group_happy[highest[0]]):
        highest.append(i)
        
### End of Program ###
for j in highest:
    print(groups[j])
print("Done!")