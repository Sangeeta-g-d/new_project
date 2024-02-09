from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden,HttpResponseBadRequest
from django.template import loader
from .models import NewUser,PasswordReset, APMCTender,APMCETender, Grades
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import date
import pandas as pd
import os
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .helpers import send_forget_password_mail
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here

# yourapp/views.py

from django.shortcuts import render
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from .models import APMCETender
from django.utils import timezone
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_driver_path = r'C:\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe'


def run_selenium(request):
    print("!!!!!!!!!!!!!!!!!!$%^&*()")
    try:
        filter_value = request.GET.get('filter', '')
        print(filter_value)
        '''if request.method == 'POST':
            # Retrieve and parse the JSON data from the request body
            data = json.loads(request.body)
            row_data = data.get('row_data')  # Access the 'row_data' object
            
            # Access specific fields from the received data
            row_id = row_data.get('row_id')
            commission_agent = row_data.get('commission_agent')
            rs = row_data.get('rs')
            lot_id = row_data.get('lot_id')

            # Process the received data
            print("Row ID:", row_id)
            print("Commission Agent:", commission_agent)
            print("RS:", rs)'''
        # Fetch data from APMCETender model
        today_date = timezone.localdate()
        recent_tenders = APMCETender.objects.filter(created_on=today_date)
        recent_tenders_list = list(recent_tenders)
        print("@@@2",recent_tenders)

        # Replace these with your actual credentials
        username = "hublSkba"
        password = "Skb@12345"

        # Specify the path to your webdriver (download the appropriate driver for your browser)
        # For example, if using Chrome, download the ChromeDriver: https://sites.google.com/chromium.org/driver/
        # s = ChromeService('C:\chromedriver-win64\chromedriver-win64\chromedriver.exe')
        s = ChromeService('C:\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe')
        

        
        chrome_options = Options()
        s = ChromeService(executable_path=chrome_driver_path, chrome_options=chrome_options)
        web = webdriver.Chrome(service=s)
        # Navigate to the login page
        web.get("https://ka54.remsl.in/UMPeMandi/")
        time.sleep(1)

        # Locate the username and password input fields and submit button
        username_field = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(1) > input")
        password_field = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(2) > input")
        submit_button = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(4) > button")

        # Input your credentials
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

       

        # Wait for a few seconds to observe the result (you can replace this with proper waiting mechanisms)
        web.implicitly_wait(5)
        time.sleep(15)

        # Navigate to the tender page
        web.get("https://ka54.remsl.in/UMPeMandi/views/index.html#/batchEtender?moduleId=200023")
        time.sleep(10)

        batch_dropdown = Select(web.find_element(By.NAME, 'batchId'))  # Replace with the actual name or identifier of the batch dropdown
        batch_dropdown.select_by_visible_text("DRY CHILLY")  # Replace with the actual name of the batch from your data
        time.sleep(5)

        batch_dropdown = Select(web.find_element(By.NAME, 'batchId'))  # Replace with the actual name or identifier of the batch dropdown
        batch_dropdown.select_by_visible_text("DRY CHILLY")  # Replace with the actual name of the batch from your data
        time.sleep(5)
        
        
        search_bar = web.find_element(By.ID, 'commissionAgent')
        search_term = filter_value

        time.sleep(2)

# Type the search term into the search bar
        search_bar.send_keys(search_term)
        time.sleep(5)
        print("^^^^^^^^^^^^^")

# Define the ID of the dropdown UL
       # Find all elements with class 'ui-menu-item'
        wait = WebDriverWait(web, 15)

        try:
    # Define the XPath for the desired option
            element_xpath = f"//div[contains(@class, 'ui-menu-item-wrapper') and contains(text(), '{search_term}')]"
    
    # Wait for the element to be visible
            option = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    # Click on the element
            option.click()
            print("Clicked on the element")
            time.sleep(5)  # Adjust this delay as needed

# Retrieve the table element again
            table_element = web.find_element(By.ID, 'biddingGrid')
            lot_code_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'footable-visible')]//label[starts-with(@id, 'lblShortCode_')]")
            

# Retrieve lot IDs from recent_tenders
            lot_ids = [str(tender.lot_id) for tender in recent_tenders_list]
            print("!!!!!!!!!",lot_ids)

