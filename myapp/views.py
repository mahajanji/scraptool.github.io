from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from myapp.models import *
from django.template.loader import render_to_string, get_template
import uuid,random
from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.http import HttpResponseRedirect
# Create your views here.

def login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/')
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'wrong email and password ....') 
                return redirect('/login/')
        else:
            return render(request, 'login.html')
    except:
        return redirect('/')
        
def logout(request):
    auth.logout(request)
    return redirect('/login/')
    
@login_required(login_url='/login/')
def dashboard(request):
    suppliers = Supplier.objects.all().count()
    metals = metal.objects.all().count()
    grades = Grade.objects.all().count()
    qualitys = Quality.objects.all().count()
    return render(request,'dashboard.html',{'suppliers':suppliers,'metals':metals,'grades':grades,'qualitys':qualitys})
    
    # supplier
    
@login_required(login_url='/login/')
def add_supplier(request):
    u = request.GET.get('u')
    if request.method == 'POST':
        if u is not None:
            users = Supplier.objects.get(id=u)
            users.name = request.POST.get('name')
            users.address = request.POST.get('address')
            users.contact = request.POST.get('contact')
            users.mob_no = request.POST.get('phone')
            users.email = request.POST.get('email')
            users.ename = request.POST.get('ename')
            users.econtact = request.POST.get('econtact')
            users.emob_no = request.POST.get('emob_no')
            users.eemail = request.POST.get('eemail')
            users.save()
            return JsonResponse({'status':1})
        else:
            name = request.POST.get('name')
            address = request.POST.get('address')
            contact = request.POST.get('contact')
            mob_no = request.POST.get('phone')
            email = request.POST.get('email')
            ename = request.POST.get('ename')
            econtact = request.POST.get('econtact')
            emob_no = request.POST.get('emob_no')
            eemail = request.POST.get('eemail')
            cat = Supplier(name=name,address=address,contact=contact,mob_no=mob_no,email=email,ename=ename,econtact=econtact,emob_no=emob_no,eemail=eemail)
            cat.save()
            return JsonResponse({'status':1})
    else:
        if u is not None:
            cat = Supplier.objects.get(id=u)
            return render(request, 'add_supplier.html',{'supplier':cat})
    return render(request,'add_supplier.html')
    
def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request,'suppliers.html',{'suppliers':suppliers})
    
def delete_supplier(request):
    u = request.GET.get('u')
    cat = Supplier.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
    # supplier
    
@login_required(login_url='/login/')
def add_yard(request):
    suppliers = Supplier.objects.all()
    u = request.GET.get('u')
    if request.method == 'POST':
        if u is not None:
            users = Yard.objects.get(id=u)
            users.name = request.POST.get('name')
            users.address = request.POST.get('address')
            supplier = request.POST.get('supplier')
            supplier_id = Supplier.objects.get(id=supplier)
            users.supplier = supplier_id 
            users.save()
            return JsonResponse({'status':1})
        else:
            supplier = request.POST.get('supplier')
            address = request.POST.get('address')
            name = request.POST.get('name')
            supplier_id = Supplier.objects.get(id=supplier)
            cat = Yard(supplier=supplier_id,address=address,name=name)
            cat.save()
            return JsonResponse({'status':1})
    else:
        if u is not None:
            cat = Yard.objects.get(id=u)
            return render(request, 'add_yard.html',{'yard':cat,'suppliers':suppliers})
    return render(request,'add_yard.html',{'suppliers':suppliers})
    
def yards(request):
    u = request.GET.get('s')
    supp = Supplier.objects.get(id=u)
    yardss = Yard.objects.filter(supplier=u)
    return render(request,'yards.html',{'yardss':yardss,'supp':supp})
    
def delete_yard(request):
    u = request.GET.get('u')
    cat = Yard.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
    # metals
    
@login_required(login_url='/login/')
def add_metal(request):
    u = request.GET.get('u')
    if request.method == 'POST':
        if u is not None:
            users = metal.objects.get(id=u)
            users.name = request.POST.get('name')
            users.shortform = request.POST.get('shortform')
            users.misc = request.POST.get('misc')
            users.save()
            return JsonResponse({'status':1})
        else:
            name = request.POST.get('name')
            shortform = request.POST.get('shortform')
            misc = request.POST.get('misc')
            cat = metal(name=name,shortform=shortform,misc=misc)
            cat.save()
            return JsonResponse({'status':1})
    else:
        if u is not None:
            metals = metal.objects.get(id=u)
            return render(request, 'add_metal.html',{'metal':metals})
    return render(request,'add_metal.html')
    
