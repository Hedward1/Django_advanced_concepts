from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Member, Feature
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['members'] = Member.objects.order_by('?').all()
        context['features'] = Feature.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Email not sent')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
