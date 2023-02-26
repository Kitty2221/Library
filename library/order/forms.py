from django import forms
from authentication.models import CustomUser
from book.models import Book
from order.models import Order


class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class OrderForm(forms.ModelForm):
    end_at = forms.DateTimeField(widget=DateInput)
    plated_end_at = forms.DateTimeField(widget=DateInput)


    class Meta:
        model = Order
        Book.__str__ = lambda self: f"{self.name}"
        CustomUser.__str__ = lambda self: f"{self.first_name} {self.last_name}"
        fields = ('book', 'user', 'plated_end_at', 'end_at')
