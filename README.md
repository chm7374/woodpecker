# Woodpecker
![kissclipart-woodpecker-clipart-woodpecker-bird-stock-photograp-1bd8e90eccd4564a](https://user-images.githubusercontent.com/47120650/147968467-2c905451-eabf-4259-986d-c60f09cdb52a.png)


Woodpecker is a program that tests the security groups, IAM roles, and instances on an AWS region of an account. It tests the basic functions of a specified region of ec2 instances an account has as well as its security groups and IAM roles for vulnerabilities and security flaws.
Like a woodpecker, it looks for known "bugs" but does so sort-of loudly. Using a mix of blue and red team tactics, this program uses information about your account and simulates an attack from a hacker, as well as the possible damage one could do if they got into a box or role.
Like woodpeckers, it does so loudly, so it is a good way to see if your security will pick up any attacks or suspicious activity inside and outside of your boxes.
Woodpecker, unlike other kinds of software, will not do anything damaging or compromising to the systems. Its purpose is to show how and where your systems can be used and vulnerable, not actually exploiting it. 

How Woodpecker works:
* It does an internal scan of the region, gathering box data, iam roles, and security groups.
* Using that data, it will then use it to attempt brute force attacks on those boxes, as well as port scans, network data, etc.
* It then will gain access to a box (using provided details) and will begin performing suspicous activity as well as testing what can be accessed if that box was ever able to be breached by a hacker.
* After this a report will be compiled listing all of Woodpecker's actions, and what it was able to discover internally and externally about the boxes.
* You should then compare the report to your aws logs to see if your system detected the malicous/unusual activity.

Goals:
* Are my systems able to withstand the attacks?
* What data is able to be accessed externally?
* Will my systems report the external attacks in the logs?
* If a malicious agent is able to break into a box, what damage can they do?
* If a malicious agent is able to break into a box, will my systems detect their activity?
* If a malicious agent is able to break into a box, can I see it in the logs?
* What vulnerabilities do my security groups and IAM roles have?
* Can my boxes withstand and report both external and internal attacks?
* What security groups and IAM roles need changes for their boxes?

Prerequsites:
* Give woodpecker admin access to the specified region. (specific iam roles will be specified soon)
* Have python installed. (version pending)

Var file:
 * region
 * aws key location
 * woodpecker iam role (all permission role until i find out what roles are specifically needed)

EX) woodpecker.py [var-file]
"welcome to woodpecker! please make sure that the neccisary things are provided in the var file."
scanning box1 [ec2-instance-name]...
scanning box2 [ec2-instance-name]...
scanning box3 [ec2-instance-name]...
Reports succeded successfully! Reports saved as [ec2-instance-name].txt

ec2-instance-name.txt
Woodpecker report errors:
- sg (name) is open to the public
- iam (name) has unnessicarry permissions
- box uses default passwords
- box is open to brute force attacks
- box can be port scanned
- box produces network information
 
What to scan:
SG:
* Is the IP open to the public
* What ports are open
* No egress cidr blocks
* if vpc hosts any vulnerable systems (puts stable ones at risk)
* repeated use of same sg on different systems
IAM:
* Unneccissary iam permissions
* user escillation
* use of defaults on multiple systems
Box:
* open ports
* known ami vulnerabilities
* open to port scanning?
* open to btye overload attack?
* Easy-to-guess passwords for users
* no limit to password guesses
* no notification of multiple failures
* internal firewalls
* vpc vulnerabilities
* repeated copies of same system (domino effect if one is ever cracked)
* escillation of user permissions
* other
* no monitoring enabled

How the tool will work:
blue team: internal scan
feeds into red team brute force
IF red team breaks in, what can they do/do i see it in the logs?
What damage can they do IF they break in & can I see it in the logs
No damage actually done to infrastructure (What If? through ssm agent)

Things to investigate:
* chaosmonkey
* cloudcustodian
* tfscan
* atomic-red-team

