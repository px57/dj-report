

from django.shortcuts import render

from kernel.http import load_response

from report.rules.stack import REPORT_RULESTACK

@load_response(stack=REPORT_RULESTACK)
def load_all(request, res=None):
    """
    Load all the reports.

    Args:
        request: the request object
        res: the response object
    """
    print (res.success())
    return res.success()