"""
pygluu.kubernetes.terminal.aws
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains helpers to interact with user's inputs for aws terminal prompts.

License terms and conditions for Gluu Cloud Native Edition:
https://www.apache.org/licenses/LICENSE-2.0
"""
import click

from pygluu.kubernetes.helpers import get_logger
from pygluu.kubernetes.terminal.helpers import confirm_yesno

logger = get_logger("gluu-prompt-aws    ")


class PromptAws:
    """Prompt is used for prompting users for input used in deploying Gluu.
    """

    def __init__(self, settings):
        self.settings = settings

    def prompt_aws_lb(self):
        """Prompts for AWS Load balancer information
        """
        lb_map = {
            1: "clb",
            2: "nlb",
            3: "alb",
        }

        if self.settings.get("AWS_LB_TYPE") not in lb_map.values():
            print("|-----------------------------------------------------------------------------|")
            print("|                     AWS Loadbalancer type                                   |")
            print("|-----------------------------------------------------------------------------|")
            print("| [1] Classic Load Balancer (CLB) [default]                                   |")
            print("| [2] Network Load Balancer (NLB - Alpha) -- Static IP                        |")
            print("| [3] Application Load Balancer (ALB - Alpha) DEV_ONLY                        |")
            print("| [ALB] Waiting for URL rewrite support by ALB controller                     |")
            print("| https://github.com/kubernetes-sigs/aws-load-balancer-controller/issues/1571 |")
            print("|-----------------------------------------------------------------------------|")

            choice = click.prompt("Loadbalancer type", default=1)
            self.settings.set("AWS_LB_TYPE", lb_map.get(choice, "clb"))
            if self.settings.get("AWS_LB_TYPE") == "alb":
                logger.info("A prompt later during installation will appear to input the ALB DNS address")

        if not self.settings.get("USE_ARN"):
            self.settings.set("USE_ARN", confirm_yesno(
                "Are you terminating SSL traffic at LB and using certificate from AWS"))

        if not self.settings.get("VPC_CIDR") and self.settings.get("USE_ARN") == "Y":
            self.settings.set("AWS_VPC_CIDR", click.prompt(
                "Enter VPC CIDR in use for the Kubernetes cluster i.e 192.168.1.1/16", default="0.0.0.0/0"
            ))

        if not self.settings.get("ARN_AWS_IAM") and self.settings.get("USE_ARN") == "Y":
            # no default means it will try to prompt in loop until user inputs
            self.settings.set("ARN_AWS_IAM", click.prompt(
                "Enter aws-load-balancer-ssl-cert arn quoted ('arn:aws:acm:us-west-2:XXXXXXXX:"
                "certificate/XXXXXX-XXXXXXX-XXXXXXX-XXXXXXXX')"
            ))
