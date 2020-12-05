from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import FileUpload
from requests import get
import tabula

public_ip = get('http://api.ipify.org/').text

def calculate(file_path):
    k=tabula.read_pdf(file_path,pages="all")
    code = int(k[0][k[0].columns[1]][2][9])
    d=k[0][4:]
    name=d.columns[1]

    #print(f"Name:{name}\nPaper Code:{code}")

    array=[]    

    array=[]
    pk=(code%2)+2
    for i in range(len(d['Name'])):
        array.append([i+1,d[name][i+4]])
    for j in range(1,pk):        
        array.append([int(k[j].columns[0]),k[j].columns[1]])
        for i in range(len(k[j][k[j].columns[1]])):
            array.append([int(k[j].columns[0])+1+i,k[j][k[j].columns[1]][i]])
    for i in array:
        if i[1] == "--" or i[1] == 'NA' or i[1] == 'Not Answered':
            i[1]="10000"


    if code==3:
        q=[[1, '3',1,0],[2, '4',1,0],[3, '4',1,0],[4, '4',1,0],[5, '1',1,0],[6, '1',1,0],[7, '2',1,0],[8, '1',1,0],[9, '2',1,0],[10, '1',1,0],[11, '1',1,0],[12, '3',1,0],[13, '2',1,0],[14, '1',1,0],[15, '1',1,0],[16, '1',1,0],[17, '1',1,0],[18, '2',1,0],[19, '2',1,0],[20, '2',1,0],[21, '2',1,0],[22, '2',1,0],[23, '1',1,0],[24, '2',1,0],[25, '2',1,0],[26, '2',1,0],[27, '3',1,0],[28, '1',1,0],[29, '2',1,0],[30, '3',1,0],[31, '3',1,0],[32, '3',1,0],[33, '1',1,0],[34, '2',1,0],[35, '1',1,0],[36, '4',1,0],[37, '2',1,0],[38, '2',1,0],[39, '2',1,0],[40, '1',1,0],[41, '2',1,0],[42, '1',1,0],[43, '2',1,0],[44, '1',1,0],[45, '2',1,0],[46, '2',1,0],[47, '1',1,0],[48, '2',1,0],[49, '2',1,0],[50, '2',1,0],[51, '1',0,0],[52, '2',3,0],[53, '4',3,0],[54, '3',3,0],[55, '3',3,0],[56, '3',3,0],[57, '2',3,0],[58, '2,4',3,1],[59, '4',4,0],[60, '4',4,0],[61, '1,4',5,1],[62, '3,4',5,1],[63, '1',5,0],[64, '2,4',6,1],[65, '3',3,0],[66, '6',3,0],[67, '1',3,0],[68, '3',3,0],[69, '3',1,0],[70, '1,3,5',1,1],[71, '3,7',3,1],[72, '2,3',3,1],[73, '1,2,3',3,1],[74, '[300,300]',3,2],[75, '[9,9]',1,2],[76, '[8,8]',3,2],[77, '[2,2]',1,2],[78, '1,2,4',1,1],[79, '2,5',1,1],[80, '[4.8,5.2]',3,2],[81, '[0.48,0.53]',5,2],[82, '2',1,0],[83, '[0.875,0.875]',1,2],[84, '2',1,0],[85, '[52,52]',1,2],[86, '[32.4,32.9]',5,2],[87, '1',0,0],[88, '3',2,0],[89, '2',2,0],[90, '1',3,0],[91, '6',3,0],[92, '3,4',2,1],[93, '2,3,4',4,1],[94, '1,4',5,1],[95, '2,3,5',5,1],[96, '[6,6]',4,2],[97, '[10,10]',5,2],[98, '1,3',3,1],[99, '1,2',3,1],[100, '1,4,5',4,1],[101, '3',3,0],[102, '[41,41]',2,2]]

    elif code==2:
        q=[[1, '3',1,0],[2, '1',1,0],[3, '2',1,0],[4, '4',1,0],[5, '1',1,0],[6, '3',1,0],[7, '4',1,0],[8, '3',1,0],[9, '6',1,0],[10, '2',1,0],[11, '2,4,6,9,10,13,14,15,16,17',10,1],[12, '2',1,0],[13, '3',1,0],[14, '2',1,0],[15, '1',1,0],[16, '1',1,0],[17, '2',1,0],[18, '1',1,0],[19, '3',1,0],[20, '3',1,0],[21, '3',1,0],[22, '2',1,0],[23, '2',1,0],[24, '1',1,0],[25, '2',1,0],[26, '1',1,0],[27, '1',1,0],[28, '2',1,0],[29, '1',1,0],[30, '1',1,0],[31, '1',1,0],[32, '2',1,0],[33, '2',1,0],[34, '2',1,0],[35, '1',1,0],[36, '2',1,0],[37, '2',1,0],[38, '1',1,0],[39, '2',1,0],[40, '2',1,0],[41, '2',1,0],[42, '1',0,0],[43, '3',3,0],[44, '4',3,0],[45, '2',3,0],[46, '3',3,0],[47, '3',3,0],[48, '1',3,0],[49, '4',4,0],[50, '4',4,0],[51, '1',5,0],[52, '3,4',3,1],[53, '1,4',5,1],[54, '2,3',5,1],[55, '1,2',6,1],[56, '2',3,0],[57, '6',3,0],[58, '2',3,0],[59, '1',3,0],[60, '2',1,0],[61, '2,3,4',1,1],[62, '1,3,4',3,1],[63, '1,2',3,1],[64, '1,2,4',3,1],[65, '[125,125]',3,2],[66, '[9,9]',1,2],[67, '[6,6]',3,2],[68, '[2,2]',1,2],[69, '1,4',1,1],[70, '2,4',1,1],[71, '[3.9,4.3]',3,2],[72, '[0.47,0.52]',5,2],[73, '2',1,0],[74, '[0.8625,0.8625]',1,2],[75, '2',1,0],[76, '[60,60]',1,2],[77, '[32.1,32.5]',5,2],[78, '1',0,0],[79, '3',3,0],[80, '1,3',2,1],[81, '1,2,4',5,1],[82, '1,3,4',5,1],[83, '1,3,5',5,1],[84, '2,3,4',3,1],[85, '[0,0]',2,2],[86, '[40,40]',2,2],[87, '[32,32]',3,2],[88, '[9,9]',4,2],[89, '[4.2,4.2]',5,2],[90, '[1.6,1.6]',3,2],[91, '3,4',5,1],[92, '3',3,0]]

    elif code==1:
        q=[[1, '4',1,0],[2, '3',1,0],[3, '2',1,0],[4, '3',1,0],[5, '4',1,0],[6, '4',1,0],[7, '3',1,0],[8, '3',1,0],[9, '2',1,0],[10, '4',1,0],[11, '3',1,0],[12, '1',1,0],[13, '1',1,0],[14, '2',1,0],[15, '2',1,0],[16, '2,6,8,9,10',5,1],[17, '2',1,0],[18, '4',1,0],[19, '2',1,0],[20, '3',1,0],[21, '1',1,0],[22, '2',1,0],[23, '3',1,0],[24, '1',1,0],[25, '2',1,0],[26, '2',1,0],[27, '1',1,0],[28, '3',1,0],[29, '2',1,0],[30, '1',1,0],[31, '1',1,0],[32, '4',1,0],[33, '2',1,0],[34, '2',1,0],[35, '1',1,0],[36, '1',1,0],[37, '2',1,0],[38, '1',1,0],[39, '1',1,0],[40, '1',1,0],[41, '1',1,0],[42, '1',1,0],[43, '2',1,0],[44, '1',1,0],[45, '1',1,0],[46, '1',1,0],[47, '1',0,0],[48, '2',3,0],[49, '2',3,0],[50, '3',3,0],[51, '4',3,0],[52, '4',3,0],[53, '2',3,0],[54, '2,4',3,1],[55, '2',4,0],[56, '4',4,0],[57, '2',5,0],[58, '2,4',5,1],[59, '3,5',5,1],[60, '2,4',6,1],[61, '4',3,0],[62, '1',3,0],[63, '4',3,0],[64, '3',1,0],[65, '1,3,4',1,1],[66, '1,3,7',3,1],[67, '1,3,5',3,1],[68, '1,2,3',3,1],[69, '[225,225]',3,2],[70, '[39,39]',3,2],[71, '[29,29]',1,2],[72, '[4,4]',3,2],[73, '[5.5,5.5]',1,2],[74, '1,4',1,1],[75, '2,4',1,1],[76, '[3.2,3.5]',3,2],[77, '[0.52,0.56]',5,2],[78, '3',1,0],[79, '[0.91,0.92]',1,2],[80, '1',1,0],[81, '[50,50]',1,2],[82, '[23.9,24.4]',5,2],[83, '1',0,0],[84, '[60,60]',2,2],[85, '[8,8]',4,2],[86, '[25,25]',5,2],[87, '1,3',2,1],[88, '1,3,4',4,1],[89, '1,3,4',3,1],[90, '2',2,0],[91, '3',2,0],[92, '3',2,0],[93, '2',3,0],[94, '3',3,0],[95, '1,2,3',4,1],[96, '1,4',3,1],[97, '1,5',5,1],[98, '4',4,0],[99, '[40,40]',2,2]]

    count=0
    engcount=0
    ctcount=0
    statcount=0
    mathcount=0
    MSQ=[]
    #print("English Wrong Answer:\n")
    #print("Q.No\t\tYours\t\tRight")
    for i in range(len(array)):
        if (i==50 and code==3) or (i==46 and code==1) or (i==42 and code==2):
            engcount=count
            #print("\n\nCT Wrong Answer:")
            #print("Q.No\t\tYours\t\tRight")
        if (i==64 and code==3) or (i==60 and code==1) or (i==55 and code==2):
            ctcount=count-engcount
            #print("\n\nStat Wrong Answer:")
            #print("Q.No\t\tYours\t\tRight")
        if (i==86 and code==3) or (i==82 and code==1) or (i==78 and code==2):
            statcount=count-ctcount-engcount
            #print("\n\nMaths Wrong Answer")
            #print("Q.No\t\tYours\t\tRight")
        if q[i][3]==0:
            if int(q[i][1])==int(array[i][1]):
                count+=int(q[i][2])
                continue
            print(i+1,"\t\t",array[i][1],"\t\t",q[i][1])
        elif q[i][3]==1:
            q[i][1]=q[i][1].split(",")
            try:  
              array[i][1]=array[i][1].split(",")
              lk=0
              for j in array[i][1]:
                  if j not in q[i][1]:
                    lk=lk+1
                    print(i+1,"\t\t",array[i][1],"\t\t",q[i][1])
                    break
              if lk==0:
                temp=float(q[i][2])*float(len(array[i][1]))/float(len(q[i][1]))
                count+=temp
                MSQ.append([i+1,array[i][1],q[i][1],temp])
              continue      
            except:
              array[i][1]=f"[{array[i][1]}]"
              array[i][1]=array[i][1].split(",")
              # print("success",array[i][1])
              lk=0
              for j in array[i][1]:
                  if j not in q[i][1]:
                    lk=lk+1
                    #print(i+1,"\t\t",array[i][1],"\t\t",q[i][1])
                    break
              if lk==0:
                temp=float(q[i][2])*float(len(array[i][1]))/float(len(q[i][1]))
                count+=temp
                MSQ.append([i+1,array[i][1],q[i][1],temp])
              continue
        elif q[i][3]==2:
            q[i][1]=q[i][1].strip("'[]'")
            q[i][1]=q[i][1].split(",")
           
            if float(array[i][1])>=float(q[i][1][0]) and float(array[i][1])<=float(q[i][1][1]):
                count += int(q[i][2])
                continue
            elif float(q[i][1][0])==float(q[i][1][1]):
                print(i+1,"\t\t",array[i][1],"\t\t",q[i][1][0])
            else:
                print(i+1,"\t\t",array[i][1],"\t\t",q[i][1])

    mathcount=count-engcount-statcount-ctcount

    if int(array[7][1])!=3 and code==2:
        count+=1
        engcount+=1
    if int(array[9][1])!=1 and code==3:
        count+=1
        engcount+=1

    if code == 2:
        if float(array[86][1])>=float(8) and float(array[86][1])<=float(8):
            count += int(2)
            mathcount+=2

        if float(array[89][1])>=float(-1.6) and float(array[89][1])<=float(-1.6):
            count += int(2)
            mathcount+=2
    total_percentage = float(count)/2
    #print(f"Total Marks:{count}\nTotal Percentage:{float(count)/2}\n\nSubject Wise Marks\nEnglish:{engcount}\nCT:{ctcount}\nStat:{statcount}\nMaths:{mathcount}\n\nSubject Wise Percentage\nEnglish:{engcount*2}\nCT:{ctcount*2}\nStat:{statcount*2}\nMaths:{mathcount*2}")
    
    return name, code,'{:.2f}'.format(count),'{:.2f}'.format(total_percentage), '{:.2f}'.format(engcount),'{:.2f}'.format(ctcount),'{:.2f}'.format(statcount),'{:.2f}'.format(mathcount),'{:.2f}'.format(engcount*2),'{:.2f}'.format(ctcount*2),'{:.2f}'.format(statcount*2),'{:.2f}'.format(mathcount*2)

# Create your views here.
def home(request):
    return render(request, 'index.htm', {'something': False,'ip': public_ip})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file_upload = request.FILES['file']
        name, code, count, total_percentage, engcount, ctcount, statcount, mathcount, engper, ctper, statper, mathper = calculate(file_upload)
        file_details = FileUpload(
            file_uploaded = file_upload,
            public_ip = public_ip,
            name = name,
            paper_code = code,
            total_marks = count,
            engcount =engcount,
            ctcount = ctcount,
            statcount = statcount,
            mathcount = mathcount,
        )
        file_details.save()

        return render(request, 'index.htm', {'something': True,'ip': public_ip,'name': name, 'code': code, 'count': count, 'total_percentage': total_percentage, 'engcount': engcount, 'ctcount': ctcount, 'statcount': statcount, 'mathcount': mathcount, 'engper': engper, 'ctper': ctper, 'statper': statper, 'mathper': mathper})
    else:
        return render(request, 'index.htm', {'something': False,'ip': public_ip})
