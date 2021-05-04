# django
from rest_framework import response, status
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q

# apps
from alerts import models as alerts_models
from currencies import models as currencies_models

# python
import requests


def sync():
    alerts_qs = alerts_models.Alert.objects.filter(
        Q(is_completed=False) &
        Q(is_active=True)
    )

    if not alerts_qs.exists():
        print({"message": "No Alerts Scheduled."}, status.HTTP_200_OK)

    URL = "https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates"
    res = requests.get(URL)

    if res.status_code != 200:
        print({"message": "NOT OK"}, status.HTTP_503_SERVICE_UNAVAILABLE)

    data = res.json()

    currencies = currencies_models.Currency.objects.filter(
        is_active=True).values_list("code", flat=True)

    currencies = [x.lower() for x in currencies]

    data = {k: v for (k, v) in data.items() if k in currencies}

    stack = []

    for _ in alerts_qs:
        currency = data.get(str(_.currency).lower())
        price = currency.get(str(_.price_in).lower(), None)
        if not price:
            continue

        if _.above_or_below == 'Above':
            if float(price) > _.price:
                stack.append({
                    "alert": _,
                    "price": float(price)
                })
        else:
            if float(price) < _.price:
                stack.append({
                    "alert": _,
                    "price": float(price)
                })

    print(stack)

    if not stack:
        print({"message": "No Alerts to send."}, status.HTTP_200_OK)

    stack_item = stack[0]
    alert = stack_item.get("alert")
    price = stack_item.get("price")

    subject = f"[ALERT] {str(alert.currency).upper()} value {'Increased' if alert.above_or_below == 'Above' else 'Decreased'}."
    message = f'''{str(alert.currency).upper()}'s current value is {str(alert.price_in).upper()} {price}. You can {'Sell' if alert.above_or_below == 'Above' else 'Buy'}.'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['joshirajesh448@gmail.com']
    try:
        send_mail(subject, message, email_from, recipient_list)
        alert.is_completed = True
        alert.save()
    except:
        pass
    print({"message": "Alert Sent"}, status.HTTP_200_OK)

sync()
