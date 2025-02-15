from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.apps import apps
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django import forms
from .forms import *
from django.db.models import Max
import json
#index page
def index(request):
    request.session['tupdate']=False
    return render(request, 'index.html')

#customer signup page
def signup(request):
    user_name = request.session.get('user_name')
    request.session['update']=False
    if user_name:
        return redirect('home')
    else:
        return render(request, 'signup.html',{'error':request.session.get('error_message'),'email':request.session.get('email_exist')})
    

#customer add
def register(request):
    if(request.method=='POST'):
        username=request.POST['signEmail']
        password=request.POST['signPass1']
        name=request.POST['signName']
        mobile=request.POST['signMobile']
        hashed_password = make_password(password)
        user = customer.objects.filter(email=username).first()
        if user:
            request.session['email_exist'] = True
            return redirect('signup') 
        else:
            data=customer(name=name,mobile=mobile,email=username,password=hashed_password)
            data.save()
            request.session['user_name'] = name
            request.session['user_mail'] = username
            request.session['email_exist'] = False
            return redirect('home')
        
    else:
        return redirect('signup') 

#customer login
def login(request):
    if request.method=='POST':
        username=request.POST['loginEmail']
        password=request.POST['loginPass']
        
        user = customer.objects.filter(email=username).first()
        if user:
            if check_password(password, user.password):
                request.session['user_name'] = user.name
                request.session['user_mail'] = username
                request.session['error_message'] = False
                request.session['email_exist'] = False
                return redirect('home')  # Redirect to dashboard 
            else:
                request.session['error_message'] = True
                return redirect('signup')
        else:
            request.session['error_message'] = True
            return redirect('signup')
    else:
        return redirect('signup')

#customer forgot password page
def forgotPage(request):
    return render(request, 'forget.html', {'retrive': request.session.get('retrive'), 'email':request.session.get('pass_email'), 'error':request.session.get('passup_error'), 'update':request.session.get('update')})

#customer forgot password
def forgotPassword(request):
    if request.method=='POST':
        mobile=request.POST['mobile']
        email=request.POST['email']
        data=customer.objects.filter(mobile=mobile,email=email).first()
        if data:
            request.session['retrive']=True
            request.session['pass_email']=email
            return redirect('forgotPage')
        else:
            request.session['passup_error']=True
            return redirect('forgotPage')
        
