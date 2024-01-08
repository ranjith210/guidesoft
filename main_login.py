from ast import literal_eval 				# literal_eval() converts string to a literal 
import user_login_module as m1
import emp_login_module as m2
import user_regr_module as m3			
f=open('data.txt','r')		# opening a file in read mode.
data,acnodict,trans,con,l3=literal_eval(f.readline()),literal_eval(f.readline()),literal_eval(f.readline()),literal_eval(f.readline()),literal_eval(f.readline())

# data ,acnodict, trans, con are "dictonaries". l3 is a list containing all account numbers. All are empty.
# In data dictionary, key=user_id and value = {passwd : user_details}. 

# acnodict is account number dictionary; key = acc_no and value = user details

# trans is a transaction dictionary; key = acc_no and value={transaction details}

# con is a dictionary; key=acc_no and value={user_id:password}
while 1:
	print("************************\n	WELCOME\n************************")
	choice=int(input('(1) User Login\n(2) Employee Login\n(3) Bank Account Registration Form\n(4) Exit\nEnter your choice: '))
	if(choice==1):
		trans=m1.userlogin(data,acnodict,trans,con)  
		print('________________________________\n')
	if(choice==2):
		m2.employeelogin(acnodict,trans)
		print('________________________________\n')
	if(choice==3):
		data,acnodict,con=m3.details(data,acnodict,con,trans,l3)
		print('________________________________\n')
	if(choice==4):
		f1=open('data.txt','w')
		f1.write(f"{data}\n{acnodict}\n{trans}\n{con}\n{l3}")
		exit()