# Iterate through the found elements
            for element in lot_code_elements:
                lot_code_website = element.text.strip()
                print("***********",lot_code_website)  # Get the lot code text

    # Check if the lot code from the website matches any lot ID from recent_tenders
                if lot_code_website in lot_ids:
                    print(f"Matching lot code found: {lot_code_website}")
        # Get the corresponding tender object based on the lot ID
                    corresponding_tender = next((tender for tender in recent_tenders_list if str(tender.lot_id) == lot_code_website), None)
                    if corresponding_tender:
                        print(f"Corresponding tender found for lot code {lot_code_website}.")
            
            # Find the input field associated with this lot code by tag name 'input'
                        input_field = element.find_element(By.XPATH, "./following::td[contains(@class, 'footable-visible')]//input[@type='number']")
            
            # Input the quote value into the input field
                        input_field.clear()
                        rs_value = corresponding_tender.rs
                        print("rs value",rs_value)
                        input_field.send_keys(str(rs_value))  # Update input field with the rs value
                    else:
                        print("Corresponding tender not found.")
            submit_bids = web.find_element(By.ID, "submitBids")
            submit_bids.click()
            time.sleep(2)
            confirm_bid = web.find_element(By.ID, "confirmBid")
            confirm_bid.click()
            time.sleep(2)
            # Find all elements that contain the lot codes
            lot_code_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'footable-visible')]//label[starts-with(@id, 'lblShortCode_')]")

# Find all elements that contain the messages
            message_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'rowUnderline')]//label[starts-with(@id, 'lblMsg_')]")

# Extract and store the lot codes and messages together
            lot_codes_and_messages = []
            for lot_code_element, message_element in zip(lot_code_elements, message_elements):
                lot_code = lot_code_element.text.strip()
                message = message_element.text.strip()
                lot_codes_and_messages.append({"Lot_Code": lot_code, "Message": message})
# Now 'lot_codes_and_messages' holds pairs of lot codes and their respective messages
            json_response = json.dumps(lot_codes_and_messages)
            



        except Exception as ex:
            print("Error occurred:", ex)
            time.sleep(10) 
# Logout
        

        # Close the browser window
        web.quit()
        json_response = json.dumps(lot_codes_and_messages)

        return JsonResponse({'status': 'Selenium executed successfully', 'data': json_response})
    except Exception as e:
        return JsonResponse({'status': 'Error in Selenium execution', 'error_message': str(e)})


def run_selenium_row(request):
    print("AAAAAAAAAAAAAAAAAAAAAAa")
    try:
        filter_value = request.GET.get('filter', '')
        print(filter_value)
        if request.method == 'POST':
            # Retrieve and parse the JSON data from the request body
            data = json.loads(request.body)
            print(data)
            row_data = data.get('row_data')  # Access the 'row_data' object
            
            # Access specific fields from the received data
            row_id = row_data.get('row_id')
            commission_agent = row_data.get('commission_agent')
            rs = row_data.get('rs')
            lot_id = row_data.get('lot_id')

            # Process the received data
            print("Row ID:", row_id)
            print("Commission Agent:", commission_agent)
            print("RS:", rs)
        # Fetch data from APMCETender model
        '''today_date = timezone.localdate()
        recent_tenders = APMCETender.objects.filter(created_on=today_date)
        recent_tenders_list = list(recent_tenders)
        print("@@@2",recent_tenders)'''

        # Replace these with your actual credentials
        username = "hublSkba"
        password = "Skb@12345"

        # Specify the path to your webdriver (download the appropriate driver for your browser)
        # For example, if using Chrome, download the ChromeDriver: https://sites.google.com/chromium.org/driver/
        s = ChromeService('C:\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe')
        

        
        chrome_options = Options()
        s = ChromeService(executable_path=chrome_driver_path, chrome_options=chrome_options)
        web = webdriver.Chrome(service=s)

        # Navigate to the login page
        web.get("https://ka54.remsl.in/UMPeMandi/")
        time.sleep(1)

        # Locate the username and password input fields and submit button
        username_field = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(1) > input")
        password_field = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(2) > input")
        submit_button = web.find_element(By.CSS_SELECTOR, "#LoginControllerID > div.container > div.loginbox > div:nth-child(1) > form > div:nth-child(4) > button")

        # Input your credentials
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

       

        # Wait for a few seconds to observe the result (you can replace this with proper waiting mechanisms)
        web.implicitly_wait(5)
        time.sleep(15)

        # Navigate to the tender page
        web.get("https://ka54.remsl.in/UMPeMandi/views/index.html#/batchEtender?moduleId=200023")
        time.sleep(10)

        batch_dropdown = Select(web.find_element(By.NAME, 'batchId'))  # Replace with the actual name or identifier of the batch dropdown
        batch_dropdown.select_by_visible_text("DRY CHILLY")  # Replace with the actual name of the batch from your data
        time.sleep(5)

        batch_dropdown = Select(web.find_element(By.NAME, 'batchId'))  # Replace with the actual name or identifier of the batch dropdown
        batch_dropdown.select_by_visible_text("DRY CHILLY")  # Replace with the actual name of the batch from your data
        time.sleep(5)
        
        
        search_bar = web.find_element(By.ID, 'commissionAgent')
        search_term = commission_agent

        time.sleep(2)

