#!/usr/bin/env python
"""
Provides outcome group and outcome value classes for SSVC.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

from pydantic import BaseModel

from ssvc._mixins import _Base, _Keyed, _Versioned


class OutcomeValue(_Base, _Keyed, BaseModel):
    """
    Models a single value option for an SSVC outcome.
    """


class OutcomeGroup(_Base, _Versioned, BaseModel):
    """
    Models an outcome group.
    """

    outcomes: list[OutcomeValue]

    def __iter__(self):
        """
        Allow iteration over the outcomes in the group.
        """
        return iter(self.outcomes)

    def __len__(self):
        """
        Allow len() to be called on the group.
        """
        olist = list(self.outcomes)
        l = len(olist)
        return l

    # register all instances
