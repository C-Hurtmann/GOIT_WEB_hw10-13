from django.forms.models import BaseModelForm
from django.http import HttpResponse


class SetUserToModelMixin:
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)