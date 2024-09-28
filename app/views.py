from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.utils import timezone


# Create your views here.
def index(request):
    # user =  request.session['user']

    return render (request, 'index.html')

def home(request):
    return render(request, "home.html")

def register(request):
    return render(request, 'register.html')

def register1(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password= request.POST['password']
        age = request.POST['age']
        phone =  request.POST['phone']
        file = request.FILES['file']
        profilename=file.name

        result =  UserModel.objects.filter(email=email).exists()
        if  not result:
            user = UserModel.objects.create(
                username=name , 
                email=email, 
                password=password,
                age=age,
                phone=phone,
                profile_picture=file,
                profilename=profilename

                )
            user.save()
            messages.success(request, 'your  account has been created successfully!')
            return redirect('login')
        messages.success(request, 'email is  already registered please login or try another one ')
        return redirect('register')
        
def login(request):
    return render(request, 'login.html')

def login1(request):
    if request.method == 'POST':
        email =  request.POST['email']
        password = request.POST['password']

        user = UserModel.objects.filter(email=email, password=password)
        data = [i.username for i in user]
        print(user[0])
        if user:
            request.session['email'] = email
            request.session['user'] = data[0]
            messages.success(request,'you are  successfully logged in')
            return redirect('home')
        else:
            messages.success(request,'username and password do not match')
            return redirect('login')
        

def logout(request):
    del request.session['email']
    messages.success(request,"logged out successfylly")
    return redirect( '/' )

def password(request):
    return render(request , "changepass.html")

def changepass(request):
    em = request.session['email']
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        if  email !=em :
            messages.error(request,'please enter your current email address to verify the changes')
            return redirect('password')
        else:
            data =  UserModel.objects.get(email=email)
            data.password=password
            data.save()
            return redirect('login')

def uploadquestion(request):
      data  = QuestionsModel.objects.all()
      return render(request, 'questions.html', {'data':data})


def question(request):
    # QuestionsModel.objects.all().delete()
    if request.method == 'POST':
        msg = request.POST['message']
        name = request.session['user']
        time = timezone.now()
        email = request.session['email']
        user = UserModel.objects.get(email=email)
        coins = user.coins
        if coins > 10:
            user.coins=coins-10
            user.save()
            qs = QuestionsModel.objects.create(name=name, question=msg, time=time, email=email)
            qs.save()
            data  = QuestionsModel.objects.all()
            return redirect('question')
        else:
            messages.success(request, "You don't have enough Coin to ask a question.")
            return redirect('question')
    data  = QuestionsModel.objects.all()
    return render(request, 'questions.html', {'data':data, 'message': messages})

def answers(request,id):
    # AnswersModel.objects.all().delete()
    dat = QuestionsModel.objects.filter(id=id)
    d=[i.email for i in dat]
    
    if request.method=='POST':
        msg=request.POST['message']
        name = request.session['user']
        time = timezone.now()
        email = request.session['email']
        user = UserModel.objects.get(email=email)
        coins = user.coins 
        # print("-----------------------------------------")
        # print(d[0],email)
        if  d[0] !=  email and coins > 10:   
            user.coins=coins-10
            user.save()
            qs = AnswersModel.objects.create(qid =id, name=name, answers=msg, time=time,email=email)
            qs.save()
            data = AnswersModel.objects.filter(qid=id)
            return redirect('answers', id)
        else:
            messages.success(request, 'you don`t have enough Coins! or  you can`t answer this question.')
            return redirect('answers', id)
  
    data = AnswersModel.objects.filter(qid=id)
    
    
    return render (request,'answers.html',{'data':data, 'id':id , 'dat' : dat})


def points(request,qid,email):
    data = QuestionsModel.objects.filter(id=qid)
    d = [i.email for i in  data]
    ses = request.session['email'] 
    if ses == d[0]:
        user = UserModel.objects.get(email=email)
        user.coins += 100
        user.save()
        return redirect('question')
    else:
        messages.success(request, 'you  are not the owner of this question!')
        return redirect('answers', qid)
    
def profile(request):
    ses = request.session['email']
    data = UserModel.objects.filter(email=ses)
    question =  QuestionsModel.objects.filter(email=ses)
    if  not question:
        return render(request, 'profile.html', {'data':data,})

    return render(request, 'profile.html', {'data':data, 'question':question })

def follow(request,id,email):
    # FollowModel.objects.all().delete()
    ses = request.session['email']
    data = UserModel.objects.get(email=email)
    fol =  FollowModel.objects.filter(userid=id, email=ses)
    print(fol)
    if  not fol:
        follow = FollowModel.objects.create(
            userid = id,
            email = ses ,
            follow = 1
        )
        follow.save()
        # dat = QuestionsModel.objects.get(id=id)
        
        fcount =  FollowModel.objects.filter(userid=id).count()
        data.followers = fcount
        data.save()
        messages.success(request, f'now  you are following {data.username}!')
        return redirect('question')
        

        # f = [(i.userid, i.email) for i in fol]
        # print(f)
    
        # if  f[0][0] == id and  f[0][1]== ses:       
    else:
        messages.success(request,f"You are already following this {data.username}")
        return redirect('question')

        
def editprofile(request):
    ses = request.session['email']
    user = UserModel.objects.get(email=ses)
    if request.method=="POST":
        username = request.POST["name"]
        age = request.POST["age"]
        phone =  request.POST["phone"]
        file  = request.FILES["file"]
        pname = file.name

        user.username=username
        user.age=age
        user.phone=phone
        user.profile_picture=file
        user.profilename=pname
        user.save()
    return redirect('profile')

def updateprofile(request):
    return  render(request,'updateprofile.html')

