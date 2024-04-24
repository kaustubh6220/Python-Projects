from django.shortcuts import render
from .decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
import mysql.connector as sql
import csv
import pandas as pd



# Create your views here.
# views.py

def usertype(request):
    return render(request,'usertype.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login URL or view
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admindashboard')  # Replace 'dashboard' with the name of your dashboard URL
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'adminlogin.html', {'form': form})


def studentlogin(request):
    return render(request,'adminlogin.html')

def logout_view(request):
    logout(request)
    return redirect('/')  # Replace 'login' with the name of your login URL



@login_required
def admindashboard_view(request):
    return render(request,'admindashboard.html')



@login_required
def catagory(request):
    return render(request,'catagory.html')



@login_required
def studentdata(request):
    return render(request,'studentdata.html')



@login_required
def halldata(request):
    
     # Replace the following with your actual database connection details
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "web",
    }

    # Connect to the database
    conn = sql.connect(**db_config)
    cursor = conn.cursor()

    semihall_query = "SELECT Block,Hall,Number_of_seats,NoOfRows,NoOfColumn FROM semihall;"
    cursor.execute(semihall_query)

    # Fetch all rows from the result
    semihalldetails = cursor.fetchall()

    # Print the fetched data (for debugging purposes)
    print(semihalldetails)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Pass the fetched data to the template for rendering
    return render(request, 'halldata.html', {'halldetails': semihalldetails})



@login_required
def stusemI(request):
    # Replace the following with your actual database connection details
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "web",
    }

    # Connect to the database
    conn = sql.connect(**db_config)
    cursor = conn.cursor()

    semistudent_query = "SELECT Branch, Year, Specialization, Rollno, Enrollmentno, Name, SrNo FROM semistudent;"
    cursor.execute(semistudent_query)

    # Fetch all rows from the result
    semistu = cursor.fetchall()

    # Print the fetched data (for debugging purposes)
    print(semistu)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Pass the fetched data to the template for rendering
    return render(request, 'stusemI.html', {'semistudent': semistu})




@login_required
def stusemII(request):
    return render(request,'stusemII.html')



@login_required
def stusemIII(request):
    return render(request,'stusemIII.html')

@login_required
def stusemIV(request):
    return render(request,'stusemIV.html')



@login_required
def stusemV(request):
    return render(request,'stusemV.html')

@login_required
def stusemVI(request):
    return render(request,'stusemVI.html')



@login_required
def stusemVII(request):
    return render(request,'stusemVII.html')



@login_required
def stusemVIII(request):
    return render(request,'stusemVIII.html')



def semIstudata(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        message = ""

        if file.name.endswith('.csv'):
            try:
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='web'
                )
                cursor = conn.cursor()

                csv_data = pd.read_csv(file)

                all_values = []
                duplicate_entries = []
                for index, row in csv_data.iterrows():
                    value = (row['SrNo'],row['Branch'], row['Year'], row['Specialization'], row['RollNo'], row['EnrollmentNo'], row['Name'])
                    
                    # Check for duplicates
                    check_query = "SELECT * FROM semistudent WHERE Rollno = %s AND Name = %s"
                    cursor.execute(check_query, (row['RollNo'], row['Name']))
                    result = cursor.fetchall()
                    if result:
                        duplicate_entries.append(str(row['RollNo']) + ' - ' + row['Name'])
                    else:
                        all_values.append(value)

                # Insert valid entries
                if all_values:
                    query = "INSERT INTO semistudent (SrNo,Branch, Year, Specialization, Rollno, Enrollmentno, Name) VALUES (%s,%s, %s, %s, %s, %s, %s)"
                    cursor.executemany(query, all_values)
                    conn.commit()

                cursor.close()
                conn.close()

                if duplicate_entries:
                    message = "Duplicate entries found for the following Rollno and Name:"
                    message += "".join(duplicate_entries)
                    rollno_name_list = []
                elif all_values:
                    message = "Data inserted successfully!"
                    rollno_name_list = [(row['RollNo'], row['Name']) for index, row in csv_data.iterrows()]
                else:
                    message = "No valid data to insert."
                    rollno_name_list = []


            except csv.Error as e:
                print("Error while connecting to MySQL", e)
                message = "An error occurred during data insertion."

        else:
            message = "Invalid file format. Please upload a CSV file."

        # Pass the message to the template and render it
        return render(request, 'stusemI.html', {'message': message, 'rollno_name_list': rollno_name_list})

    return render(request, 'stusemI.html')



def deletesemIstu(request):
    
    conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='web'
                )
    cursor = conn.cursor()
    studeletquery='TRUNCATE TABLE semistudent;'
    cursor.execute(studeletquery)
    return render(request,'stusemI.html')

# def semIstudent(request):
    conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='admin'
                )
    cursor = conn.cursor()
    semistudent="SELECT Branch, Year, Specialization, Rollno, Enrollmentno, Name FROM semivstudent "
    cursor.execute(semistudent)
    semistudent=cursor.fetchall()
    print(semistudent)
    conn.commit()


    

    print(semistudent)
    
        # return render(request, 'semIhallreport.html',{'header_details':additional_details})


    return render(request, 'stusemI.html', {'semistudent': semistudent})



