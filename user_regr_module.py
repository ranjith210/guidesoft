from random import randint
def details(d,a,c,t,l3):
	p={}
	setname(p)
	setphoneno(p)
	setdob(p)
	setbal(p)
	setaddress(p)
	setacno(p,l3)
	uploaduidpd(d,a,c,t,p)
	return d,a,c
def setname(p):
	name=input('Enter Name: (atleast 5 characters) ')
	if len(name)<5 and not(name.isalpha()):
		print('Enter valid Name: ')
		setname(p)
	else:
		p['Name']=name
def setphoneno(p):
	phno=input("Enter Phone number: ")
	if phno.isdigit():
		if len(phno)==10 and int(phno[0])>5:
			p["Phone Number"]=phno
		else:
			print("ENTER A VALID PHONE NUMBER")
			setphoneno(p)
	else:
		print("ENTER A VALID PHONE NUMBER")
		setphoneno(p)
def setdob(p):		
	dob=input('Enter date of birth(DD/MM/YYYY): ')
	if len(dob)==10 and int(dob[0:2])<=31 and int(dob[3:5])<=12 and int(dob[6:10])>1940 and int(dob[6:10])<2020 and dob[2]=='/' and dob[5]=='/':
		p['Date of birth']=dob
		p['Age']=2020-int(dob[6:10])
		if p['Age']<18:
			print("You're registered for Student Account")
			p['Account type']='Student'
		else:
			p['Account type']='Major'
	else:
		print('PLEASE ENTER A VALID DATE OF BIRTH')
		setdob(p)
def setbal(p):
	if p['Age']<18:
		p['Balance']=randint(1000,99999)
	else:
		p['Balance']=randint(1000,2000000)
def setaddress(p):
	doorno=input('Enter DoorNo: ')
	streetname=input('Enter StreetName: ')
	city=input('Enter City: ')
	if len(city)>=4 and city.isalpha() and len(streetname)>=4 and len(doorno)>=4:
		p['Door No']=doorno
		p['Street Name']=streetname
		p['City']=city
	else:
		print("PLEASE ENTER VALID ADDRESS DETAILS")
		setaddress(p) 
def setacno(p,l3):	
	while 1:
			i=randint(1000,9999)
			if i not in l3:
				p['Account No']=i
				l3.append(i)
				break
def uploaduidpd(d,a,c,t,p):
	uid=input('Enter UserId:(minimum 4 characters): ')
	pd=input('Enter Password:(minimum 4 characters): ')
	if len(uid)>=4 and len(pd)>=4:
		if check(uid,pd,d):
			k={}
			k[uid]={}
			k[uid][pd]=p.copy()
			d.update(k)
			a[p['Account No']]=p.copy()
			c[p['Account No']]={}
			c[p['Account No']][uid]=pd
			t[p['Account No']]={}
			print('Your Account No is:',p['Account No'])
			print('Your A/C balance: ',p['Balance'])
			print('Details are saved...')
		else:
			print('Try to save with another userid and password')
			uploaduidpd(d,a,c,t,p)
	else:
		print("PLEASE ENTER VALID USERNAME AND PASSWORD")
		uploaduidpd(d,a,c,t,p)
def check(uid,pd,d):
	if uid in d:
		if pd in d[uid]:
			return False
	else:
		return True