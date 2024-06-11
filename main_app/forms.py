from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
  # * meta is used to give information about the form. though not necessary, it helps eliminate extra code
  # putting it here as Meta would still be necessary in order to define the model used for this form.
  # without meta there, we would need to write the below not stored in fields but each to their own respective variable
  # date = forms.DateField() meal = forms.CharField() and then class Meta below but still within the feedingClass
  # and a variable called model within it storing Feeding referencing to the feeding model
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

