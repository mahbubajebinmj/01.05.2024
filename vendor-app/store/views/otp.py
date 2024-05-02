from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer

class Otp(View):
    def get(self, request):
        return render(request, 'otp.html')
    
    def post(self, request):
        entered_otp = request.POST.get('otp')
        customer_id = request.session.get('customer_id')
        
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
            if customer.otp == entered_otp:
                # OTP is correct, mark email as verified
                customer.email_verified = True
                customer.save()
                # Redirect to success page or any other page
                return redirect('homepage')
        
        error_message = 'Invalid OTP. Please try again.'
        return render(request, 'otp.html', {'error': error_message})
