#inputs
name = input("Enter your name : ")
sid = int(input("Enter your SID : "))
dept_name = input("Enter the name of your department : ").upper()
cgpa=float(input("Enter your CGPA : "))
#output
print("\nHey, \033[1m%s\033[0m Here!\nMy SID is \033[1m%d\033[0m\nI am from \033[1m%s\033[0m department and my CGPA is \033[1m%0.1f\033[0m\n" % (name, sid, dept_name, cgpa))