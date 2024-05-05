#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_cloudformation.cdk_stack import CdkCloudFormationStack

app = cdk.App()
CdkCloudFormationStack(app, "CdkCloudFormationStack")
app.synth()
