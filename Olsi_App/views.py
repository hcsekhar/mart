from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


# Create your views here.
branch = Branches.objects.all()
prdt_data = product_Db.objects.all()
cat_data = category_Db.objects.all()
prdt_faq = Product_FAQ.objects.all()
state = Branch.objects.all()


def home(req):
    return render(req, 'Olsi_app_Html/index.html', {'data' : prdt_data,'category':cat_data,'branch':branch,'state':state})

def business(req):
    return render(req, 'Olsi_app_Html/business.html',{'state':state})

def products(req,id):
    if id == 0:
        product = product_Db.objects.all()
    else:
        category = category_Db.objects.get(id=id)
        product = product_Db.objects.filter(category=category)
    allcategory = category_Db.objects.all() 
    return render(req, 'Olsi_app_Html/product.html',{'data' : prdt_data,'product':product,'category':cat_data,'state':state})

def aboutus(req):
    return render(req, 'Olsi_app_Html/Aboutus.html',{'data' : prdt_data,'category':cat_data,'state':state})

def agriculture(req):
    return render(req, 'Olsi_app_Html/agriculture.html',{'data' : prdt_data,'category':cat_data,'state':state})

def manufacture(req):
    return render(req, 'Olsi_app_Html/manufacture.html',{'data' : prdt_data,'category':cat_data,'state':state})

def dwnld(req,id):
     vwprdt = product_Db.objects.get(id=id)
     desc = Product_dsc.objects.filter(PRDT_DSC_Title = vwprdt.PRDT_Title)
     faq = Product_FAQ.objects.filter(PRDT_FAQ_Title = vwprdt.PRDT_Title)
     feature = Product_feat.objects.filter(PRDT_FEAT_Title = vwprdt.PRDT_Title)
     use = Product_usage.objects.filter(PRDT_USE_Title = vwprdt.PRDT_Title,)
     return render(req, 'Olsi_app_Html/dwnld.html',{'i':vwprdt,'data' : prdt_data,'category':cat_data,'state':state})

def prddwnld(req):
        product = product_Db.objects.all()
        return render(req, 'Olsi_app_Html/prddown.html',{'data' : prdt_data,'product':product,'category':cat_data,'state':state})

def offers(req):
    return render(req, 'Olsi_app_Html/offers.html',{'data' : prdt_data,'category':cat_data,'state':state})
def career(req):
    return render(req,'Olsi_app_Html/career.html',{'state':state})

def Documentation(req):
    return render(req, 'Olsi_app_Html/Documentation.html',{'data' : prdt_data,'category':cat_data,'state':state})


def applyJob(request):
    fn = request.POST['first_name']
    ln = request.POST['last_name']
    em = request.POST['email']
    jr = request.POST['job_role']
    num = request.POST['number']
    qlfc = request.POST['qualification']
    ct = request.POST['city']
    pc = request.POST['pincode']
    dt = request.POST['date']
    pdf_file = request.FILES['upload_file']
    
    message = EmailMessage(
        f'Apply For the {jr}',
        f'Hi {settings.EMAIL_HOST_USER}\n,\n\tname = {fn+" "+ln},\n\temail = {em},\n\tJob Role = {jr},\n\tMobile = {num},\n\tQualification = {qlfc},\n\tCity = {ct},\n\tPincode = {pc},\n\tDate = {dt}',
        em,
        [settings.EMAIL_HOST_USER],
    )
    message.attach(pdf_file.name, pdf_file.read(), pdf_file.content_type)
    message.send(fail_silently=False) 
    # alert_mgs = messages.success(request,"Thank you for submition we will get back to you")
    return render(request, 'Olsi_app_Html/career.html',{'data' : prdt_data,'category':cat_data,'state':state})

def viewproduct(req, id):
    vwprdt = product_Db.objects.get(id=id)
    desc = Product_dsc.objects.filter(PRDT_DSC_Title = vwprdt.PRDT_Title)
    faq = Product_FAQ.objects.filter(PRDT_FAQ_Title = vwprdt.PRDT_Title)
    feature = Product_feat.objects.filter(PRDT_FEAT_Title = vwprdt.PRDT_Title)
    use = Product_usage.objects.filter(PRDT_USE_Title = vwprdt.PRDT_Title,)
    return render(req, 'Olsi_app_Html/viewproduct.html', {'i' : vwprdt,'category':cat_data,'faq':faq,'desc':desc,'feat':feature,'use':use,'data':prdt_data,'state':state})


def contact(req):
    return render(req, 'Olsi_app_Html/contact.html',{'data' : prdt_data,'category':cat_data,'state':state})

def faq(req):
    return render(req, 'Olsi_app_Html/faq.html',{'data' : prdt_data,'category':cat_data,'state':state})

