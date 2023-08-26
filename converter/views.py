from .models import Conversion
from django.shortcuts import render
import requests
def convert_currency(request):
    if request.method == 'POST':
        base_currency = request.POST.get('base_currency')
        target_currency = request.POST.get('target_currency')
        amount = request.POST.get('amount')

        try:
            float_amount = float(amount)
        except ValueError:
            return render(request, 'converter/index.html', {'error': 'Please enter a number'})

        url = f'https://v6.exchangerate-api.com/v6/2c985527a9f1435a54deebde/latest/{base_currency}'
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            conversion_rate = data['conversion_rates'].get(target_currency)
            if conversion_rate is None:
                return render(request, 'converter/index.html', {'error': 'Invalid target currency'})

            converted_amount = float_amount * conversion_rate
            context = {
                'base_currency': base_currency,
                'target_currency': target_currency,
                'amount': float_amount,
                'converted_amount': converted_amount,
            }

            # Save the conversion history to the database
            Conversion.objects.create(
                base_currency=base_currency,
                target_currency=target_currency,
                amount=float_amount,
                converted_amount=converted_amount
            )

            return render(request, 'converter/index.html', context)

    return render(request, 'converter/index.html')
