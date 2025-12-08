# Networking basics
- A network can be logically partitioned into subnets.

## IP addresses
    - The IP address is 192.0.2.0. Each of the four dot (.)-separated numbers of the IP
address represents 8 bits in octal number format. That means each of the four numbers can be
anything from 0 to 255. The combined total of the four numbers for an IP address is 32 bits in
binary format.
    - A 32-bit IP address is called an IPv4 address.
    - IPv6 addresses, which are 128 bits, are also available.
    - An IPv6 address is composed of eight groups of four letters and numbers that are separated by
colons (:)
    - Each
of the eight colon-separated groups of the IPv6 address represents 16 bits in hexadecimal
number format (Total 128 bits).

<p align="center">
  <img src="../images/CIDR.png" width="600">
  <br/>
</p>

    - the CIDR address is 192.0.2.0/24. The last number (24) tells you that the first 24
bits must be fixed. The last 8 bits are flexible, which means that 2 8 (or 256) IP addresses are
available for the network, which range from 192.0.2.0 to 192.0.2.255.
    - If the CIDR was 192.0.2.0/16, the last number (16) tells you that the first 16 bits must be fixed.
The last 16 bits are flexible, which means that 216 (or 65,536) IP addresses are available for the
network, ranging from 192.0.0.0 to 192.0.255.255.
    - There are two special cases:
        - Fixed IP addresses, in which every bit is fixed, represent a single IP address (for example,
192.0.2.0/32). This type of address is helpful when you want to set up a firewall rule and give
access to a specific host.
        - The internet, in which every bit is flexible, is represented as 0.0.0.0/0

<p align="center">
  <img src="../images/osi.png" width="600">
  <br/>
</p>

    - The Open Systems Interconnection (OSI) model is a conceptual model that is used to explain how
data travels over a network.
    - It consists of seven layers and shows the common protocols and
addresses that are used to send data at each layer. 
    - hubs and switches work at layer 2 (the data link layer). 
    - Routers work at layer 3 (the network layer).


## VPC
- Amazon Virtual Private Cloud (Amazon VPC) is a service that lets you provision a logically isolated
section of the AWS Cloud (called a virtual private cloud, or VPC) where you can launch your AWS
resources.

<p align="center">
  <img src="../images/vpcandsubnets.png" width="600">
  <br/>
</p>

- When you create a VPC, you assign it to an IPv4 CIDR block (range of private IPv4
addresses).
- You cannot change the address range after you create the VPC.
- The largest IPv4 CIDR block size is /16.
- The smallest IPv4 CIDR block size is /28.
- IPv6 is also supported (with a different block size limit).
- CIDR blocks of subnets cannot overlap.


## Reserved IP addresses
When you create a subnet, it requires its own CIDR block. For each CIDR block that you specify, AWS reserves five IP addresses within that block, and these addresses are not available for use.

<p align="center">
  <img src="../images/reservedips.png" width="600">
  <br/>
</p>

For example, suppose that you create a subnet with an IPv4 CIDR block of 10.0.0.0/24 (which has 256 total IP addresses). The subnet has 256 IP addresses, but only 251 are available because five are reserved.

## Public IP address types
1. Public IPv4 address
    - Automatically assigned through the auto-assign public IP address settings at the subnet level.
2. Elastic IP address
    - An Elastic IP address is a static and public IPv4 address that is designed for dynamic cloud computing. You can associate an Elastic IP address with any instance or network interface for any VPC in your account. With an Elastic IP address, you can mask the failure of an instance by rapidly remapping the address to another instance in your VPC.

## Elastic network interface
- An elastic network interface is a virtual network interface that you can:
    - Attach to an instance.
    - Detach from the instance, and attach to another instance to redirect network traffic.
- Each instance in your VPC has a default network interface that is assigned a private IPv4 address from the IPv4 address range of your VPC.

