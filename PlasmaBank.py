import subprocess as sp
import pymysql
import pymysql.cursors
from getpass import getpass
from datetime import datetime
from datetime import date


def UpdateBloodCost():
	var0 = input("Enter Plasma_bag_number whose cost is to be Updated: ")
	bloodId = int(var0)
	var1 = input("Enter updated cost: ")
	new_cost = int(var1)
	query0 = "Select count(*) AS cnt from BLOOD where Plasma_bag_number = %d" %(bloodId)    
	query_duty = "UPDATE BLOOD_COST SET cost =  %d where plasma_bag_number = %d" % ( new_cost,bloodId)

	try:
		executeQuery(query0)
		val = cur.fetchall()
		val = val[0]
		val = val['cnt']
		if(val == 0) :
			print("Input plasma_bag_number does not exist. Please enter valid input")
			return
		executeQuery(query_duty)
		print("Blood cost updated sucessfully")
	except Exception as e:
		excepting(e)

	return

def executeQuery(query):
	cur.execute(query)
	con.commit()

def deleteBlood():
	var0 = input("Enter Plasma bag number to be deleted: ")
	delete_id = int(var0)
	query0 = "Select count(*) AS cnt from BLOOD where plasma_bag_number = %d" %(delete_id)
	query1 = "DELETE FROM BLOOD where plasma_bag_number = %d" % (delete_id)

	try:
		cur.execute(query0)
		val = cur.fetchall()
		val = val[0]
		val = val['cnt']
		if(val != 0 ):
			executeQuery(query1)
			print("Deleted successfully")
		else:
			print("Input plasma_bag_number does not exist.Please enter a valid plasma_bag_number")
			return

	except Exception as e:
		excepting(e)
	return    


def addBlood():
	try:
		# Takes emplyee details as input
		row = {}
		print("Enter new Plasma details: ")
		var0 = input("plasma_bag_number: ")
		row["plasma_bag_number"] = int(var0)
		row["blood_type"] = input("Plasma blood_type: ")
		var1 = input("blood_amount: ")
		row["blood_amount"] = int(var1)
		var2 = input("platelets_count (in thousands): ")
		row["platelets_count"] = float(var2)
		query = "INSERT INTO BLOOD(plasma_bag_number,blood_type,blood_amount,platelets_count) VALUES('%d', '%s', '%d', '%0.1f')" %(row["plasma_bag_number"],row["blood_type"], row["blood_amount"], row["platelets_count"])
		executeQuery(query)
		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return

def addPaymentTnx():
	try:
		row = {}
		print("Enter transaction details: ")
		var0 = input("rec_id: ")
		row["rec_id"] = int(var0)
		var1 = input("Payment Amount: ")
		row["payment_amt"] = int(var1)
		timenow = datetime.now()
		current_time = timenow.strftime("%d/%m/%Y %H:%M:%S")
		print("Time of Txn =", current_time)
		row["payment_time"] = current_time
		query = "INSERT INTO PAYMENT_TRANSACTION(rec_id,payment_amt,payment_time) VALUES('%d', %d', '%s')" %(row["rec_id"],row["payment_amt"], row["payment_time"])
		executeQuery(query)
		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return

def addDonorInfo():
	try:
		row = {}
		print("Enter new donor's details: ")
		rawname = input("Name (Fname Lname): ")
		name = (rawname).split(' ')
		row["fname"] = name[0]
		row["lname"] = name[1]
		var0 = input("Donor_id: ")
		row["donor_id"] = int(var0)
		row["blood_type"]=input("Plasma Blood_type: ")
		dob = (input("DOB (YYYY-MM-DD): ")).split('-')
		row["dOB"] = dob[0]+'-'+dob[1]+'-'+dob[2]
		print("Age:", calculateAge(date(int(dob[0]), int(dob[1]), int(dob[2]))), "years")
		row["age"] = calculateAge(date(int(dob[0]), int(dob[1]), int(dob[2])))
		row["sex"] = input("Sex: ")
		var3 = input("phone_no: ")
		row["phone_no"] = var3
		var7 = input("Address: ")
		row["address"] = var7

		query = "INSERT INTO DONOR_INFO(donor_id,blood_type,phone_no,dOB,age,sex,fname,lname,address) VALUES('%d', '%s', '%s','%s','%d','%s','%s','%s','%s')" %(row["donor_id"], row["blood_type"], row["phone_no"], row["dOB"], row["age"],row["sex"],row["fname"],row["lname"],row["address"])
		executeQuery(query)

		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return

def addRecipient():
	try:
		row = {}
		print("Enter new recipient's details: ")
		rawname = input("Name (Fname Lname): ")
		name = (rawname).split(' ')
		row["fname"] = name[0]
		row["lname"] = name[1]
		var3 = input("Rec_id: ")
		row["rec_id"] = int(var3)
		row["blood_type"]=input("Plasma Blood_type: ")
		var0 = input("Quantity_needed: ")
		row["quantity_needed"] = int(var0)
		row["date_of_request"] = input("Date of request (YYYY-MM-DD): ")
		dob = (input("DOB (YYYY-MM-DD): ")).split('-')
		row["dOB"] = dob[0]+'-'+dob[1]+'-'+dob[2]
		print("Age:", calculateAge(date(int(dob[0]), int(dob[1]), int(dob[2]))), "years")
		row["age"] = calculateAge(date(int(dob[0]), int(dob[1]), int(dob[2])))
		row["sex"] = input("Sex: ")
		var5 = input("Address: ")
		row["address"] = var5
		query = "INSERT INTO RECIPIENT(rec_id,blood_type,quantity_needed,date_of_request,fname,lname,dOB,sex,age,address) VALUES('%d', '%s', '%d','%s','%s','%s','%s','%s','%d','%s')" %(row["rec_id"], row["blood_type"], row["quantity_needed"], row["date_of_request"],row["fname"],row["lname"],row["dOB"],row["sex"],row["age"],row["address"])
		executeQuery(query)

		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return


