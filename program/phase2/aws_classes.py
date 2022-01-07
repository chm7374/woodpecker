# EC2 Instance data
class AWSInstance:
    def __init__( self, instanceId, keyName, imageId, avZone, monState, pubIP, pubDNS, subnetId, vpcId, iamRole, SGs):
        # ID of the ec2 instance
        self.instanceId = instanceId
        # Keyname used to access instance
        self.keyName = keyName 
        # ImageId used for the instance
        self.imageId = imageId 
        # Avaliability zone
        self.avZone = avZone
        # Monitoring state
        self.monState = monState
        # Public IP
        self.pubIP = pubIP
        # Public DNS
        self.pubDNS = pubDNS
        # Subnet ID
        self.subnetId = subnetId
        # VPC ID
        self.vpcId = vpcId 
        # IAM Role (class)
        self.iamRole = iamRole
        # Security Groups (array of classes)
        self.SGs = SGs
    def getInstanceId(self):
            return self.instanceId
    def getKeyName(self):
            return self.keyName 
    def getImageId(self):
            return self.imageId 
    def getAvZone(self):
            return self.avZone
    def getMonState(self):
            return self.monState
    def getPubIP(self):
            return self.pubIP
    def getPubDNS(self):
            return self.pubDNS
    def getSubnetId(self):
            return self.subnetId
    def getVpcId(self):
            return self.vpcId 
    def getIamRole(self):
            return self.iamRole
    def getSGs(self):
            return self.SGs
    def __str__(self):
            return str(self.__class__) + ": " + str(self.__dict__)


class IamRole:
    def __init__( self, roleName, iamArn, iamPolicies):
        # IAM role name
        self.roleName = roleName
        self.iamArn = iamArn
        # Array of IAM policies attached to the role
        self.iamPolicies = iamPolicies
    def getRoleName(self):
        return self.roleName
    def getIamArn(self):
        return self.iamArn
    def getIamPolicies(self):
        return self.iamPolicies
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class IamPolicy:
    def __init__( self, policyName, policyArn, versionId, permissions):
        self.policyName = policyName
        self.policyArn = policyArn
        self.versionId = versionId
        # array of IAM policy permissions
        self.permissions = permissions
    def getPolicyName(self):
        return self.policyName
    def getPolicyArn(self):
        return self.policyArn
    def getVersionId(self):
        return self.versionId
    def getPermissions(self):
        return self.permissions
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class IamStatement:
    def __init__( self, effect, actions, resource):
        self.effect = effect
        # array of iam rules
        self.actions = actions
        self.resource = resource
    def getEffect(self):
        return self.effect
    def getActions(self):
        return self.actions
    def getResource(self):
        return self.resource
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Sg:
    def __init__( self, groupId, groupName, ownerId, vpcId, ipPermissions ):
        self.groupId = groupId
        self.groupName = groupName
        self.ownerId = ownerId
        self.vpcId = vpcId
        # array of ip permissions
        self.ipPermissions = ipPermissions
    def getGroupId(self):
        return self.groupId
    def getGroupName(self):
        return self.groupName
    def getOwnerId(self):
        return self.ownerId
    def getVpcId(self):
        return self.vpcId
    def getIpPermissions(self):
        return self.ipPermissions
    def __str__(self):
            return str(self.__class__) + ": " + str(self.__dict__)


class SgIpPermissions:
    def __init__( self, inOrOut, toPort, fromPort, cidr, protocol ):
        self.inOrOut = inOrOut
        self.toPort = toPort
        self.fromPort = fromPort
        self.cidr = cidr
        self.protocol = protocol
    def getInOrOut(self):
        return self.inOrOut
    def getToPort(self):
        return self.toPort
    def getFromPort(self):
        return self.fromPort
    def getCird(self):
        return self.cidr
    def getProtocol(self):
        return self.protocol
    def __str__(self):
            return str(self.__class__) + ": " + str(self.__dict__)
        
        
