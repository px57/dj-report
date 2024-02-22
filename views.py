from django.shortcuts import render
from kernel.http import Response

def load_all(request):
    """
    Load all the reports. 
    """
    res = Response()
    # -> Load the report templates.
    return res