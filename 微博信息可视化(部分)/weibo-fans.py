import xlrd
import matplotlib.pyplot as plt

file = 'news.xls'

wb = xlrd.open_workbook(file)       #导入文件
ws = wb.sheet_by_name('Sheet1')     #导入Sheet1
sheet1 = wb.sheet_by_index(0)       #通过目录导入


cols = sheet1.col_values(7)         #导入第8列的数据
temp = ' '.join(cols)               #将第八列数据存为str类型
data_weibofans = temp.split( )      #去除空格
del data_weibofans[0]            #删除第一个元素
count = 0   

for i in data_weibofans[:]:      # 计算并移除"不显示"的字符串
    if i == "不显示":
        count += 1
        data_weibofans.remove(i)
    else:
        pass


data_x = []                         #x轴数据
new_data_weibofans = []          #int数据的列表


for r in data_weibofans:
    new_data_weibofans.append(int(r))

     
#print(new_data_weibofans)


def num_data(list1, list2):              #list1:int型列表总数据  list2:存储数量
    num1,num2,num3,num4 = 0,0,0,0
    for i in list1[:]:
        if i >= 1 and i <= 1000:
            num1 += 1
        elif i > 1000 and i <= 10000:
            num2 += 1
        elif i >10000 and i <= 100000:
            num3 += 1
        else:
            num4 += 1
    list2.append(num1)
    list2.append(num2)
    list2.append(num3)
    list2.append(num4)

num_data(new_data_weibofans, data_x)

data_x.append(count)


x = ['1~1000', '1000~10000', '10000~100000', '>100000', 'blank']

y = data_x

 

#create new figure

plt.figure("虚假新闻")

plt.xlabel('weibo_fans')
plt.ylabel('population')
plt.title('weibo_fans_population')
#线


plt.plot(x, y)

 


plt.show()
