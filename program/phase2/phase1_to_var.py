import subprocess as sp
import os
from aws_classes import *


def makeAWSInstance( instanceId ):
    # Create the class with default params
    ec2 = AWSInstance(instanceId, "null", "null", "null", "null", "null", "null", "null", "null", "null", "null")
    # Keyname used to access instance
    ec2.keyName = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query Reservations[*].Instances[*].[KeyName] --output text")
    # ImageId
    ec2.imageId = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query Reservations[*].Instances[*].[ImageId] --output text >> $line.txt")
    # Avaliability zone
    ec2.avZone = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query 'Reservations[*].Instances[*].[Placement.AvailabilityZone]' --output text")
    # Monitoring state
    ec2.monState = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query 'Reservations[*].Instances[*].[Monitoring.State]' --output text")
    # Public IP
    ec2.pubIP = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query 'Reservations[*].Instances[*].[PublicIpAddress]' --output text")
    # Public DNS
    ec2.pubDNS = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query 'Reservations[*].Instances[*].[PublicDnsName]' --output text")
    # Subnet ID
    ec2.subnetId = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query Reservations[*].Instances[*].[SubnetId] --output text")
    # VPC ID
    ec2.vpcId = sp.getoutput("aws ec2 describe-instances --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query Reservations[*].Instances[*].[VpcId] --output text")
    # Get the IAM instance role profile ARN to get the true IAM Role
    ec2.iamRole = makeIamRole( sp.getoutput("aws ec2 describe-iam-instance-profile-associations --filter Name=instance-id,Values=" + ec2.getInstanceId() + " --query 'IamInstanceProfileAssociations[*].[IamInstanceProfile.Arn]' --output text | cut -c44-") )
    sgs = []
    sgArray = sp.getoutput("aws ec2 describe-security-groups --group-ids $(aws ec2 describe-instances --instance-id " + ec2.getInstanceId() + " --query 'Reservations[].Instances[].SecurityGroups[].GroupId[]' --output text) --query 'SecurityGroups[*].GroupId' --output text")
    for sg in sgArray.split():
        sgs.append( makeSG(sg) )
    ec2.SGs = sgs
    print(ec2)
    
def makeIamRole( instanceProfileRole ):
    iamRoleARN = sp.getoutput("aws iam get-instance-profile --instance-profile-name " + instanceProfileRole + " --query 'InstanceProfile.Roles[*].RoleName' --output text")
    iam = IamRole( iamRoleARN, "null", "null")
    iam.iamArn = sp.getoutput("aws iam list-attached-role-policies --role-name " + iamRoleARN + " --query 'AttachedPolicies[*].PolicyArn' --output text")
    iamPoliciesArray = sp.getoutput("aws iam list-attached-role-policies --role-name " + iamRoleARN + " --query 'AttachedPolicies[*].PolicyArn' --output text")
    iamPolicyArray = []
    print(iamPoliciesArray.split())
    for policy in iamPoliciesArray.split():
        policies = makeIamPolicy(policy)
        iamPolicyArray.append(policies)
    print(iamPolicyArray)
    iam.iamPolicies = iamPolicyArray
    print(iam)
    return iam
        
        
    
def makeIamPolicy( policyArn ):
    policyVersion = sp.getoutput("aws iam get-policy --policy-arn " + policyArn + " --query 'Policy.DefaultVersionId' --output text")
    policyName = sp.getoutput("aws iam get-policy --policy-arn " + policyArn + " --query 'Policy.PolicyName' --output text")
    policy = IamPolicy( policyName, policyArn, policyVersion, "null")
    index = 0
    statementArray = []
    while ( 1 == 1 ):
        statements = sp.getoutput("aws iam get-policy-version --policy-arn " + policyArn + " --version-id " + policyVersion + " --query 'PolicyVersion.Document.Statement[" + str(index) + "].Action' --output text")
        if (statements == "None"):
            policy.permissions = statementArray
            print(policy)
            return policy
        else:
            actionArray = []
            for i in statements.split():
                actionArray.append(i)
            effect = sp.getoutput("aws iam get-policy-version --policy-arn " + policyArn + " --version-id " + policyVersion + " --query 'PolicyVersion.Document.Statement[" + str(index) + "].Effect' --output text")
            resource = sp.getoutput("aws iam get-policy-version --policy-arn " + policyArn + " --version-id " + policyVersion + " --query 'PolicyVersion.Document.Statement[" + str(index) + "].Resource' --output text")
            policyStatement = IamStatement( effect, actionArray, resource)
            statementArray.append(policyStatement)
            index += 1
   
    
def makeSG( groupid ):
    sg = Sg( groupid, "null", "null", "null", "null")
    sg.groupName = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].[GroupName]" --output text')
    sg.ownerId = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].[OwnerId]" --output text')
    sg.vpcId = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].[VpcId]" --output text >> $1')
    index = 0
    rulestArray = []
    while ( 1 == 1 ):
    	rules = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissions[' + str(index) + '].IpRanges[*].CidrIp" --output text')
    	print("rules" + rules)
    	if not rules:
    	    index = 0
    	    print("moving to egress")
    	    while (1 == 1):
    	        rules = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissionsEgress[' + str(index) + '].IpRanges[*].CidrIp" --output text')
    	        print("rules" + rules)
    	        if not rules:
    	            print("done")
    	            sg.ipPermissions = rulestArray
    	            print(sg)
    	            return sg
    	        else:
    	            sgRuleTo = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissionsEgress[' + str(index) + '].ToPort" --output text')
    	            sgRuleFrom = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissionsEgress[' + str(index) + '].FromPort" --output text')
    	            sgRuleProtocol = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissionsEgress[' + str(index) + '].IpProtocol" --output text')
    	            sgPerm = SgIpPermissions( "egress", sgRuleTo, sgRuleFrom, rules, sgRuleProtocol)
    	            print(sgPerm)
    	            rulestArray.append(sgPerm)
    	            index += 1
    	else:
    	    sgRuleTo = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissions[' + str(index) + '].ToPort" --output text')
    	    sgRuleFrom = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissions[' + str(index) + '].FromPort" --output text')
    	    sgRuleProtocol = sp.getoutput('aws ec2 describe-security-groups --filters Name=group-id,Values=' + groupid + ' --query "SecurityGroups[*].IpPermissions[' + str(index) + '].IpProtocol" --output text')
    	    sgPerm = SgIpPermissions( "ingress", sgRuleTo, sgRuleFrom, rules, sgRuleProtocol)
    	    rulestArray.append(sgPerm)
    	    print(sgPerm)
    	    index += 1
       
    
if __name__ == "__main__":
    # First get the iterable list of all the boxes
    os.system("aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId}' --output text > ec2-instance-id.txt")
    with open("ec2-instance-id.txt", "r") as a_file:
        for line in a_file:
            print(line)
            makeAWSInstance( line.strip() )
