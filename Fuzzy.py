import csv

def bacaData():
	f = open('influencers.csv', 'r')
	reader = csv.reader(f)
	a=[];b=[];c=[]
	for row in reader:
	    a.append(row[0])
	    b.append(row[1])
	    c.append(row[2])
	data=[]
	for x in range(1, 101):
		temp=[]
		temp.append(int(a[x]))
		temp.append(int(b[x]))
		temp.append(float(c[x]))
		data.append(temp)
	f.close()
	return data

#Fuzzifikasi
def follower(data):
	temp=[]
	for x in range(len(data)):
		foll=[]
		rendah=0;sedang=0;tinggi=0
		#rendah
		if(data[x][1]<=18000):
			rendah=1
		elif(data[x][1]<=25000 and data[x][1]>18000):
			rendah=(data[x][1]+18000)/(18000+25000)
		#sedang
		if(data[x][1]>=25000 and data[x][1]<=45000):
			sedang=1
		elif(data[x][1]<=25000 and data[x][1]>18000):
			sedang=(25000-data[x][1])/(18000+25000)
		elif(data[x][1]<=47000 and data[x][1]>45000):
			sedang=(data[x][1]+45000)/(45000+47000)
		#tinggi
		if(data[x][1]>=47000):
			tinggi=1
		elif(data[x][1]<=47000 and data[x][1]>45000):
			tinggi=(47000-data[x][1])/(47000+45000)
		foll.append(rendah);foll.append(sedang);foll.append(tinggi)
		temp.append(foll)
	return temp

def engagement(data):
	temp=[]
	for x in range(len(data)):
		eng=[]
		rendah=0;tinggi=0;
		#rendah
		if(data[x][2]<=4):
			rendah=1
		elif(data[x][2]<=6 and data[x][2]>4):
			rendah=(data[x][2]+4)/(4+6)
		#tinggi
		if(data[x][2]>=6):
			tinggi=1
		elif(data[x][2]<=6 and data[x][2]>4):
			tinggi=(6-data[x][2])/(4+6)
		eng.append(rendah);eng.append(tinggi)
		temp.append(eng)
	return temp

#Rule Inferensi
	#eng\foll 	r 	s 	t
	#r 			n 	n 	n
	#t 			n 	y 	y

def inferensiDefuzikasi(foll, eng):
	inf=[]
	for x in range(len(foll)):
		temp=[];temp1=[];temp2=[]
		if(foll[x][0]!=0 and eng[x][0]!=0):
			temp.append(50*min(foll[x][0],eng[x][0]))
			temp1.append(min(foll[x][0],eng[x][0]))
		if(foll[x][1]!=0 and eng[x][0]!=0):
			temp.append(50*min(foll[x][1],eng[x][0]))
			temp1.append(min(foll[x][1],eng[x][0]))
		if(foll[x][2]!=0 and eng[x][0]!=0):
			temp.append(50*min(foll[x][2],eng[x][0]))
			temp1.append(min(foll[x][2],eng[x][0]))
		if(foll[x][0]!=0 and eng[x][1]!=0):
			temp.append(50*min(foll[x][0],eng[x][1]))
			temp1.append(min(foll[x][0],eng[x][1]))
		if(foll[x][1]!=0 and eng[x][1]!=0):
			temp.append(80*min(foll[x][1],eng[x][1]))
			temp1.append(min(foll[x][1],eng[x][1]))
		if(foll[x][2]!=0 and eng[x][1]!=0):
			temp.append(80*min(foll[x][2],eng[x][1]))
			temp1.append(min(foll[x][2],eng[x][1]))
		if(len(temp)==1):
			temp2.append(temp[0]/temp1[0]);temp2.append(x+1)
		else:
			temp2.append(temp[0]+temp[1]/temp1[0]+temp1[1]);temp2.append(x+1)
		inf.append(temp2)
	return inf

def takesecond(a):
    return a[0]

#Menulis jawaban
def tulisJawaban(jawaban):
	file = open('hasil.csv', 'w', newline='')
	filecsv = csv.writer(file)
	filecsv.writerows(jawaban)
	file.close()

#Main Program
z=[]
jawaban=[]
a=follower(bacaData())
b=engagement(bacaData())
sortedlist = sorted(inferensiDefuzikasi(a,b), key=takesecond)
for i in reversed(sortedlist):
	z.append(i)
for x in range(20):
	c=[];c.append(z[x][1])
	jawaban.append(c)
print(jawaban)
tulisJawaban(jawaban)
print('\t\t\tJawaban Berhasil Disimpan Pada hasil.csv ')