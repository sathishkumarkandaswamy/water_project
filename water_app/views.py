from django.shortcuts import render
from water_app.forms import WaterParameterForm


def index(request):
    data = 'Dashboard'
    return render(request, 'water_app/index.html', {'data': data})

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