def uploadhalldata(request):
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        message = ""

        if file.name.endswith('.csv'):
            try:
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='web'
                )
                cursor = conn.cursor()

                csv_data = pd.read_csv(file)

                all_hall_values = []
                all_seat_values = []
                duplicate_entries = []
               
                for index, row in csv_data.iterrows():
                    block = row['Block']
                    hall = row['Hall']
                    number_of_seats = row['Number of Seats']
                    rows=row['Rows']
                    column=row['Columns']

                    # Check for duplicates
                    check_query = "SELECT * FROM semihall WHERE Block = %s AND Hall = %s"
                    cursor.execute(check_query, (block, hall))
                    result = cursor.fetchone()
                    if result:
                        duplicate_entries.append(block + ' - ' +str(hall))
                    else:
                        # Insert into semihall table
                        hall_values = (index + 1, block, hall, number_of_seats,rows,column)
                        all_hall_values.append(hall_values)

                        # Generate seat numbers from 1 to number_of_seats
                        seat_numbers=[]

                        seat_numbers = [(i+1) for i in range(number_of_seats)]
                        print(seat_numbers)
                        
                        
                        seat_values=[]
                        for seat in seat_numbers:
                            cursor.execute("SELECT MAX(SrNo) FROM semiseat")
                            max_srno = cursor.fetchone()[0]
                            if max_srno==None:
                                SrNo=1
                                print("Max SrNo:", max_srno)
                                
                                SrNo_values=(SrNo,block,hall,seat)
                                seat_query = "INSERT INTO semiseat (SrNo, Block, Hall, SeatNumber) VALUES (%s, %s, %s, %s)"
                                cursor.execute(seat_query, SrNo_values)
                                conn.commit()
                                
                            else:
                                print("Max SRNO :",max)
                                SrNo=max_srno+1
                                SrNo_values=(SrNo,block,hall,seat)
                                seat_query = "INSERT INTO semiseat (SrNo, Block, Hall, SeatNumber) VALUES (%s, %s, %s, %s)"
                                cursor.execute(seat_query, SrNo_values)
                                conn.commit()
                                seat_values.extend(SrNo_values)

                           

                        all_seat_values.extend(seat_values)
                        print(all_seat_values)

                     
                        

                # Insert valid entries into semihall table
                if all_hall_values:
                    hall_query = "INSERT INTO semihall (SrNo, Block, Hall, Number_of_seats, NoOfRows, NoOfColumn) VALUES (%s, %s, %s, %s, %s, %s)"
                    cursor.executemany(hall_query, all_hall_values)
                    conn.commit()

             

                cursor.close()
                conn.close()

                if duplicate_entries:
                    message = "Duplicate entries found for the following Block and Hall:"
                    message += "".join(duplicate_entries)
                    rollno_name_list = []

                elif all_hall_values:
                    message = "Data inserted successfully!"
                    rollno_name_list = [(row['Block'], row['Hall'])for index, row in csv_data.iterrows()]
                else:
                    message = "No valid data to insert."
                    rollno_name_list = []

            except csv.Error as e:
                print("Error while connecting to MySQL", e)
                message = "An error occurred during data insertion."

        else:
            message = "Invalid file format. Please upload a CSV file."

        # Pass the message to the template and render it
        return render(request, 'halldata.html', {'message': message, 'rollno_name_list': rollno_name_list})

    return render(request, 'halldata.html')



def deletehall(request):
    
    conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='web'
                )
    cursor = conn.cursor()
    halldeletquery='TRUNCATE TABLE semihall;'
    cursor.execute(halldeletquery)
    seatdeletquery='TRUNCATE TABLE semiseat;'    
    cursor.execute(seatdeletquery)

    return render(request,'halldata.html')


def hallreport(request):
    return render(request,'hallreport.html')


def semIhallreport(request):
    return render(request,'semIhallreport.html')


def semIhallreport(request):
    conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='web'
                )
    cursor = conn.cursor()
    hallquery="SELECT stu.Branch, stu.Year, stu.Specialization, stu.Rollno, seat.Block, seat.Hall, seat.SrNo, seat.SeatNumber, stu.Enrollmentno, stu.Name FROM semistudent stu JOIN semiseat seat ON stu.SrNo = seat.SrNo"
    cursor.execute(hallquery)
    hall_report=cursor.fetchall()
    print(hall_report)
    conn.commit()


    extracted_srnos = []
    for item in hall_report:
        value_4 = item[4]  # Value at index 4
        value_5 = item[5]  # Value at index 5
        
        # Search the values in MySQL table and extract srno
        query = "SELECT srno FROM semihall WHERE Block = %s AND Hall = %s"
        cursor.execute(query, (value_4, value_5))
        result = cursor.fetchone()
        if result:
            extracted_srnos.append(result[0])  # Append srno to the list
    
    

    cursor.close()
    conn.close()

    data_with_hallno = [(srno,) + item for srno, item in zip(extracted_srnos, hall_report)]

    print(data_with_hallno)
    if request.method=="POST":
        exam_month=request.POST.get('month')
        exam_year=request.POST.get('year')
        academic_year=request.POST.get('academicYear')
        program=request.POST.get('program')
        datefrom=request.POST.get('dateFrom')
        dateto=request.POST.get('dateTo')
        timefrom=request.POST.get('timeFrom')
        timeto=request.POST.get('timeTo')
        additional_details=[(exam_month,exam_year,academic_year,program,datefrom,dateto,timefrom,timeto)]
        print(additional_details)

        # return render(request, 'semIhallreport.html',{'header_details':additional_details})


    return render(request, 'semIhallreport.html', {'hall_report': data_with_hallno, 'header_details':additional_details})

def I_additional(request):
    return render(request,'I_additional.html')

from django.shortcuts import render
from django.db import connection

# def hall_view(request):
    
#     with connection.cursor() as cursor:
#         # Execute a raw SQL query to fetch the data
#         cursor.execute("SELECT Hall, Number_of_seats, NoOfRows, NoOfColumn FROM semihall;")
#         halls_data = cursor.fetchall()

#     halls = [{'Hall': hall, 'Number_of_seats': seats, 'NoOfRows': rows, 'NoOfColumn': columns} for hall, seats, rows, columns in halls_data]
#     print(halls_data)
#     return render(request, 'hall_view.html', {'halls': halls})
