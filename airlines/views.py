import datetime
from django.shortcuts import redirect, render
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from armsApp import models, forms
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

def context_data():
    context = {
        'page_name' : '',
        'page_title' : '',
        'system_name' : 'Airlines Reservation Managament System',
        'topbar' : True,
        'footer' : True,
    }

    return context
    
#Airline
@login_required
def list_airline(request):
    context = context_data()
    context['page_title'] ="Airlines"
    context['airlines'] = models.Airlines.objects.filter(delete_flag = 0).all()
    return render(request, 'airlines.html', context) 

@login_required
def manage_airline(request, pk = None):
    if pk is None:
        airline = {}
    else:
        airline = models.Airlines.objects.get(id = pk)
    context = context_data()
    context['page_title'] ="Manage Airline"
    context['airline'] = airline
    return render(request, 'manage_airline.html', context) 

@login_required
def save_airline(request):
    resp = { 'status': 'failed', 'msg':'' }
    if not request.method == 'POST':
       resp['msg'] = "No data has been sent."
    else:
        post = request.POST
        if not post['id'] == '':
            airline = models.Airlines.objects.get(id = post['id'])
            form = forms.SaveAirlines(request.POST, request.FILES, instance = airline)
        else:
            form = forms.SaveAirlines(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            resp['status'] = 'success'
            if post['id'] == '':
                resp['msg'] = "New Airline has been added successfully."
            else:
                resp['msg'] = "Airline Details has been updated successfully."
            messages.success(request,f"{resp['msg']}")
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str("<br />")

                    resp['msg'] += str(f"[{field.name}] {error}")
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_airline(request, pk=None):
    resp = { 'status' : 'failed', 'msg' : '' }
    if pk is None:
        resp['msg'] = 'No ID has been sent'
    else:
        try:
            models.Airlines.objects.filter(id = pk).update(delete_flag = 1)
            resp['status'] = 'success'
            messages.success(request, "Airline has been deleted successfully")
        except:
            resp['msg'] = 'Airline has failed to delete'
    return HttpResponse(json.dumps(resp), content_type="application/json")