def metals(request):
    allmetals = metal.objects.all()
    return render(request,'metals.html',{'allmetals':allmetals})
    
def delete_metal(request):
    u = request.GET.get('u')
    cat = metal.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
    # cost
    
@login_required(login_url='/login/')
def add_cost(request):
    u = request.GET.get('u')
    if request.method == 'POST':
        if u is not None:
            users = cost.objects.get(id=u)
            users.name = request.POST.get('name')
            users.shortform = request.POST.get('shortform')
            users.rate = request.POST.get('rate')
            users.misc = request.POST.get('misc')
            users.save()
            return JsonResponse({'status':1})
        else:
            name = request.POST.get('name')
            shortform = request.POST.get('shortform')
            rate = request.POST.get('rate')
            misc = request.POST.get('misc')
            cat = cost(name=name,shortform=shortform,rate=rate,misc=misc)
            cat.save()
            return JsonResponse({'status':1})
    else:
        if u is not None:
            cat = cost.objects.get(id=u)
            return render(request, 'add_cost.html',{'costs':cat})
    return render(request,'add_cost.html')
    
def costs(request):
    costs = cost.objects.all()
    values = GradeNewValue.objects.filter(id=3)
    return render(request,'costs.html',{'costs':costs,'values':values})
    
    
def delete_cost(request):
    u = request.GET.get('u')
    costs = cost.objects.filter(id=u)
    if costs:
        costs = cost.objects.get(id=u)
        costs.delete()
        return JsonResponse({'status':1})
    return JsonResponse({'status':0})
    
    # grade
    
@login_required(login_url='/login/')
def add_grade(request):
    u = request.GET.get('u')
    costs = cost.objects.all()
    metals = metal.objects.all()
    if request.method == 'POST':
        if u is not None:
            users = Grade.objects.get(id=u)
            users.name = request.POST.get('name')
            users.details = request.POST.get('details')
            users.gradegrp = request.POST.get('gradegrp')
            users.misc = request.POST.get('miscellaneous')
            users.typeo = request.POST.get('typeo')
            users.recovery = request.POST.get('Recovery')
            users.save()
            Metal = request.POST.getlist('Metal[]')
            Metal_Cost = request.POST.getlist('Metal_Cost[]')
            Overhead = request.POST.getlist('Overhead[]')
            Overhead_Cost = request.POST.getlist('Overhead_Cost[]')
            for c, m in zip(Metal_Cost, Metal):
                metals = metal.objects.get(id=m)
                grademetal = GradeMetal(grade=users,metal=metals,cost=c)
                grademetal.save()
            for o, ocv in zip(Overhead, Overhead_Cost):
                costs = cost.objects.get(id=o)
                gradecosts = GradeOverhead(grade=users,cost=costs,cost_value=ocv)
                gradecosts.save()
            return JsonResponse({'status':1})
        else:
            name = request.POST.get('name')
            details = request.POST.get('details')
            gradegrp = request.POST.get('gradegrp')
            miscellaneous = request.POST.get('miscellaneous')
            typeo = request.POST.get('typeo')
            Recovery = request.POST.get('Recovery')
            Metal = request.POST.getlist('Metal[]')
            Metal_Cost = request.POST.getlist('Metal_Cost[]')
            Overhead = request.POST.getlist('Overhead[]')
            Overhead_Cost = request.POST.getlist('Overhead_Cost[]')
            grade = Grade(name=name,details=details,gradegrp=gradegrp, misc=miscellaneous,typeo=typeo,recovery=Recovery)
            grade.save()
            for c, m in zip(Metal_Cost, Metal):
                metals = metal.objects.get(id=m)
                grademetal = GradeMetal(grade=grade,metal=metals,cost=c)
                grademetal.save()
            for o, ocv in zip(Overhead, Overhead_Cost):
                costs = cost.objects.get(id=o)
                gradegverhead = GradeOverhead(grade=grade,cost=costs,cost_value=ocv)
                gradegverhead.save()
            return JsonResponse({'status':1})
    else:
        if u is not None:
            cat = Grade.objects.get(id=u)
            return render(request, 'update_grade.html',{'grades':cat,'costs':costs,'metals':metals})
    return render(request,'add_grade.html',{'costs':costs,'metals':metals})
    
def grades(request):
    grades = Grade.objects.all()
    return render(request,'grades.html',{'grades':grades})
    
def gradenewvalue(request):
    name = request.GET.get('name')
    values = GradeNewValue.objects.filter(id=3)
    if values:
        values = GradeNewValue.objects.get(id=3)
        values.name = name
        values.save()
        messages.success(request, 'details updated.')
    return redirect(request.META['HTTP_REFERER'])
    
