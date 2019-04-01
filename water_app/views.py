from django.shortcuts import render
from water_app.forms import WaterParameterForm
from water_app.models import WaterParameter


def index(request):
    data = 'Dashboard'
    sample_list = WaterParameter.objects.values('id', 'title')

    return render(request, 'water_app/index.html', {'data': data, 'sample_list': sample_list})

def water_add(request):
    '''
    Add water Parameter
    '''
    page = 'water_app/add.html'
    message = ""

    if request.method == "POST":
        form = WaterParameterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                message = "Parameter submitted successfully"
                return redirect('')
            except:
                pass
    else:
        form = WaterParameterForm()

    return render(request, page, {'form':form, 'message': message} )


def dashboard(request, sample_id=None):
    '''
    Dashboard
    '''
    page = 'water_app/dashboard.html'
    message = ""
    data = ""

    print(sample_id)
    data = WaterParameter.objects.get(id=sample_id)

    return render(request, page, {'data': data})