# Type the search term into the search bar
        search_bar.send_keys(search_term)
        time.sleep(5)
        print("^^^^^^^^^^^^^")

# Define the ID of the dropdown UL
       # Find all elements with class 'ui-menu-item'
        wait = WebDriverWait(web, 15)

        try:
    # Define the XPath for the desired option
            element_xpath = f"//div[contains(@class, 'ui-menu-item-wrapper') and contains(text(), '{search_term}')]"
    
    # Wait for the element to be visible
            option = wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    # Click on the element
            option.click()
            print("Clicked on the element")
            time.sleep(5)  # Adjust this delay as needed

# Retrieve the table element again
            table_element = web.find_element(By.ID, 'biddingGrid')
            

# Retrieve lot IDs from recent_tenders
            lot_code_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'footable-visible')]//label[starts-with(@id, 'lblShortCode_')]")

# Find the element that contains the specific lot code
            matching_lot_code_element = None

            for element in lot_code_elements:
                lot_code_website = element.text.strip()
                if lot_code_website == lot_id:
                    matching_lot_code_element = element
                    break

            if matching_lot_code_element:
                try:
                    input_field = matching_lot_code_element.find_element(By.XPATH, "./following::td[contains(@class, 'footable-visible')]//input[@type='number']")
                    rs_value = row_data.get('rs')  # Assuming 'rs' is obtained from row_data or somewhere else
                    input_field.clear()
                    input_field.send_keys(str(rs_value))
                    time.sleep(3)
                except NoSuchElementException as e:
                    print("Error finding or interacting with the input field:", e)
            else:
                print("Matching lot code element not found.")
            submit_bids = web.find_element(By.ID, "submitBids")
            submit_bids.click()
            time.sleep(5)
            confirm_bid = web.find_element(By.ID, "confirmBid")
            confirm_bid.click()
            time.sleep(6)
            # Find all elements that contain the lot codes
            lot_code_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'footable-visible')]//label[starts-with(@id, 'lblShortCode_')]")

# Find all elements that contain the messages
            message_elements = web.find_elements(By.XPATH, "//td[contains(@class, 'rowUnderline')]//label[starts-with(@id, 'lblMsg_')]")

# Extract and store the lot codes and messages together
            lot_codes_and_messages = []
            for lot_code_element, message_element in zip(lot_code_elements, message_elements):
                lot_code = lot_code_element.text.strip()
                message = message_element.text.strip()
                if lot_code == lot_id:
                    lot_codes_and_messages.append({"Lot_Code": lot_code, "Message": message})
                    break 
            if lot_codes_and_messages:
                json_response = json.dumps(lot_codes_and_messages)
            else:
                json_response = json.dumps({"Lot_Code": "", "Message": "Lot code not found."})
# Now 'lot_codes_and_messages' holds pairs of lot codes and their respective messages
            
        
        except Exception as ex:
            print("Error occurred:", ex)
            time.sleep(10) 
# Logout
        

        # Close the browser window
        web.quit()
        json_response = json.dumps(lot_codes_and_messages)

        return JsonResponse({'status': 'Selenium executed successfully', 'data': json_response})
    except Exception as e:
        return JsonResponse({'status': 'Error in Selenium execution', 'error_message': str(e)})




@login_required
def index(request):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
    user = request.user.username
    context = {
    'user':user
    }
    return render(request,'index.html',context)


def register(request):
    return render(request,'register.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login1.html', {'login_failed': True})  # Sending a flag indicating login failure
    return render(request, 'login1.html')

def admin_logout(request):
    logout(request)
    return redirect('login1')