#customer update forget password
def uppassword(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        data=customer.objects.filter(email=email).first()
        if data:
            data.password=make_password(password)
            data.save()
            request.session['retrive']=False
            request.session['pass_email']=False
            request.session['passup_error']=False
            request.session['update']=True
            return redirect('forgotPage')


#customer logout
def logout(request):
    request.session['user_name']=False
    request.session['tuser_name']=False
    request.session['auser_name']=False
    request.session['user_email']=False
    request.session['tuser_email']=False
    return redirect('index')

#customer home page
def home(request):
    user_name = request.session.get('user_name')
    if user_name:
        return render(request, 'home.html', {'user_name': user_name})
    else:
        return redirect('index')

#customer contact page
def contact(request):
    user_name = request.session.get('user_name')
    if user_name:
        return render(request, 'contact.html', {'user_name': user_name})
    else:
        return redirect('index')

#customer about page
def about(request):
    user_name = request.session.get('user_name')
    if user_name:
        return render(request, 'about.html', {'user_name': user_name})
    else:
        return redirect('index')

#customer bookings page
def bookings(request):
    user_name = request.session.get('user_name')
    if user_name:
        user=customer.objects.filter(email=request.session.get('user_mail')).first()
        active=Booking.objects.filter(cid_id=user.cid,status__iexact='active').values()
        inactive=Booking.objects.filter(cid_id=user.cid,status__iexact='inactive')
        guide=TourGuide.objects.all().values()

        return render(request, 'bookings.html', {'user_name': user_name, 'active':active, 'guide':guide, 'inactive': inactive})
        
    else:
        return redirect('index')

#customer cancel booking
def cacelBook(request):
    user_name = request.session.get('user_name')
    if user_name:
        book=Booking.objects.filter(bid=request.GET.get('bid')).first()
        tid=book.tid_id
        book.status='inactive'
        book.save()
        data=TourGuide.objects.filter(tid=tid).first()
        data.status='active'
        data.save()
        return redirect('bookings')
    else:
        return redirect('index')

#give rating to guide
def rate(request):
    if request.method=='POST':
        id=request.POST['id']
        comment=request.POST['comment']
        rating=request.POST['rating']
        feedback=Booking.objects.filter(bid=id).first()
        guideid=feedback.tid_id
        feedback.rating=rating
        feedback.comment=comment
        feedback.feedback='inactive'
        feedback.save()
        cal=Booking.objects.filter(tid=guideid)
        print(cal)
        sum,no=0,0
        for i in cal:
            sum+=i.rating
            no+=1
        total=sum/no
        from .models import TourGuide
        submit=TourGuide.objects.filter(tid=guideid).first()
        submit.rating=total
        submit.save()

        return redirect('bookings') 
    else:
        return redirect('index')

#customer profile
def profile(request):
    user_name = request.session.get('user_name')
    if user_name:
        from .models import customer
        cust=customer.objects.filter(email=request.session.get('user_mail')).first()
        return render(request, 'profile.html', {'user_name': user_name, 'customer':cust})
    else:
        return redirect('index')

#update profile
def cutomerProfile(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        print(username)
        from .models import customer
        user = customer.objects.filter(email=request.session.get('user_mail')).first()
        if user:
            user.name = username
            user.mobile = mobile
            user.email = email
            user.save()

            request.session['user_name'] = username
            request.session['user_mail'] = email
            return redirect('profile')  
        else:
            return redirect('profile')            
    else:
        return redirect('signup')

#update customer password
def updatePassword(request):
    if request.method=='POST':
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        from .models import customer
        user = customer.objects.filter(email=request.session.get('user_mail')).first()
        if user:
            if check_password(password1, user.password):
                user.password=make_password(password2)
                user.save()
            return redirect('profile')  
        else:
            return redirect('profile')            

    else:
        return redirect('signup')

#show restaurant customer
def restaurant(request):
    user_name = request.session.get('user_name')
    if user_name:
        request.session['city'] = request.GET.get('city')
        request.session['type'] = 'restaurant'
        from .models import restaurant
        restaurants = restaurant.objects.filter(city__iexact=request.session.get('city'))
        return render(request, 'restaurant.html', {'user_name': user_name,'data': restaurants, 'error': request.session.get('search_error')})
    else:
        return redirect('index')

#show hotel customer
def hotel(request):
    user_name = request.session.get('user_name')
    if user_name:
        request.session['city'] = request.GET.get('city')
        request.session['type'] = 'hotel'
        from .models import hotel
        hotel = hotel.objects.filter(city__iexact=request.session.get('city'))
        
        return render(request, 'hotel.html', {'user_name': user_name,'data': hotel, 'error': request.session.get('search_error')})
    else:
        return redirect('index')

#show places customer
def place(request):
    user_name = request.session.get('user_name')
    if user_name:
        request.session['city'] = request.GET.get('city')
        request.session['type'] = 'place'
        from .models import place
        places = place.objects.filter(city__iexact=request.session.get('city'))
        
        return render(request, 'place.html', {'user_name': user_name,'data': places, 'error': request.session.get('search_error')})
    else:
        return redirect('index')
    
#search by customer
def search(request):
    user_name = request.session.get('user_name') 
    type_name = request.session.get('type')
    city = request.session.get('city')
    search = request.GET.get('search')
    location = type_name + '.html'

    #search by city
    list1=['mahabaleshwar','lonavala','shegaon','matheran','Mahabaleshwar','Lonavala','Shegaon','Matheran']
    if search in list1:
        request.session['search_error']= False
        return redirect('/'+type_name+'s/?city=' + search)
    # Get the model class dynamically
    typee = apps.get_model(app_label='tourguide', model_name=type_name)
    if typee:
        #search by area
        data = typee.objects.filter(city__iexact=city, area__icontains=search).values()
        if data:
            request.session['search_error']= False
            return render(request, location, {'user_name': user_name, 'data': data, 'error': request.session.get('search_error')})
            
        else:
            #search by name
            data = typee.objects.filter(city__iexact=city, name__icontains=search).values()
            if data:
                request.session['search_error']= False
                return render(request, location, {'user_name': user_name, 'data': data, 'error': request.session.get('search_error')})
            else:
                request.session['search_error']= True
                return render(request, location, {'user_name': user_name, 'data': data, 'error': request.session.get('search_error')})
    else:
        return HttpResponse("NO data")

#show details to customer
def details(request):
    user_name = request.session.get('user_name') 
    type_name = request.session.get('type')
    rid = request.GET.get('id')

    # Get the model class dynamically
    typee = apps.get_model(app_label='tourguide', model_name=type_name)
    if typee:
        data = typee.objects.filter(rid=rid).first()
        if data:
            area = data.area
            city = data.city

        # Retrieve nearby places excluding the current one
        nearby_places = typee.objects.filter(area=area, city=city).exclude(rid=rid).values()

        # Retrieve other places in the same city but different area
        other_places_same_city = typee.objects.filter(city=city).exclude(area=area).values()

        # Retrieve tour guides for the same city
        guides = TourGuide.objects.filter(city__iexact=city,status__iexact='active').values()

        if type_name=='place':
            return render(request, 'details.html', {'user_name': user_name, 'data': data,'type':type_name,'nearby':nearby_places, 'extra':other_places_same_city,'guide':guides, 'amenitites':False})
        elif type_name=='hotel':
            from .models import hotel
            count=0
            data=hotel.objects.filter(rid=rid).first()
            for key,values in data.amenities.items():
                if values:
                    count+=1
                    return render(request, 'details.html', {'user_name': user_name, 'data': data,'type':type_name,'nearby':nearby_places, 'extra':other_places_same_city,'guide':False, 'amenities':True})
            return render(request, 'details.html', {'user_name': user_name, 'data': data,'type':type_name,'nearby':nearby_places, 'extra':other_places_same_city,'guide':False, 'amenities':False})
        else:
            return render(request, 'details.html', {'user_name': user_name, 'data': data,'type':type_name,'nearby':nearby_places, 'extra':other_places_same_city,'guide':False, 'amenities':False})

    else:
        return HttpResponse("NO data")


#show other guide details to customer
def tdetails(request):
    user_name = request.session.get('user_name')
    tid = request.GET.get('id')
    # Get the model class dynamically
    if user_name:
        data = TourGuide.objects.filter(tid=tid).values()
        nearby = TourGuide.objects.all().exclude(tid=tid).values()
        nearby=nearby.exclude(status__iexact='inactive')
        if data:
            return render(request, 'tdetails.html', {'user_name': user_name, 'data': data,'nearby':nearby})
        else:
            return HttpResponse("NO data")
    else:
        return redirect('index')


#tourguide booking by customer
def tbook(request):
    user_name = request.session.get('user_name')
    if user_name:
        id=request.GET.get('id')
        user=customer.objects.filter(email=request.session.get('user_mail')).first()
        guide=TourGuide.objects.filter(tid=id).first()
        return render(request, 'tbooking.html', {'user_name': user_name, 'customer':user,'guide':guide})
    else:
        return redirect('index')

#confirm tourguide booking by payment
def pay(request):
    if request.method=='POST':
        venue=request.POST['venue']
        date=request.POST['date']
        time=request.POST['time']
        pickup=request.POST['pickup']
        price=request.POST['price']
        tid=request.POST['id']
        cid=request.POST['cid'] 

        tour_guide = TourGuide.objects.get(tid=tid)
        customer1 = customer.objects.get(cid=cid)

        book=Booking(tid=tour_guide, cid=customer1, pickup=pickup, venu=venue, date=date, time=time, price=price)
        book.save()

        tour_guide.status='inactive'
        tour_guide.save()

        return redirect('bookings')
    else:
        return redirect('index')  


#Tourguide signup page
def tsignup(request):
    request.session['tupdate']=False
    user_name = request.session.get('tuser_name')
    if user_name:
        return redirect('thome')
    else:
        return render(request, 'tsignup.html',{'error':request.session.get('error_message'),'email':request.session.get('email_exist')})

#Tourguide add
def tregister(request):
    if(request.method=='POST'):
        username=request.POST['signEmail']
        password=request.POST['signPass1']
        name=request.POST['signName']
        mobile=request.POST['signMobile']
        hashed_password = make_password(password)
        user = TourGuide.objects.filter(email=username).first()
        if user:
            request.session['email_exist'] = True
            return redirect('tsignup') 
        else:
            data=TourGuide(name=name,mobile=mobile,email=username,password=hashed_password)
            data.save()
            request.session['tuser_name'] = name
            request.session['tuser_mail'] = username
            request.session['email_exist'] = False
            return redirect('thome')
        
    else:
        return redirect('tsignup')  

#Tourguide login
def tlogin(request):
    if request.method=='POST':
        username=request.POST['loginEmail']
        password=request.POST['loginPass']
        
        user = TourGuide.objects.filter(email=username).first()
        if user:
            if check_password(password, user.password):
                request.session['tuser_name'] = user.name
                request.session['tuser_mail'] = username
                request.session['status'] = user.status
                request.session['error_message'] = False
                request.session['email_exist'] = False
                return redirect('thome')  # Redirect to dashboard 
            else:
                request.session['error_message'] = True
                return redirect('tsignup')
        else:
            request.session['error_message'] = True
            return redirect('tsignup')
    else:
        return redirect('tsignup')

#Tourguide forget password page
def tforget(request):
    return render(request, 'tforget.html', {'retrive': request.session.get('tretrive'), 'email':request.session.get('tpass_email'), 'error':request.session.get('tpassup_error'), 'update':request.session.get('tupdate')})

#Tourguide forget password
def tforgotPassword(request):
    if request.method=='POST':
        mobile=request.POST['mobile']
        email=request.POST['email']
        data=TourGuide.objects.filter(mobile=mobile,email=email).first()
        if data:
            request.session['tretrive']=True
            request.session['tpass_email']=email
            return redirect('tforget')
        else:
            request.session['tpassup_error']=True
            return redirect('tforget')

#Tourguide update forget password
def tuppassword(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
        data=TourGuide.objects.filter(email=email).first()
        if data:
            data.password=make_password(password)
            data.save()
            request.session['tretrive']=False
            request.session['tpass_email']=False
            request.session['tpassup_error']=False
            request.session['tupdate']=True
            return redirect('tforget')

#TourGuide Home Page
def thome(request):
    user_name = request.session.get('tuser_name')
    if user_name:
        tourguide=TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
        data=Booking.objects.filter(tid=tourguide.tid,status__iexact='active').first()
        inactive=Booking.objects.filter(tid_id=tourguide.tid,status__iexact='inactive')
        return render(request, 'thome.html', {'user_name': user_name, 'guide':tourguide, 'data':data, 'inactive':inactive })
    else:
        return redirect('index')

#TourGuide contact Page
def tcontact(request):
    user_name = request.session.get('tuser_name')
    if user_name:
        return render(request, 'tcontact.html', {'user_name': user_name})
    else:
        return redirect('index')

#TourGuide Profile
def tprofile(request):  
    user_name = request.session.get('tuser_name')
    if user_name:
        guide=TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
        return render(request, 'tprofile.html', {'user_name': user_name, 'guide':guide, 'error_message':request.session.get('error_message')})
    else:
        return redirect('index')


#update tourguide profile
def upTprofile(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        area=request.POST['area']
        city=request.POST['city']
        bio=request.POST['bio']
        languages=request.POST['languages']
        price=request.POST['price']
        experience=request.POST['experience']
        from .models import TourGuide
        user = TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
        if user:
            user.name = username
            user.mobile = mobile
            user.email = email
            user.area = area
            user.city = city
            user.languages=languages
            user.price=price
            user.bio = bio
            user.experience = experience
            user.save()
            
            request.session['tuser_name'] = username
            request.session['tuser_mail'] = email
            return redirect('tprofile')  
        else:
            return redirect('tprofile')            

    else:
        return redirect('index')

#update tourguide password
def upTpassword(request):
    if request.method=='POST':
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        from .models import customer
        user = TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
        if user:
            if check_password(password1, user.password):
                user.password=make_password(password2)
                user.save()
                request.session['error_message'] = False
            else:
                request.session['error_message'] = True
            return redirect('tprofile')  
        else:
            return redirect('tprofile')            

    else:
        return redirect('index')

#update photo of guide
def tphoto(request):
    if request.method=='POST':
        form = GuidePhoto(request.POST, request.FILES)
        if form.is_valid():
            guide = TourGuide.objects.get(email=request.session.get('tuser_mail'))
            guide.img = form.cleaned_data['img']
            guide.save()
        return redirect('tprofile') 

    else:
        return redirect('index')

#tourguide status update
def status(request):
    status1 = request.GET.get('status1')
    user = TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
    if user:
        user.status = status1
        user.save()
        request.session['status'] = status1  
        return redirect('thome')  
    else:
        return redirect('thome')   

#tourguide cancelling bookings
def bookStatus(request):
    user_name = request.session.get('tuser_name')
    if user_name:
        book=Booking.objects.filter(bid=request.GET.get('bid')).first()
        book.status='inactive'
        book.save()

        user = TourGuide.objects.filter(email=request.session.get('tuser_mail')).first()
        if user:
            user.status='active'
            user.save()

        return redirect('thome')
    else:
        return redirect('index')

#admin login
def alogins(request):
    user_name = request.session.get('auser_name')
    if user_name:
        return redirect('ahome')
    else:
        return render(request, 'alogin.html', { 'error':request.session.get('error_message')})

#admin signin
def asignin(request):
    name=request.POST['username']
    password=request.POST['password']
    user=admins.objects.filter(name=name,password=password).first()
    if user:
        request.session['error_message'] = False
        request.session['auser_name']=name
        return redirect('ahome')
    else:
        request.session['error_message'] = True
        return redirect('alogins')

#admin home
def ahome(request):
    user_name = request.session.get('auser_name')
    if user_name:
        return render(request, 'ahome.html', {'user_name': user_name})
    else:
        return redirect('index')


#admin hotel
def ahotel(request):
    user_name = request.session.get('auser_name')
    if user_name:
        from .models import hotel
        hotels = hotel.objects.all().values()
        return render(request, 'ahotel.html', {'user_name': user_name, 'hotel': hotels})
    
    else:
        return redirect('index')
    
#updtae hotel
def updateHotel(request):
    if request.method=='POST':
        hotel_name=request.POST['hotel_name']
        hotel_area=request.POST['hotel_area']
        hotel_city=request.POST['hotel_city']
        hotel_link=request.POST['hotel_link']
        hotel_description=request.POST['hotel_description']
        hid=request.POST['id']
        wifi='wifi' in request.POST
        swimming_pool='swimming_pool' in request.POST
        fitness_center='fitness_center' in request.POST
        spa='spa' in request.POST
        restaurant='restaurant' in request.POST
        bar='bar' in request.POST
        room_service='room_service' in request.POST
        parking='parking' in request.POST
        pet_friendly='pet_friendly' in request.POST
        ac='ac' in request.POST
        laundry='laundry' in request.POST
        tv='tv' in request.POST
        amenities= {
            "wifi": wifi,
            "swimming_pool": swimming_pool,
            "fitness_center": fitness_center,
            "spa": spa,
            "restaurant": restaurant,
            "bar": bar,
            "room_service": room_service,
            "parking": parking,
            "pet_friendly": pet_friendly,
            "ac": ac,
            "tv": tv,
            "laundry": laundry
        }

        from .models import hotel
        hotels=hotel.objects.filter(rid=hid).first()
        hotels.name=hotel_name
        hotels.city=hotel_city
        hotels.area=hotel_area
        hotels.location=hotel_link
        hotels.deacription=hotel_description
        hotels.amenities=amenities
        hotels.save()
        
        return redirect('ahotel')
        
    else:
        return redirect('index')    

#hotel photo update
def hotelPhoto(request):
    form = HotelPhoto(request.POST, request.FILES)
    from .models import hotel
    id=request.POST['id']
    if form.is_valid():
        hotel = hotel.objects.filter(rid=id).first()
        hotel.img = form.cleaned_data['img']
        hotel.save()
    return redirect('ahotel')

#add hotel
def addHotel(request):
    if request.method=='POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.img = request.FILES['img']
            form.save()
        wifi='wifi' in request.POST
        swimming_pool='swimming_pool' in request.POST
        fitness_center='fitness_center' in request.POST
        spa='spa' in request.POST
        restaurant='restaurant' in request.POST
        bar='bar' in request.POST
        room_service='room_service' in request.POST
        parking='parking' in request.POST
        pet_friendly='pet_friendly' in request.POST
        ac='ac' in request.POST
        laundry='laundry' in request.POST
        tv='tv' in request.POST
        amenities= {
            "wifi": wifi,
            "swimming_pool": swimming_pool,
            "fitness_center": fitness_center,
            "spa": spa,
            "restaurant": restaurant,
            "bar": bar,
            "room_service": room_service,
            "parking": parking,
            "pet_friendly": pet_friendly,
            "ac": ac,
            "tv": tv,
            "laundry": laundry
        }
        from .models import hotel
        maxid = hotel.objects.aggregate(max_rid=Max('rid'))['max_rid']
        hotels = hotel.objects.filter(rid=maxid).first()
        hotels.amenities=amenities
        hotels.save()
        return redirect('ahotel')
        
    else:
        return redirect('index')  

#admin restaurant
def arestaurant(request):
    user_name = request.session.get('auser_name')
    if user_name:
        from .models import restaurant
        hotels=restaurant.objects.all().values
        return render(request, 'aRestaurant.html', {'user_name': user_name,'hotel':hotels})
    else:
        return redirect('index')


#update hotel
def updateRestaurant(request):
    if request.method=='POST':
        hotel_name=request.POST['hotel_name']
        hotel_area=request.POST['hotel_area']
        hotel_city=request.POST['hotel_city']
        hotel_link=request.POST['hotel_link']
        hotel_description=request.POST['hotel_description']
        hid=request.POST['id']


        from .models import restaurant
        hotels=restaurant.objects.filter(rid=hid).first()
        hotels.name=hotel_name
        hotels.city=hotel_city
        hotels.area=hotel_area
        hotels.location=hotel_link
        hotels.deacription=hotel_description
        hotels.save()
        
        return redirect('arestaurant')
        
    else:
        return redirect('index')
        
#restaurant photo update
def restaurantPhoto(request):
    form = RestaurantPhoto(request.POST, request.FILES)
    from .models import restaurant
    id=request.POST['id']
    if form.is_valid():
        restaurant = restaurant.objects.filter(rid=id).first()
        restaurant.img = form.cleaned_data['img']
        restaurant.save()
    return redirect('arestaurant')

#add hotel
def addRestaurant(request):
    if request.method=='POST':
        form = RestaurantForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Save the image file to the media directory
            form.instance.img = request.FILES['img']

            # Save the form data to the hotel model
            form.save()
        return redirect('arestaurant')
        
    else:
        return redirect('index')  


#admin place
def aplaces(request):
    user_name = request.session.get('auser_name')
    if user_name:
        from .models import place
        hotels=place.objects.all().values
        return render(request, 'aplaces.html', {'user_name': user_name,'hotel':hotels})
    else:
        return redirect('index')

#update hotel
def updatePlace(request):
    if request.method=='POST':
        hotel_name=request.POST['hotel_name']
        hotel_area=request.POST['hotel_area']
        hotel_city=request.POST['hotel_city']
        hotel_link=request.POST['hotel_link']
        hotel_description=request.POST['hotel_description']
        hid=request.POST['id']

        from .models import place
        hotels=place.objects.filter(rid=hid).first()
        hotels.name=hotel_name
        hotels.city=hotel_city
        hotels.area=hotel_area
        hotels.location=hotel_link
        hotels.deacription=hotel_description
        hotels.save()
        return redirect('aplaces')   
    else:
        return redirect('index')    

#place photo update
def placePhoto(request):
    form = GuidePhoto(request.POST, request.FILES)
    from .models import place
    id=request.POST['id']
    if form.is_valid():
        places = place.objects.filter(rid=id).first()
        places.img = form.cleaned_data['img']
        places.save()
    return redirect('aplaces')

#add place
def addPlace(request):
    if request.method=='POST':
        form = PlaceForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Save the image file to the media directory
            form.instance.img = request.FILES['img']

            # Save the form data to the hotel model
            form.save()
        return redirect('aplaces')
        
    else:
        return redirect('index')  

#view tourguide
def viewtourguide(request):
    user_name = request.session.get('auser_name')
    if user_name:
        hotels=TourGuide.objects.all().values
        return render(request, 'aviewGuide.html', {'user_name': user_name,'guide':hotels})
    else:
        return redirect('index')





#test page
#view tourguide
def test(request):
    return render(request, 'test.html')
