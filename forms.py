
from django import forms

class ReportSendOneForm(forms.Form):
    """
    The report send one form.
    """
    report_id = forms.CharField(
        required=True,
        max_length=100,
    )

    