def gallery(req):
    return render(req, 'Olsi_app_Html/galery.html',{'data' : prdt_data,'category':cat_data,'state':state})

def team(req):
    return render(req, 'Olsi_app_Html/team.html',{'data' : prdt_data,'category':cat_data,'state':state})

def check(req):
    return render(req, 'Olsi_app_Html/check.html',{'data' : prdt_data,'category':cat_data,'state':state})
###########

def grivance(req):
    return render(req, 'Olsi_app_Html/grivance.html',{'data' : prdt_data,'category':cat_data,'state':state})

def gst(req):
    return render(req, 'Olsi_app_Html/gst.html',{'data' : prdt_data,'category':cat_data,'state':state})

def ComplianceDocuments(req):
    return render(req, 'Olsi_app_Html/ComplianceDocuments.html',{'data' : prdt_data,'category':cat_data,'state':state})

def Mechanism(req):
    return render(req, 'Olsi_app_Html/Mechanism.html',{'data' : prdt_data, 'category':cat_data,'state':state})

#############

# def branches(req):
#     return render(req, 'Olsi_app_Html/branches.html',{'data' : prdt_data,'category':cat_data})
def branches(req):
     categories = Branch.objects.all()
     query = req.GET['search']
     items= Branches.objects.filter(slug__icontains=query) 
     word="Searched Result :"
    #  state = Branch.objects.get(id=id)
    #  branch = Branches.object.filter(state = state.name)
     return render(req, 'Olsi_app_Html/branches.html',{'data' : prdt_data,'category':cat_data,'item':items,'categories':categories,'state':state})

def underconstruction(req):
    return render(req, 'Olsi_app_Html/404.html',{'data' : prdt_data,'category':cat_data,'state':state})

def register(req):
    return render(req, 'Olsi_app_Html/register.html',{'data' : prdt_data,'category':cat_data,'state':state})

def upcoming(req):
    return render(req, 'Olsi_app_Html/upcoming.html',{'data' : prdt_data,'category':cat_data,'state':state})

def review(req):
    return render(req, 'Olsi_app_Html/review.html',{'data' : prdt_data,'category':cat_data,'state':state})

def cancel_policy(req):
    return render(req, 'Olsi_app_Html/cancel_policy.html',{'data' : prdt_data,'category':cat_data,'state':state})

def privacy_policy(req):
    return render(req, 'Olsi_app_Html/privacy_policy.html',{'data' : prdt_data,'category':cat_data,'state':state})

def prdt_shipping(req):
    return render(req, 'Olsi_app_Html/prdt_shipping.html',{'data' : prdt_data,'category':cat_data,'state':state})

def terms_condition(req):
    return render(req, 'Olsi_app_Html/terms_condition.html',{'data' : prdt_data,'category':cat_data,'state':state})

def login_reg(req):
    return render(req, 'Olsi_app_Html/login_reg.html',{'data' : prdt_data, 'category':cat_data,'state':state})

def otplogin(req):
    return render(req, 'Olsi_app_Html/otplogin.html',{'data' : prdt_data, 'category':cat_data,'state':state})

def distributor(req):
    return render(req, 'Olsi_app_Html/distributor.html',{'data' :prdt_data,'category':cat_data,'state':state})

def training(req):
    return render(req, 'Olsi_app_Html/training.html',{'data' : prdt_data, 'category':cat_data,'state':state})

def add_session(request):
     if request.method == 'POST':
         form = SessionForm(request.POST)
         if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
             # you might associate this address with a specific user or order
            return redirect('trainer')
     else:
         form = SessionForm()
     return render(request, 'Olsi_app_Html/edit_session.html', {'form': form})


def edit_session(request,id):
    address = get_object_or_404(Session, pk=id)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('trainer')
    else:
        form = SessionForm(instance=address)
    return render(request, 'Olsi_app_Html/edit_session.html', {'form': form})


def delete_session(request,id):
	address = Session.objects.get(id=id)
	address.delete()
	return redirect('trainer')

def  trainer(req):
    session = Session.objects.all()
    states = State.objects.all()
    location = Location.objects.all()
    trainer = Trainer.objects.all()
    trainer_type = Trainer_type.objects.all()
    category1 = req.GET.get('category1')
    category2 = req.GET.get('category2')
    category3 = req.GET.get('category3')
    
    if category1:
        session = session.filter(name__slug=category1)

    if category2:
        session = session.filter(state__slug=category2)
        
    if category3:
        session = session.filter(types__slug=category3)
    return render(req,'Olsi_app_Html/trainer.html',{'trainer':session,'state':states,'location':location,'trainers':trainer,'trainer_type':trainer_type,'state':state})

def branch1(req,id):
    vwprdt = Branch.objects.get(id=id)
    items = Branches.objects.filter(state = id)
    return render(req,'Olsi_app_Html/branches.html',{'item':items,'state':state,'state':state})