## Route tables and routes
- A route table contains a set of rules (called routes) that directs network traffic from your subnet.
- Each route specifies a destination and a target. 
    - The destination is the destination CIDR block where you want traffic from your subnet to go. 
    - The target is the target that the destination traffic is sent through. 
    - By default, every route table that you create contains a local route for communication in the VPC.
- Each subnet in your VPC must be associated with a route table. The main route table is the route
table is automatically assigned to your VPC.


# VPC Networking
## Internet gateway
- An internet gateway is a scalable, redundant, and highly available VPC component that allows
communication between instances in your VPC and the internet.
- Two purposes
    1. to provide a target in your VPC route tables for internet-routable traffic, 
    2. to perform network address translation for instances that were assigned public IPv4 addresses.
- To make a subnet public, you attach an internet gateway to your VPC and add a route to the route
table to send non-local traffic through the internet gateway to the internet (0.0.0.0/0).

<p align="center">
  <img src="../images/internetgateway.png" width="600">
  <br/>
</p>

## Network address translation (NAT) gateway
- A network address translation (NAT) gateway enables instances in a private subnet to connect to
the internet or other AWS services, but prevents the internet from initiating a connection with
those instances.

<p align="center">
  <img src="../images/natgateway.png" width="600">
  <br/>
</p>

- To create a NAT gateway: 
    1. you must specify the public subnet in which the NAT gateway should reside.
    2. You must also specify an Elastic IP address to associate with the NAT gateway when you
create it. 
    3. After you create a NAT gateway, you must update the route table that is associated with
one or more of your private subnets to point internet-bound traffic to the NAT gateway. 
    4. Thus, instances in your private subnets can communicate with the internet.

## VPC Sharing
- VPC sharing enables customers to share subnets with other AWS accounts in the same
organization in AWS Organizations.
- In this model, the account that owns the VPC (owner) shares one or
more subnets with other accounts (participants) that belong to the same organization in AWS
Organizations. 
- After a subnet is shared, the participants can view, create, modify, and delete their
application resources in the subnets that are shared with them. 
- Participants cannot view, modify,
or delete resources that belong to other participants or the VPC owner.

## VPC Peering
- A VPC peering connection is a networking connection between two VPCs that enables you to
route traffic between them privately.

<p align="center">
  <img src="../images/vpcpeering.png" width="600">
  <br/>
</p>

When you set up the peering connection, you create rules in your route table to allow the VPCs
to communicate with each other through the peering resource. For example, suppose that you
have two VPCs.

## AWS Site-to-Site VPN
By default, an instance that you launch within an Amazon VPC can't communicate with a local (AWS Cloud) network and a remote device — for example, this might be a site or an on-premises device. You can enable access to your remote devices from your VPC by creating an AWS Site-to-Site VPN (Site-to-Site VPN) connection, and configuring routing to pass traffic through the connection.


<p align="center">
  <img src="../images/sitetositevpn.png" width="600">
  <br/>
</p>

## AWS Direct Connect
One of the challenges of network communication is network performance. Performance can be
negatively affected if your data center is located far away from your AWS Region. For such
situations, AWS offers AWS Direct Connect, or DX. AWS Direct Connect enables you to establish a
dedicated, private network connection between your network and one of the DX locations. This
private connection can reduce your network costs, increase bandwidth throughput, and provide a
more consistent network experience than internet-based connections. DX uses open standard
802.1q virtual local area networks (VLANs).

<p align="center">
  <img src="../images/awsdirectconnect.png" width="600">
  <br/>
</p>

## VPC Endpoints
A VPC endpoint is a virtual device that enables you to privately connect your VPC to supported
AWS services and VPC endpoint services that are powered by AWS PrivateLink. Connection to
these services does not require an internet gateway, NAT device, VPN connection, or AWS Direct
Connect connection. Instances in your VPC do not require public IP addresses to communicate
with resources in the service. Traffic between your VPC and the other service does not leave the
Amazon network.

<p align="center">
  <img src="../images/vpcendpoints.png" width="600">
  <br/>
</p>
