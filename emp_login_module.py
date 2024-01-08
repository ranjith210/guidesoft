# e is acc_no dictionary

# t is transaction dictionary

def employeelogin(e,t):
	l1=["emp1","emp2"]
	l2=["35333","9089"]
	eu=input('Enter employee id: ')
	ep=input('Enter password: ')
	while 1:
		if eu in l1:
			if ep in l2:
				ch=int(input('(1) All users transactions\n(2) Single user Details\n(3) Selected users transactions\n(4) Exit\nEnter your choice: '))
				if ch==1:
					for i in t:
						print('Account No: ',i)
						printtransactions(t,i)
						print()
						print('--------------------------------------')
				if ch==2:				
					singleuserdetails(e,t)
				if ch==3:
					n=int(input('Enter Number of users: '))
					for i in range(1,n+1):
						ac=int(input('Enter Account No: '))
						printtransactions(t,ac)
						print()
						print('--------------------------------------')
				if ch==4:
					return				
			else:
				print('ENTERED INVALID CREDENTIALS')
				return
		else:
			print('ENTERED INVALID CREDENTIALS')
			return
def printtransactions(t,ac):
	if ac not in t:
		print('No User exists with AccountNo ',ac)
	else:
		if len(t[ac])==0:
			print('No transactions done yet')
		else:
			count,index=1,1
			print('TransNo\tFrom\tTo\tAmount\tTask')
			for j in t[ac]:
				if j=='not':
					continue
				if count==1:
					print(index,end='\t')
				if count%5!=0:
					print(t[ac][j],end='\t')
					count=count+1
				if count%5==0:
					index=index+1
					if index<=(t[ac]['not']+1):
						count=count+1
						print()
						print(index,end='\t')
def singleuserdetails(e,t):
	ac=int(input('Enter account no: '))
	if ac in e:										# if acc_no in acc_no dictionary
		while 1:
			emp_choice=int(input('\n(1) Details\n(2) Transactions\n(3) Exit\nEnter your choice: '))
			if emp_choice==1:	
				for i in e[ac]:
					print(i,':',e[ac][i])
			if emp_choice==2:
				printtransactions(t,ac)
			if emp_choice==3:
				return
	else:				
		print('INVALID ACCOUNT NUMBER')
