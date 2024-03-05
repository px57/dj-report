

from django.utils import timezone
import os

from report.rules.stack import REPORT_RULESTACK


from kernel.interfaces.interfaces import InterfaceManager

import PIL

class DefaultReportRule(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    def db_load_all(self):
        """
        Load all the report templates.
        """
        from report.models import ReportTemplate
        return ReportTemplate.objects.filter(
            interface=self.label,
        )


REPORT_RULESTACK.set_rule(DefaultReportRule)