def delete_grade(request):
    u = request.GET.get('u')
    cat = Grade.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
def delete_metal_grade(request):
    u = request.GET.get('id')
    cat = GradeMetal.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
def delete_metal_overhead(request):
    u = request.GET.get('id')
    cat = GradeOverhead.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})

def update_metal_grade(request):
    u = request.GET.get('id')
    Metalupdate = request.GET.get('Metalupdate')
    Metal_Costupdate = request.GET.get('Metal_Costupdate')
    metals = metal.objects.get(id=Metalupdate)
    if GradeMetal.objects.filter(id=u):
        cat = GradeMetal.objects.get(id=u)
        cat.metal = metals
        cat.cost = Metal_Costupdate
        cat.save()
        return JsonResponse({'status':1})
    return JsonResponse({'status':0})
    
def update_overhead_grade(request):
    u = request.GET.get('id')
    Overhead_update = request.GET.get('Overhead_update')
    Overhead_Cost_update = request.GET.get('Overhead_Cost_update')
    costs = cost.objects.get(id=Overhead_update)
    if GradeOverhead.objects.filter(id=u):
        cat = GradeOverhead.objects.get(id=u)
        cat.cost = costs
        cat.cost_value = Overhead_Cost_update
        cat.save()
        return JsonResponse({'status':1})
    return JsonResponse({'status':0})
    
    # quality
    
@login_required(login_url='/login/')
def add_quality(request):
    u = request.GET.get('u')
    supp = Supplier.objects.all()
    grades = Grade.objects.all()
    if request.method == 'POST':
        if u is not None:
            suppliers = request.POST.get('supplier')
            grades = request.POST.get('grade')
            Yards = request.POST.get('Yard')
            duty =  request.POST.get('duty')
            weightage = request.POST.getlist('weightagequa[]')
            ww = 0
            for weight in weightage:
                ww = int(ww) + int(weight)
            if ww == 100:
                supplier = Supplier.objects.get(id=suppliers)
                yard = Yard.objects.get(id=Yards)
                grade = Grade.objects.get(id=grades)
                users = Quality.objects.get(id=u)
                users.supplier = supplier
                users.yard = yard
                users.grade = grade
                users.duty = duty
                users.save()
                quaid = request.POST.getlist('quaid[]')
                Metal_Cost = request.POST.getlist('Metal_Costqua[]')
                Overheadid = request.POST.getlist('Overheadid[]')
                cost_value = request.POST.getlist('cost_valuequa[]')
                alc = 0
                wal = 0
                mc = 0
                ohc = 0
                for c, q, w in zip(Metal_Cost, quaid, weightage):
                    if QualityMetal.objects.filter(id=q):
                        metals = metal.objects.get(id=q)
                        if metals.name == 'Aluminium':
                            alc = float(alc) + float(c)
                            wal = float(wal) + float(w)
                        else:
                            cwip =  float(c) * float(w) / 100
                            mc = float(mc) + float(cwip)
                        qual = QualityMetal.objects.get(id=q)
                        qual.quality=users
                        qual.cost=c
                        qual.weightage=w
                        qual.save()
                users.alc = alc
                users.mc = mc
                users.weightage_al = wal
                for o, cv in zip(Overheadid, cost_value):
                    if QualityOverhead.objects.filter(id=o):
                        ohc = float(ohc) + float(cv)
                        overid = QualityOverhead.objects.get(id=o)
                        overid.quality=users
                        overid.cost_value=cv
                        overid.save()
                users.ohc = ohc
                users.save()
                return JsonResponse({'status':1})
            else:
                return JsonResponse({'status':2,'w':ww})
        else:
            suppliers = request.POST.get('supplier')
            grades = request.POST.get('grade')
            Yards = request.POST.get('Yard')
            duty =  request.POST.get('duty')
            recovery = request.POST.get('recovery')
            typeo =  request.POST.get('typeo')
            supplier = Supplier.objects.get(id=suppliers)
            yard = Yard.objects.get(id=Yards)
            grade = Grade.objects.get(id=grades)
            Metal = request.POST.getlist('Metal[]')
            Metal_Cost = request.POST.getlist('Metal_Cost[]')
            weightage = request.POST.getlist('weightage[]')
            ww = 0
            for weight in weightage:
                ww = int(ww) + int(weight)
            if ww == 100:
                if Quality.objects.filter(supplier=supplier,yard=yard):
                    return JsonResponse({'status':3})
                else:
                    Overhead = request.POST.getlist('Overhead[]')
                    cost_value = request.POST.getlist('cost_value[]')
                    cat = Quality(supplier=supplier,yard=yard,grade=grade,duty=duty,recovery=recovery,typeo=typeo)
                    cat.save()
                    alc = 0
                    wal = 0
                    mc = 0
                    ohc = 0
                    for c, m, w in zip(Metal_Cost, Metal, weightage):
                        metals = metal.objects.get(id=m)
                        if metals.name == 'Aluminium':
                            alc = float(alc) + float(c)
                            wal = float(wal) + float(w)
                        else:
                            cwip =  float(c) * float(w) / 100
                            mc = float(mc) + float(cwip)
                        grademetal = QualityMetal(quality=cat,metal=metals,cost=c,weightage=w)
                        grademetal.save()
                    cat.alc = alc
                    cat.mc = mc
                    cat.weightage_al = wal
                    for o, cv in zip(Overhead, cost_value):
                        ohc = float(ohc) + float(cv)
                        costs = cost.objects.get(id=o)
                        gradegverhead = QualityOverhead(quality=cat,cost=costs,cost_value=cv)
                        gradegverhead.save()
                    cat.ohc = ohc
                    cat.save()
                    return JsonResponse({'status':1})
            else:
                return JsonResponse({'status':2,'w':ww})
    else:
        if u is not None:
            cat = Quality.objects.get(id=u)
            return render(request, 'update_quality.html',{'qua':cat,'supp':supp,'grades':grades})
    return render(request,'add_quality.html',{'supp':supp,'grades':grades})
    
