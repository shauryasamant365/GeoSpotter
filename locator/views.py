import ipaddress
from .models import Contact, IpAddress
from django.shortcuts import redirect, render
import ipinfo

# Create your views here.
def index(request):
    if request.method == 'POST':
        ip_address = request.POST['ip']
        try:
            ip_obj = ipaddress.ip_address(ip_address)
            if isinstance(ip_obj, ipaddress.IPv4Address):
                valid = True
            elif isinstance(ip_obj, ipaddress.IPv6Address):
                valid = True
        except ValueError:
            valid = False
        if valid:
            IpAddress.objects.create(address=ip_address).save()
            # access token for ipinfo.io
            access_token = '012ed5e8fac2ce'
            # create a client object with the access token
            handler = ipinfo.getHandler(access_token)
            # get the ip info
            details = handler.getDetails(ip_address)
            # print the ip info
            data = details.all.items()
            # for key, value in details.all.items():
            #     print(f"{str(key).title()}: {value}")
            return render(request, 'index.html', {'valid': True, 'data': data})
        else:
            return render(request, 'not_valid.html')
    else:
        return render(request, 'index.html')
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        form = Contact.objects.create(name=name, email=email, message=message)
        form.save()
        return redirect('index')
    else:
        return render(request, 'contact.html')
