import os
import traceback

from st2common.runners.base_action import Action
from lib.base import AzureBaseAction

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.compute.models import DiskCreateOption

from msrestazure.azure_exceptions import CloudError

from haikunator import Haikunator


class RestartVM(AzureBaseAction):

    def run(self, group_name, vm_name):

        credentials, subscription_id = self.get_credentials()
        compute_client = ComputeManagementClient(credentials, subscription_id)

        try:
            # Restart the VM
            async_vm_start = compute_client.virtual_machines.start(
                group_name, vm_name)
            result = {"message": vm_name + "VM restart successful"}
        except CloudError:
            result = {"error": "A VM operation failed:\n" + traceback.format_exc()}
        
        return result