def qualitys(request):
    qualitys = Quality.objects.all()
    return render(request,'qualitys.html',{'qualitys':qualitys})
    
def delete_quality(request):
    u = request.GET.get('u')
    cat = Quality.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
    # actual
    
@login_required(login_url='/login/')
def add_actual(request):
    u = request.GET.get('u')
    supp = Supplier.objects.all()
    qualitys = Quality.objects.all()
    if request.method == 'POST':
        if u is not None:
            suppliers = request.POST.get('supplier')
            Yards = request.POST.get('Yard')
            duty =  request.POST.get('duty')
            supplier = Supplier.objects.get(id=suppliers)
            po_number = request.POST.get('po_number')
            yard = Yard.objects.get(id=Yards)
            users = Actual.objects.get(id=u)
            users.supplier = supplier
            users.yard = yard
            users.duty = duty
            users.po_number = po_number
            users.save()
            actualmidu = request.POST.getlist('actualmidu[]')
            Metal_Cost = request.POST.getlist('Metal_Costactualu[]')
            weightage = request.POST.getlist('weightageactualu[]')
            actual_value = request.POST.getlist('actual_valueu[]')
            for c, m, w, av in zip(Metal_Cost, actualmidu, weightage, actual_value):
                if ActualMetal.objects.filter(id=m):
                    actualmetal = ActualMetal.objects.get(id=m)
                    actualmetal.actual=users
                    actualmetal.cost=c
                    actualmetal.actual_value=av
                    actualmetal.save()
            return JsonResponse({'status':1})
        else:
            suppliers = request.POST.get('supplier')
            Yards = request.POST.get('Yard')
            gradeid = request.POST.get('gradeid')
            grade = Grade.objects.get(id=gradeid)
            duty =  request.POST.get('duty')
            po_number = request.POST.get('po_number')
            typeoid = request.POST.get('typeo')
            recovery = request.POST.get('recovery')
            supplier = Supplier.objects.get(id=suppliers)
            yard = Yard.objects.get(id=Yards)
            Metal = request.POST.getlist('metalid[]')
            Metal_Cost = request.POST.getlist('Metal_Costactual[]')
            weightage = request.POST.getlist('weightageactual[]')
            actual_value = request.POST.getlist('actual_value[]')
            Overhead = request.POST.getlist('costoverheadid[]')
            cost_value = request.POST.getlist('cost_valueactual[]')
            ww = 0
            for act in actual_value:
                ww = int(ww) + int(act)
            if ww == 100:
                if Actual.objects.filter(supplier=supplier,yard=yard):
                    return JsonResponse({'status':3})
                else:
                    cat = Actual(supplier=supplier,yard=yard,grade=grade,duty=duty,recovery=recovery,typeo=typeoid,po_number=po_number)
                    cat.save()
                    alc = 0
                    wal = 0
                    mc = 0
                    ohc = 0
                    for c, m, w, av in zip(Metal_Cost, Metal, weightage, actual_value):
                        metals = metal.objects.get(id=m)
                        if metals.name == 'Aluminium':
                            alc = float(alc) + float(c)
                            wal = float(wal) + float(w)
                        else:
                            cwip =  float(c) * float(w) / 100
                            mc = float(mc) + float(cwip)
                        grademetal = ActualMetal(actual=cat,metal=metals,cost=c,weightage=w,actual_value=av)
                        grademetal.save()
                    cat.alc = alc
                    cat.mc = mc
                    cat.weightage_al = wal
                    for o, cv in zip(Overhead, cost_value):
                        ohc = float(ohc) + float(cv)
                        costs = cost.objects.get(id=o)
                        gradegverhead = ActualOverhead(actual=cat,cost=costs,cost_value=cv)
                        gradegverhead.save()
                    cat.ohc = ohc
                    cat.save()
                    return JsonResponse({'status':1})
            else:
                return JsonResponse({'status':2,'w':ww})
    else:
        if u is not None:
            cat = Actual.objects.get(id=u)
            return render(request, 'update_actual.html',{'qua':cat,'supp':supp,'qualitys':qualitys})
    return render(request,'add_actual.html',{'supp':supp,'qualitys':qualitys})
    
