from django.shortcuts import render
from .forms import EmailVerifyForm
from validate_email_address import validate_email
import dns.resolver

def verify_email_view(request):
    result = None
    if request.method == 'POST':
        form = EmailVerifyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            result = validate_email(email, verify=True)  # Verify if email exists by querying DNS
            if result:
                result = f"Email '{email}' is valid!"
            else:
                result = f"Email '{email}' is invalid!"
    else:
        form = EmailVerifyForm()

    return render(request, 'verifier/verify.html', {'form': form, 'result': result})

