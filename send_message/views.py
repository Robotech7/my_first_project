from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .forms import SendMessageForm


class SendMessageView(LoginRequiredMixin, View):
    login_url = 'login_register:login'

    def get(self, request):
        return render(request, 'send_message/send_message.html')

    def post(self, request):
        form = SendMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            author = request.user
            message.author = author
            theme = form.cleaned_data['title']
            text = form.cleaned_data['text']
            receiver = User.objects.get(username='admin').email
            sender_mail = author.email if author.email else f'{author}@none-email.com'
            try:
                send_mail(theme, text, sender_mail, [receiver])
            except Exception as error:
                message.status = 2
                ex_type = type(error).__name__
                ex_text = list(error.args)
                message.error = f'{ex_type}: {ex_text}'
                content = {'data': message.error}
                message.save()
                return JsonResponse(content)
            message.status = 1
            message.save()
            content = {'key': 'yes'}
            return JsonResponse(content)
