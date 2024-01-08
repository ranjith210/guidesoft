# d is data dictionary, having user_id as key and value as a dictionary containg key as password and value as user details

# k is account number dictionary; acc_no as key and user details as value

# trans is transaction dictionary; acc_no as key and transaction details(from,to,amount,no.of trans,debited/credited) as value

# c is a dictionary; key=acc_no and value={user_id:password}
def userlogin(d,k,trans,c):
	print('\nLOGIN\n')
	u_id=input('Enter UserId: ')
	u_pswd=input('Enter Password: ')
	if u_id in d:
		if u_pswd in d[u_id]:
			while 1:
				user_choice=int(input('(1) Personal Details\n(2) Withdraw\n(3) Balance\n(4) Transfer\n(5) Transaction details\n(6) Exit\nEnter your choice: '))
				if user_choice==1:
					personal(u_id,u_pswd,d)
					print('--------------------------------------\n')		
				if user_choice==2:
					withdraw(u_id,u_pswd,d,k)					
					print('--------------------------------------\n')		
				if user_choice==3:
					balance(u_id,u_pswd,d)
					print('--------------------------------------\n')
				if user_choice==4:
					transfer(u_id,u_pswd,d,k,trans,c)
					print('--------------------------------------\n')
				if user_choice==5:
					transactiondetails(d,u_id,u_pswd,trans)
					print()
					print('--------------------------------------\n')
				if user_choice==6:	
					return trans
			else:
				print('ENTERED INVALID CREDENTIALS')
				return
		else:
			print('ENTERED INVALID CREDENTIALS')
			return
		
def personal(u,l,d):
	for i in d[u][l].keys():	
		print(i,':',d[u][l][i])
def withdraw(u,l,d,k):
	print('Your Balance is: ',d[u][l]['Balance'])
	amount=int(input('Enter amount to withdraw: '))
	if amount<=d[u][l]['Balance']:
		if d[u][l]['Account type']=='Student':
			if amount<=10000:			
				d[u][l]['Balance']-=amount
				ac=d[u][l]['Account No']											# ac is account number of current user
				k[ac]['Balance']-=amount
				print(amount,'is deducted from your account')
				print('Your Balance is: ',d[u][l]['Balance'])
			else:
				print('Student account cannot able to withdraw more than 10000rs')
		else:
			d[u][l]['Balance']-=amount
			ac=d[u][l]['Account No']
			k[ac]['Balance']-=amount
			print(amount,'is deducted from your account')
			print('Your Balance is:',d[u][l]['Balance'])
	else:
		print('Insufficient Amount')
def balance(u,l,d):
	print('Balance: ',d[u][l]['Balance'])
def transfer(u,l,d,k,trans,c):
	ac2=int(input('Enter account no to transfer:'))
	if ac2==d[u][l]['Account No']:
		print("CANNOT TRANSFER MONEY TO THE SAME ACCOUNT")
	else:
		if ac2 in k:
			amt=int(input('Enter amount: '))
			if amt<=d[u][l]['Balance']:			
				ac=d[u][l]['Account No']
				k[ac]['Balance']-=amt
				k[ac2]['Balance']+=amt
				d[u][l]['Balance']-=amt
				for i in c[ac2]:
					u1=i
					l1=c[ac2][i]
				d[u1][l1]['Balance']+=amt
				upload(ac,ac2,amt,trans)
				print(amt,' is transfered from your account to',ac2)
				print('Your Balance is:',d[u][l]['Balance'])
			else:
				print('INSUFFICIENT AMOUNT. UNABLE TO PROCESS TRANSACTION')
		else:
			print('Account Number',ac2,'not found')
def upload(ac,ac2,amt,trans):
	p,x={},{}
	if len(trans[ac])>=1:
		trans[ac]['not']+=1							        	# not is no.of transactions
		n=trans[ac]['not']
		nfro='From'+str(n)										# n is transaction number
		nto='To'+str(n)
		namt='Amount'+str(n)
		ntsk='Task'+str(n)
		p[nfro]=ac
		p[nto]=ac2
		p[namt]=amt
		p[ntsk]='Debited'
		trans[ac].update(p)
	if len(trans[ac2])>=1:
		trans[ac2]['not']+=1
		n1=trans[ac2]['not']
		nfro='From'+str(n1)
		nto='To'+str(n1)
		namt='Amount'+str(n1)
		ntsk='Task'+str(n1)
		p[nfro]=ac
		p[nto]=ac2
		p[namt]=amt
		p[ntsk]='Credited'
		trans[ac2].update(p)
	p['From']=ac
	p['To']=ac2
	p['Amount']=amt
	if len(trans[ac])==0:
		x[ac]={}
		x[ac]=p.copy()
		x[ac]['Task']='Debited'
		x[ac]['not']=0
		trans.update(x)
	if len(trans[ac2])==0:
		p['not']=0
		x[ac2]={}
		x[ac2]=p.copy()
		x[ac2]['Task']='Credited'
		x[ac2]['not']=0
		trans.update(x)
def transactiondetails(d,u,l,trans):
	ac=d[u][l]['Account No']
	if len(trans[ac])==0:
		print('No transactions done yet')
	else:
		count,index=1,1
		print()
		print('TransNo\tFrom\tTo\tAmount\tTask')
		for j in trans[ac]:
			if j=='not':
				continue
			if count==1:
				print(index,end='\t')
			if count%5!=0:
				print(trans[ac][j],end='\t')
				count=count+1
			if count%5==0:
				index=index+1
				if index<=(trans[ac]['not']+1):
					count=count+1
					print()
					print(index,end='\t')