def actuals(request):
    actuals = Actual.objects.all()
    return render(request,'actuals.html',{'actuals':actuals})
    
def delete_actual(request):
    u = request.GET.get('u')
    cat = Actual.objects.get(id=u)
    cat.delete()
    return JsonResponse({'status':1})
    
    #add_calculation
    
def add_calculation(request):
    u = request.GET.get('u')
    gradenewvalue = GradeNewValue.objects.filter(id=3)
    grades = Grade.objects.all()
    if request.method == 'POST':
        pass
    else:
        if u is not None:
            cat = Actual.objects.get(id=u)
            return render(request,'add_calculation.html',{'grades':grades})
    return render(request,'add_calculation.html',{'grades':grades,'gradenewvalue':gradenewvalue})
    
def calculations(request):
    return render(request,'calculations.html')
    
    # AJax
    
def fatch_cost_ajax(request):
    x = request.GET.get('x')
    gradec = cost.objects.filter(id=x)
    if gradec:
        gradec = cost.objects.get(id=x)
        costrate = gradec.rate
        return JsonResponse({'status':1,'costrate':costrate})
    else:
        return JsonResponse({'status':0})
        
def fatch_Supplier_ajax(request):
    x = request.GET.get('x')
    qua = request.GET.get('qua')
    if qua is not None:
        sYard = Yard.objects.filter(supplier_id=x)
        qua = Quality.objects.get(id=qua)
        return render(request, 'load_data.html',{'sYard':sYard,'qua':qua})
    else:
        sYardss = Yard.objects.filter(supplier_id=x)
        return render(request, 'ajax_yard.html',{'sYardss':sYardss})
        
def fatch_yard_quality_ajax(request):
    x = request.GET.get('x')
    qua = request.GET.get('qua')
    if qua is not None:
        sYard = Yard.objects.filter(supplier_id=x)
        qua = Actual.objects.get(id=qua)
        return render(request, 'load_data.html',{'sYard':sYard,'qua':qua})
    else:
        sYards = Yard.objects.filter(supplier_id=x)
        return render(request, 'ajax_yard.html',{'sYardss':sYards})
    
def fatch_grade_ajax(request):
    x = request.GET.get('x')
    grades = Grade.objects.filter(id=x)
    return render(request, 'load_data.html',{'grades':grades})

        
def fatch_quality_ajax(request):
    x = request.GET.get('x')
    s = request.GET.get('s')
    y = request.GET.get('y')
    Yardid = request.GET.get('Yardid')
    supplierid = request.GET.get('supplierid')
    if s is not None:
        quaactual = Quality.objects.filter(supplier__id=s,yard__id=y)
        return render(request, 'load_data.html',{'quaactual':quaactual})
    elif Yardid is not None:
        Actualid = Actual.objects.filter(supplier__id=supplierid,yard__id=Yardid)
        return render(request, 'load_data.html',{'Actualid':Actualid})
    else:
        quality = Quality.objects.filter(id=x)
        return render(request, 'load_data.html',{'quality':quality})
        
# ajax calc

def fatch_grade_calculator(request):
    grade = request.GET.get('grade')
    actualquality = request.GET.get('actualquality')
    if actualquality == 'Quality':
        quality = Quality.objects.filter(grade__id=grade)
        return render(request, 'load_calc.html',{'quality':quality})
    else:
        quality = Actual.objects.filter(grade__id=grade)
        return render(request, 'load_calc.html',{'quality':quality,'actual':1})
    