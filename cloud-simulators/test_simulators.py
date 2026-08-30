from aws_simulator import AWSSimulator
from azure_simulator import AzureSimulator
from gcp_simulator import GCPSimulator


aws = AWSSimulator()
azure = AzureSimulator()
gcp = GCPSimulator()


print("\nAWS")
print(aws.get_metrics())

print("\nAzure")
print(azure.get_metrics())

print("\nGCP")
print(gcp.get_metrics())