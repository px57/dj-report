

from django.shortcuts import render

from gpm.http.decorators import load_json
from gpm.http import load_response
from gpm.i18n.models import translateDBQuerySet

from report.rules.stack import REPORT_RULESTACK
from report.models import Reported, ReportTemplate

from profiles.decorators import load_profile

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

@load_json
@load_response(stack=REPORT_RULESTACK)
@load_profile
def send_one(request, res=None):
    """
    Send the report.

    Args:
        request: the request object
        res: the response object
    """
    _in = res.get_interface()
    report_id = request.POST.get('report_id', None)
    relatedModelId = request.POST.get('relatedModelId', None)
    if not report_id:
        return res.error('Post.report_id is required')
    
    if not relatedModelId:
        return res.error('Post.relatedModelId is required')
    
    dbReportTemplate = ReportTemplate.objects.filter(id=report_id).first()
    dbReported = Reported.objects.filter(
        relatedModel=_in.relatedModel,
        relatedModelId=relatedModelId
    ).first()

    if not dbReportTemplate:
        return res.error('Report template not found')
    
    if dbReported is None:
        dbReported = Reported(
            profile=request.profile,
            relatedModel=_in.relatedModel,
            relatedModelId=relatedModelId,
        )
        dbReported.save()
    else: 
        dbReported.template = dbReportTemplate
        dbReported.save()
    
    return res.success()


@load_response(stack=REPORT_RULESTACK)
@load_profile
def send_multiple(request, res=None):
    """
    Send multiple reports.

    Args:
        request: the request object
        res: the response object
    """
    print (res.success())
    return res.success()