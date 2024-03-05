

from django.shortcuts import render

from kernel.http import load_response

from report.rules.stack import REPORT_RULESTACK

from kernel.i18n.models import translateDBQuerySet

@load_response(stack=REPORT_RULESTACK)
def load_all(request, res=None):
    """
    Load all the reports.

    Args:
        request: the request object
        res: the response object
    """
    _in = res.get_interface()
    dbReportTemplates = _in.db_load_all()
    res.report_list = [
        report.serialize(request)
        for report in translateDBQuerySet(
            request=request,
            querySet=dbReportTemplates,
        )
    ]
    return res.success()

@load_response(stack=REPORT_RULESTACK)
def send_one(request, res=None):
    """
    Send the report.

    Args:
        request: the request object
        res: the response object
    """
    print (res.success())
    return res.success()


@load_response(stack=REPORT_RULESTACK)
def send_multiple(request, res=None):
    """
    Send multiple reports.

    Args:
        request: the request object
        res: the response object
    """
    print (res.success())
    return res.success()