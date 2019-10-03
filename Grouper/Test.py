from collections import Counter

x=["Hello!","Hi"]
y="e"
z=[[1,2],[3,4],[5,6]]
a=[1,1,1,1,1,2,2,2,2,3,3,3,4,4,0]
b=[[1,1,2],[2,2,3],[3,3,3],[4],[0,0,2]]

def test1():
    if y in x:
        print("yes")
    else:
        print("no")

def test2():
    print(type(x))
    if(type(x)==type([])):
        print("Yes")
    
def test3():
    print(z[1:])

def test4():
    if(1 in z):
        print("yes")
    else:
        print("no")

def test5():
    if(3 not in pair1 for pair1 in z):
        print("no")
    tf=True    
    for pair1 in z:
        if(3 in pair1):
            tf=False       ### Swicth all cases of this with a return to end the loop once it is false. ###
    if(tf==False):
        print("No")
        
def test6():
    print(a.index(3))

def test7():
    print(Counter(d for c in b for d in c).values())
    print(sorted(Counter(d for c in b for d in c).values()))
    
def test8():
    x=[1,2,3,4,5,3]
    for z in x:
        if z==3:
            x.pop(x.index(3))
            print x

def test9(pairs):
    conflicts, pairs, final_pairs=test10(pairs, [])
    while len(conflicts) != 0:
        num_conflicts = Counter(conflict for pair in conflicts for conflict in pair).values()
        num_conflicts_o = sorted(num_conflicts)
        least_occurences = num_conflicts_o[0]
        if (least_occurences != num_conflicts_o[1]):
            while least_occurences != 0:
                pairs.pop(num_conflicts.index(num_conflicts_o[0]))
                least_occurences-=1
        else:
            least_value=[i for i,value in enumerate(num_conflicts) if value == least_occurences] ### Places of the least values ###
            pairs_temp=[]
            possible_final_pairs=[]
            print("Pairs = " + str(pairs))
            for i in least_value:
                if [v for c,v in enumerate(pairs) if c not in conflicts[i]] not in pairs_temp:
                    pairs_temp.append([v for c,v in enumerate(pairs) if c not in conflicts[i]])
                    possible_final_pairs.append(test9(pairs_temp))
            print("Possible final pairs = " + str(possible_final_pairs))
            possible_final_pairs2d=test17(possible_final_pairs)
            print("Possible final pairs 2D = " + str(possible_final_pairs2d))
            possible_final_pairs_add=sorted(i for i in possible_final_pairs2d)
            print("Possible final pairs add = " + str(possible_final_pairs_add))
            final_pairs_add=[]
            for i in possible_final_pairs_add:
                if i not in final_pairs_add:
                    final_pairs_add.append(i)
            print("Final pairs add = " + str(final_pairs_add))
            if(len(final_pairs) == 0 or type(final_pairs[0][0]) != type([])):
                final_pairs=[final_pairs]
            print("Final Pairs = " + str(final_pairs))
            for i in range(len(final_pairs_add)-1):
                final_pairs.append(list(final_pairs[-1]))
            print("Final pairs extended = " + str(final_pairs))
            for i in range(len(final_pairs_add)):
                for c in final_pairs_add[i]:
                    final_pairs[i].append(c)
            print("Final pairs extended and added = " + str(final_pairs))
            pairs=[]
        conflicts, pairs, final_pairs=test10(pairs, final_pairs)
        print("Final pairs = " + str(final_pairs))
    return(final_pairs)
    
def test10(pairs, final_pairs):
    conflicts=[]
    for pair in range(len(pairs)):
        conflicts.append([])
        for test in range(len(pairs)):
            if (pairs[pair] != pairs[test]):
                if (pairs[pair][1] in pairs[test] or pairs[pair][2] in pairs[test]):
                    conflicts[pair].append(test)
    delete=[]
    for i in range(len(conflicts)):
        if (conflicts[i] == []):
            delete.append(i)
    for i in reversed(range(len(delete))):
        conflicts.pop(delete[i])
        final_pairs.append(pairs[delete[i]])
        pairs.pop(delete[i])
    for conflict in range(len(conflicts)):
        for conflictor in range(len(conflicts[conflict])):
            for deleted in sorted(delete, reverse=True):
                if conflicts[conflict][conflictor] >= deleted:
                    conflicts[conflict][conflictor]-=1
    return conflicts, pairs, final_pairs
      
def test11():
    for c in b:
        for d in c:
            d-=1
    print b

def test12():
    sorted_list=sorted([1,4,3,5,7,2])
    print(type(sorted_list))
    
def test13():
    c=3
    a.pop(-c)
    print(a)

def test14():
    print(a[:-1])

def test15():
    testing_list=[[1,2,3],[1,2,3]]
    num=1
    testing_list[num].append(2)
    print(testing_list)
    
def test16():
    l=[[0,'a','a'],[0,'c','a'],[0,'a','b'],[0,'b','a']]
    print(sorted(l))
    
def test17(test_list):
    final_list=[]
    for i in test_list:
        if (type(i[0][0]) == type([])):
            list_add=test17(i)
            for t in list_add:
                final_list.append(t)
        else:
            final_list.append(i)
    return(final_list)

def test18():
    alpha=[]
    alpha.append(a)
    print alpha

#final_pairings=test9([[0,'a','b'],[0,'c','d'],[0,'e','f'],[0,'c','b'],[0,'g','h'],[0,'g','i']])
#final_pairings=test9([[0,'a','b'],[0,'c','d'],[0,'a','d'],[0,'c','b']])
#final_pairings=test9([[0,'a','b'],[0,'b','c'],[0,'c','d'],[0,'d','a'],[0,'e','f']])
#final_pairings=test9([[0,'a','b'],[0,'c','d'],[0,'e','f'],[0,'c','b'],[0,'g','h'],[0,'i','j'],[0,'h','i']])
#print("Done: " + str(final_pairings))

test18()