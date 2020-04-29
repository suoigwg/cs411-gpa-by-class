import json
import copy

with open('parsed_prereq.txt', "r") as f:
    data = f.read()
with open("avg_gpa.json","r") as f1:
    dt=f1.read()


gpa=json.loads(dt)
dic = json.loads(data)
print(type(dic))


def decompose(prereq, lis):
    if type(prereq) == str:
        if lis:
            if type(lis[0]) != str:
                for i in range(len(lis)):
                    lis[i].append(prereq)
            else:
                lis.append(prereq)
        else:
            lis.append(prereq)
    elif type(prereq) == dict:
        for key in prereq.keys():
            if key == 'and':
                decompose(prereq[key],lis)
            elif key == 'or':
                lor = []
                for i in range(len(prereq[key])):
                    ll = copy.deepcopy(lis)
                    decompose(prereq[key][i],ll)
                    if len(lis) == 0:
                        lor.append(ll)
                    else:
                        for i in range(len(ll)):
                            lor.append(ll[i])
                lis.clear()
                for i in lor:
                    lis.append(i)
    else:
        for i in range(len(prereq)):
            decompose(prereq[i],lis)


if __name__ == '__main__':
    outF = open("course_preq.txt", "w")
    for key in dic.keys():
        if key in gpa.keys():
            record={}
            list = []
            decompose(dic[key],list)
            #print(list)
            record['Course'] = key
            record['Prereq'] = []
            record['AvgGpa'] = gpa[key]
            if type(list[0]) == str:
                d = {}
                while list:
                    temp = list.pop()
                    if type(temp) != str:
                        temp = temp[0]
                    if temp in gpa.keys():
                        d[temp] = gpa[temp]
                record['Prereq'].append(d)
            else:
                for i in range(len(list)):
                    d={}
                    while list[i]:
                        temp = list[i].pop()
                        if type(temp) != str:
                            for tt in range(len(temp)):
                                if tt in gpa.keys():
                                    d[tt] = gpa[tt]
                        else:
                            if temp in gpa.keys():
                                d[temp]=gpa[temp]
                    record['Prereq'].append(d)
            print(record)
            outF.write(str(record))
            outF.write("\n")
    outF.close()


