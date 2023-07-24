from django.shortcuts import render,HttpResponse,redirect
from message_app.models import Msg

# Create your views here.
def create(request):
    if request.method=='GET':
        print("request is:",request.method)
        return render(request,"create.html")
    else:
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        print("name:",n)
        print("Email:",mail)
        print("name:",mob)
        print("name:",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)  #to insert   data using ORM querry
        m.save()
       # return HttpResponse("Data entered sucessfully")
        return redirect('/dashboard')
   
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    #return HttpResponse("Data FETCHED From Database Table")
    return render(request,'dashboard.html',context)


#print("data deleted",rid)
    #return HttpResponse("Deleted data in id"+rid)
    #fetch data using filter() method:
    # var=model_name.objects.filter(col_name=value)
     #delete record using delete() method:
    #objectname.delete()
     #redirect helps to redirect to the link
def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/dashboard')


#print("Id to be edited",rid)
   # return HttpResponse("Record to be edited"+rid)
   #when we see the form the URL will receive the GET method
   # we need to edit the data in the form so we use dictonary to get values.
    #as the value fetched in the form of dictonary 
        #we need to render it using dictionary name
def edit(request,rid):
    if request.method=='GET':
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)  
    else:
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mobile']
        umsg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)
        return redirect('/dashboard')
        #print("name:",un)
        #print("Email:",umail)
        #print("name:",umob)
        #print("name:",umsg)
       # return HttpResponse("record updated")