def operator_logout(request):
    logout(request)
    return redirect('operator_login')

def operator_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None and user.user_type == 'operator':
            login(request, user)
            return redirect('operator_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'operator_login.html', {'login_failed': True})

    return render(request, 'operator_login.html')

@login_required
def add_operator(request):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
    if request.method == 'POST':
        email = request.POST.get('email')
        # Check if the user with the given email already exists
        if NewUser.objects.filter(email=email).exists():
            return render(request, 'add_operator.html', {'error': 'User with this email already exists'})
            

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        adhar_no = request.POST.get('adhar_no')
        pan_no = request.POST.get('pan_no')
        password = phone_no
        passw = make_password(password)  # Set password as phone_no or generate a secure password

        # Create a new user instance
        user = NewUser.objects.create(
            email=email,
            username = first_name,
            first_name=first_name,
            last_name=last_name,
            password=passw,
            phone_no=phone_no,
            adhar_no=adhar_no,
            pan_no=pan_no,
            is_staff=True,  # For regular users
            is_active=True    # For active users
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Operator added successfully.')  # Set success message
        return redirect('add_operator')
    return render(request,'add_operator.html')


def quality_range(request):
    obj = Grades.objects.all()
    context = {'obj':obj}
    return render(request,'quality_range.html',context)

def add_quality(request):
    if request.method == 'POST':
        quality = request.POST.get('quality')
        min = request.POST.get('min')
        max = request.POST.get('max')
        data = Grades.objects.create(quality=quality,minimum = min, maximum = max)
        return redirect('quality_range')
    return render(request,'add_quality.html')

def update_quality(request,id):
    data = Grades.objects.get(id=id)
    context = {
    'data':data
    }
    if request.method == 'POST':
        data.quality = request.POST.get('quality')
        data.minimum = request.POST.get('min')
        data.maximum = request.POST.get('max')
        data.save()
        return redirect('quality_range')
    return render(request,'update_quality.html',context)


@login_required
def operators_list(request):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
    obj = NewUser.objects.filter(user_type='operator')
    context = {
    'obj':obj
    }
    return render(request,'operators_list.html',context)

def delete_operator(request, pk):
    application = get_object_or_404(NewUser, pk=pk)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Operator has been deleted successfully.')  # Set success message
        return redirect('operators_list')

def update_operator(request,id):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
    i = id
    print("Iddddddddddddddd",i)
    obj = NewUser.objects.get(id=i)
    context = {
    'obj':obj
    }
    if request.method == 'POST':
        obj.first_name = request.POST.get('first_name')
        obj.last_name = request.POST.get('last_name')
        obj.email = request.POST.get('email')
        obj.phone_no = request.POST.get('phone_no')
        obj.adhar_no = request.POST.get('adhar_no')
        obj.pan_no = request.POST.get('pan_no')
        obj.save()
        messages.success(request, 'Updated successfully.')
        return redirect('operators_list')
    return render(request,'update_operator.html',context)

@login_required
def profile(request):
    if request.user.user_type != 'operator':
        return HttpResponseForbidden()
    id = request.user.id
    user = request.user.first_name
    last = request.user.last_name
    pno = request.user.phone_no
    ad = request.user.adhar_no
    pan = request.user.pan_no
    email = request.user.email

    context = {'user':user, 'last':last,'pno':pno,'ad':ad,'pan':pan,'email':email}
    return render(request,'profile.html',context)

import uuid
def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not NewUser.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forgot_password')
            user_obj = NewUser.objects.get(username = username)
            id = user_obj.id
            print("IDDDDDDDDDDDDDDDDD",id)
            token = str(uuid.uuid4())
            profile_obj= PasswordReset.objects.create(user_id_id = id , forget_password_token=token)

            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/forgot_password')
    except Exception as e:
        print(e)
    return render(request , 'forgot_password.html')

def change_password(request , token):
    context = {}
    try:
        profile_obj = PasswordReset.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')

            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/change-password/{token}/')


            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login/')
    except Exception as e:
        print(e)
    return render(request , 'change_password.html' , context)


def applied_tender(request):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()

    # Get the latest available date for data
    latest_date = APMCTender.objects.latest('created_on').created_on if APMCTender.objects.exists() else date.today()

    # Check for date filter in GET parameters
    filter_date = request.GET.get('date')

    if filter_date:
        try:
            filter_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
            obj_list = APMCTender.objects.filter(created_on=filter_date).order_by('-id')
        except ValueError:
            # Handle invalid date format here
            pass
    else:
        obj_list = APMCTender.objects.filter(created_on=date.today()).order_by('-id')

    paginator = Paginator(obj_list, 10)  # Show 10 objects per page

    # Default to the first page (latest 10 rows)
    page = request.GET.get('page', 1)

    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    context = {
        'obj': obj,
        'default_date': date.today().strftime('%Y-%m-%d'),  # Set the default date
    }

    return render(request, 'applied_tender.html', context)

'''def check_tender_exists(request):
    if request.method == 'POST' and 'tender_id' in request.POST:
        tender_id = request.POST.get('tender_id')

        if APMCETender.objects.filter(tender_id_id=tender_id).exists():
            print("111111111")
            return JsonResponse({'exists': True})
        else:
            return JsonResponse({'exists': False})

    # Return an error response if the request method is not POST or tender_id is not found
    return JsonResponse({'error': 'Invalid request'}, status=400)'''



def submitted_tender(request):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
     # Get the latest available date for data
    latest_date = APMCETender.objects.latest('created_on').created_on if APMCTender.objects.exists() else date.today()

    # Check for date filter in GET parameters
    filter_date = request.GET.get('date')

    if filter_date:
        try:
            filter_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
            obj_list = APMCETender.objects.filter(created_on=filter_date).order_by('-id')
        except ValueError:
            # Handle invalid date format here
            pass
    else:
        obj_list = APMCETender.objects.filter(created_on=date.today()).order_by('-id')

    paginator = Paginator(obj_list, 10)  # Show 10 objects per page

    # Default to the first page (latest 10 rows)
    page = request.GET.get('page', 1)

    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    context = {
        'obj': obj,
        'default_date': date.today().strftime('%Y-%m-%d'),  # Set the default date
    }

    return render(request, 'submitted_tender.html', context)


def operator_tender(request):
    if request.user.user_type != 'operator':
        return HttpResponseForbidden()
    id = request.user.id
    
    user = request.user.first_name
    last = request.user.last_name
    
    # Get the latest available date for data
    latest_date = APMCTender.objects.latest('created_on').created_on if APMCTender.objects.exists() else date.today()

    # Check for date filter in GET parameters
    filter_date = request.GET.get('date')

    if filter_date:
        try:
            filter_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
            obj_list = APMCETender.objects.filter(created_on=filter_date).order_by('-id')
        except ValueError:
            # Handle invalid date format here
            pass
    else:
        obj_list = APMCTender.objects.filter(created_on=date.today()).order_by('-id')

    paginator = Paginator(obj_list, 10)  # Show 10 objects per page

    # Default to the first page (latest 10 rows)
    page = request.GET.get('page', 1)

    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        obj = paginator.page(paginator.num_pages)

    context = {
        'obj': obj,
        'user':user,
        'last':last,
        'default_date': date.today().strftime('%Y-%m-%d'),  # Set the default date
    }

    return render(request, 'operator_tender.html', context)

def get_quality_ranges(request):
    quality_ranges = list(Grades.objects.all().values('quality', 'minimum', 'maximum'))
    return JsonResponse({'quality_ranges': quality_ranges})



from django.urls import reverse

def update_quote(request,id):
    if request.user.user_type != 'admin':
        return HttpResponseForbidden()
    i = id
    print("Iddddddddddddddd",i)
    obj = APMCTender.objects.get(id=i)
    data = APMCETender.objects.filter(tender_id_id=id)
    print(data)
    
    context = {
    'obj':obj
    }
    if request.method == 'POST':
        print("Hiiiiiiiiiiiiiiiiiiiiiiiiii")
        obj.rs = request.POST.get('rs')
        for item in data:
            item.rs = request.POST.get('rs')
            item.save()
        print("!!!!!!!!!!!!!!!!!!!!!!!!1",obj.rs)
        obj.save()  
        return redirect('/applied_tender')
    return render(request,'update_quote.html',context)


def get_grade_range(request):
    selected_quality = request.GET.get('selected_quality')

    if selected_quality:
        try:
            grade = Grades.objects.get(quality=selected_quality)
            return JsonResponse({'minimum': grade.minimum, 'maximum': grade.maximum})
        except Grades.DoesNotExist:
            pass

    return JsonResponse({'error': 'Grade not found'})



#demo
def operator_dashboard(request):

    id = request.user.id
    user = request.user.first_name
    last = request.user.last_name
    unique_qualities = Grades.objects.values_list('quality', flat=True).distinct()
    # Fetches unique values of 'quality' from the Grades model
    if request.method == 'POST':
        select_commodity = request.POST.get('commodity')
        lot_id = request.POST.get('lot_id')
        commission_agent = request.POST.get('commission_agent')
        bags = request.POST.get('bags')
        lot_code = request.POST.get('lot_code')
        quality = request.POST.get('quality')
        quote = request.POST.get('quote')

        tender = APMCTender.objects.create(commodity=select_commodity,lot_id=lot_id,commission_agent=commission_agent,
        Bags=bags,lot_code=lot_code,quality=quality,rs=quote,operator_id_id=id)


    # Retrieve initial batch options
    file_path = os.path.join('media', 'assets', 'MasterTestData.xlsx')

# Specify the sheet name using the sheet_name parameter
    data = pd.read_excel(file_path, sheet_name='ReMS_Output')

# Extract unique values from the 'Commodity' column in the 'ReMS_Output' sheet
    batch_options = data['Commodity'].unique().tolist()

    context = {'batch_options': batch_options,'user':user,'last':last,'unique_qualities':unique_qualities}
    return render(request, 'operator_dashboard.html', context)

def get_commission_agent(request):
    selected_batch = request.GET.get('commodity')
    if selected_batch:
        file_path = os.path.join('media', 'assets', 'MasterTestData.xlsx')
        data = pd.read_excel(file_path, sheet_name='ReMS_Output')

        commission_agent_options = data[data['Commodity'] == selected_batch]['Commission_Agent'].unique().tolist()

        return JsonResponse(commission_agent_options, safe=False)
    return JsonResponse([], safe=False)

def get_commission_agent(request):
    selected_batch = request.GET.get('commodity')
    if selected_batch:
        file_path = os.path.join('media', 'assets', 'MasterTestData.xlsx')
        data = pd.read_excel(file_path, sheet_name='ReMS_Output')

        commission_agent_options = data[data['Commodity'] == selected_batch]['Commission_Agent'].unique().tolist()

        return JsonResponse(commission_agent_options, safe=False)
    return JsonResponse([], safe=False)

def get_lot_id(request):
    selected_batch = request.GET.get('commission_agent')
    try:
        if selected_batch:
            file_path = os.path.join('media', 'assets', 'MasterTestData.xlsx')
            data = pd.read_excel(file_path, sheet_name='ReMS_Output')

            # Drop columns you want to exclude
            columns_to_exclude = ['Last Price', 'Message']
            data_cleaned = data.drop(columns=columns_to_exclude, errors='ignore')

        # Replace NaN values with 'null'
            data_cleaned = data_cleaned.where(pd.notna(data_cleaned), 'null')

            selected_rows = data_cleaned[data_cleaned['Commission_Agent'] == selected_batch].to_dict(orient='records')
     
            print(selected_rows)
            # Fetch grades data for all qualities
            grades_data = Grades.objects.values('quality', 'minimum', 'maximum')

            quality_options = [grade['quality'] for grade in grades_data]

            # Create a dictionary to map quality to its corresponding minimum and maximum values
            quality_info = {grade['quality']: {'minimum': grade['minimum'], 'maximum': grade['maximum']} for grade in grades_data}

            return JsonResponse({'selected_rows': selected_rows, 'grades': list(grades_data), 'quality_info': quality_info, 'quality_options': quality_options}, safe=False)
    except Exception as e:
        print(f"Error in get_lot_id view: {e}")
    return JsonResponse([], safe=False)

from django.views.decorators.http import require_POST
@require_POST
def submit_all_data(request):
    try:
        operator_id = request.user.id
        print("heloooooooooo")
        # Parse the JSON data from the request
        submitted_data = json.loads(request.body)
        print(submitted_data)

        # Iterate through the submitted data and create APMCTender objects
        for data_row in submitted_data:
            APMCTender.objects.create(
                commodity=data_row.get('Commodity', ''),
                commission_agent=data_row.get('Commission_Agent', ''),
                lot_id=data_row.get('Lot ID', ''),
                Bags=data_row.get('Bags', 0),
                lot_code=data_row.get('Lot_Code', ''),
                quality=data_row.get('Quality', ''),
                rs=data_row.get('Quote (Rs./UOM)', 0),
                operator_id_id=operator_id,  # Replace with actual operator ID logic
                # Assuming created_on is automatically set to the current date
            )

        # Return a success response
        return JsonResponse({'status': 'success'})
    except Exception as e:
        # Return an error response if there is any issue
        return JsonResponse({'status': 'error', 'message': str(e)})


def get_details(request):
    selected_batch = request.GET.get('lot_id')
    if selected_batch:
        file_path = os.path.join('media', 'assets', 'MasterTestData.xlsx')
        data = pd.read_excel(file_path, sheet_name='ReMS_Output')

        selected_row = data[data['Lot ID'] == selected_batch].copy()

        selected_row['Commission_Agent'] = selected_row['Commission_Agent'].astype(str)
        selected_row['Bags'] = selected_row['Bags'].astype(str)
        selected_row['Lot_Code'] = selected_row['Lot_Code'].astype(str)

            # Access 'Commission Agent', 'Bags', and 'Lot Code' values from the selected row
        commission_agent = selected_row['Commission_Agent'].iloc[0]
        bags = selected_row['Bags'].iloc[0]
        lot_code = selected_row['Lot_Code'].iloc[0]
        response_data = {
            'Commission Agent': commission_agent,
            'Bags': bags,
            'Lot Code': lot_code
        }
        print(response_data)

        return JsonResponse(response_data)
    return JsonResponse({})


from django.shortcuts import get_object_or_404
def submit_row(request, row_id):
    submitted_row = get_object_or_404(APMCTender, id=row_id)

    # Check if a row with the same tender_id exists
    existing_row = APMCETender.objects.filter(tender_id_id=submitted_row.id).exists()

    if existing_row:
        # If a duplicate row exists, return the 'duplicateExists' flag as True
        return JsonResponse({'duplicateExists': True})
    else:
        # If no duplicate row exists, create a new row and return its details
        new_row = APMCETender.objects.create(
            commodity=submitted_row.commodity,
            commission_agent=submitted_row.commission_agent,
            lot_id=submitted_row.lot_id,
            Bags=submitted_row.Bags,
            lot_code=submitted_row.lot_code,
            quality=submitted_row.quality,
            rs=submitted_row.rs,
            operator_id_id=submitted_row.operator_id_id,
            tender_id_id=submitted_row.id
        )

        # Return the newly created row data
        return JsonResponse({
            'nonduplicate': {
                'id': new_row.id,  # Example: Return the new row's ID
                'commodity': new_row.commodity,
                'commission_agent':new_row.commission_agent,
                'lot_id':new_row.lot_id,
                'Bags':new_row.Bags,
                'lot_code':new_row.lot_code,
                'quality':new_row.quality,
                'rs':new_row.rs,
                'operator_id_id':new_row.operator_id_id,
                'tender_id_id':new_row.tender_id_id  # Include other fields you want to return
                # Add other fields as needed
            }
        })


def submit_all_rows(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        rows = data.get('rows', [])
        print("!!!!!!!!!",rows)

        response_data = []
        rows_added = False  # Flag to check if new rows were added

        for row in rows:
            tender_id = row['tender_id']

            existing_row = APMCETender.objects.filter(tender_id_id=tender_id).exists()

            if existing_row:
                response_data.append({
                    'message': f"Row with tender_id_id {tender_id} already exists. Skipped.",
                    'data': row
                })
                continue

            try:
                new_row = APMCETender.objects.create(
                    commodity=row['commodity'],
                    commission_agent=row['commission_agent'],
                    lot_id=row['lot_id'],
                    rs=row['rs'],
                    Bags=row['bags'],
                    lot_code=row['lot_code'],
                    quality=row['quality'],
                    tender_id_id=tender_id,
                    operator_id_id=row['operator_id']
                )
                response_data.append({
                    'message': f"Row with tender_id_id {tender_id} created successfully.",
                    'data': row
                })
                rows_added = True  # Set the flag if a row was successfully added
            except IntegrityError as e:
                response_data.append({
                    'message': f"Error creating row with tender_id_id {tender_id}: {str(e)}",
                    'data': row
                })

        if rows_added:
            # Trigger the Selenium process as new rows were added
            # Call your Selenium function here or set a flag to do it in the response
            response_data.append({
                'message': 'Selenium process triggered for new rows.'
            })

        return JsonResponse({'response_data': response_data})