def addDonor():
	try :
		row={}
		print("Enter new donation details: ")
		var0 = input("Donor-id: ")
		row["donor_id"] = int(var0)
		row["date_of_donation"] = input("Date of donation (YYYY-MM-DD): ")
		query = "INSERT INTO DONORS(donor_id,date_of_donation) VALUES('%d', '%s')" %(row["donor_id"],row["date_of_donation"])
		print(query)
		executeQuery(query)

		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return

def Supervisors():
	try :
		a = input("Enter supervisor name: ")
		query = "select * FROM STAFF where supervisor='%s'" % (a)
		executeQuery(query)
		row = cur.fetchall()
		print("Employees under Supervisor", a, "are:" )
		print(row)
	except Exception as e:
		excepting(e)
		
	return         

def hireStaff():
	try:
		# Takes emplyee details as input
		row = {}
		print("Enter new staff member's details: ")
		row["fname"] = input("Name: ")
		var0 = input("emp_id: ")
		row["emp_id"] = int(var0)
		row["supervisor"] = input("supervisor: ")
		row["address1"] = input("address: ")
		var1 = input("salary: ")
		row["salary"] = int(var1)
		var2 = input("phone_no: ")
		row["phone_no"] = int(var2)
		query = "INSERT INTO STAFF(emp_id,fname,supervisor, address1,phone_no,salary) VALUES('%d', '%s', '%s', '%s', '%d', '%d')" %(row["emp_id"],row["fname"],row["supervisor"], row["address1"], row["phone_no"], row["salary"])
		executeQuery(query)
		print("Inserted Into Database")

	except Exception as e:
		excepting(e)
		
	return

def TotalBlood():
	try :
		query = "select SUM(blood_amount) total FROM BLOOD"
		executeQuery(query)
		row = cur.fetchall()
		print("The total Plasma available is :")
		print(row)
	except Exception as e:
		excepting(e)
		
	return

def TotalBloodOfGiven():
	try :
		a = input("Enter the Plasma type: ")
		query = "select SUM(blood_amount) FROM BLOOD where blood_type='%s'" % (a)
		executeQuery(query)
		row = cur.fetchall()
		print("The total available Plasma of type", a, "is:" )
		print(row)
	except Exception as e:
		excepting(e)
		
	return     

def ViewBlood():
	try :
		query = "select * FROM BLOOD"
		executeQuery(query)
		row = cur.fetchall()
		print(row)
	except Exception as e:
		excepting(e)

	return

def AddBloodCost():
	try :
		row={}
		print("Enter following details: ")
		var0 = input("Plasma bag number: ")
		row["plasma_bag_number"] = int(var0)
		row["cost"] = int(input("Plasma Cost: "))
		query = "INSERT INTO BLOOD_COST(plasma_bag_number,cost) VALUES('%d', '%d')" %(row["plasma_bag_number"],row["cost"])
		executeQuery(query)
		print("Inserted Into Database")

	except Exception as e:
		excepting(e)

	return

def excepting(e):
	con.rollback()
	print("Failed to insert/delete/update/find database")
	print (">>>>>>>>>>>>>", e)
	return

def calculateAge(birthDate): 
	days_in_year = 365.2425    
	age = int((date.today() - birthDate).days / days_in_year) 
	return age

def dispatch(ch):

	if(ch==1): 
		addDonor()
	if(ch==2):
		addDonorInfo()
	if(ch==3):
		addBlood()
	if(ch==4):
		addRecipient()
	if(ch==5):
		hireStaff()
	if(ch == 6):
		deleteBlood()
	if(ch == 7):
		UpdateBloodCost()
	if(ch ==8):
		TotalBlood()
	if(ch==9):
		TotalBloodOfGiven()
	if(ch ==10):
		ViewBlood()
	if(ch == 11):
		AddBloodCost()
	if(ch == 12):
		Supervisors()   
	if(ch == 13):
		addPaymentTnx()  
	if(ch > 14):
		print("Error: Invalid Option")

# Global
while(1):
	tmp = sp.call('clear',shell=True)
	user = input("Username: ")
	password = getpass("Password: ")

	try:
		con = pymysql.connect(host='localhost',
				user=user,
				password=password,
				database='PLASMABANK',
				cursorclass=pymysql.cursors.DictCursor)
		tmp = sp.call('clear', shell=True)

		if(con.open):
			print("Connected")
		else:
			print("Failed to connect")

		tmp = input("Enter any key to CONTINUE>")

		with con.cursor() as cur:
			while(1):
				tmp = sp.call('clear', shell=True)
				print("1. Add new Plasma donation")
				print("2. Add new donor information")
				print("3. Add new Plasma")
				print("4. Add new recipient")
				print("5. Hire a new employee")
				print("6. Delete a Plasma sample")
				print("7. Change Plasma Cost")
				print("8. Total Plasma Donated")
				print("9. Total Plasma of given type Donated")
				print("10. View Plasma")
				print("11. Add Plasma cost")
				print("12. Supervisor List")
				print("13. Add Transaction Details")
				print("14. Logout")
				ch = int(input("Enter choice> "))
				tmp = sp.call('clear', shell=True)
				if ch != 14:
					dispatch(ch)
					tmp = input("Enter any key to CONTINUE>")
				elif ch == 14:
					break


	except:
		tmp = sp.call('clear', shell=True)
		print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
		tmp = input("Enter any key to CONTINUE>")
