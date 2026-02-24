# Regions & AZ

## AWS Global Infrastucture
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

## AWS Regions 
- A region is a cluster of data centers
- 22 current regions
- How to choose an AWS Region?
    - Compliance with data governance and legal requirements: data never leaves a region without your explicit permission.
    - Proximity to customers: reduced latency
    - Available services within a Region
    - Pricing: pricing varies region to region

- Data Repication accross Regions is controlled by you
- Communication between Regions uses AWS backbone network infrastructure

## AWS Availability Zones
- A region typically consists of two or more AZ
- Each region has many zones, min is 3, max is 6
- Each availability Zone (AZ) is one or more discrete data centers with redundant power, networking and connectiviy. 
- They are isolated from disasters.

## AWS Points of Presence (Edge Locations)
Points of Presence (PoPs) are AWS data centers located in large population centers around the world, outside of the main AWS Regions. Their main function is to bring AWS content and services closer to your users, functioning as a capillary distribution network.

They are divided into two types of infrastructure:
- **Edge Locations**: These are small, highly distributed data centers designed for low-latency tasks.
- **Regional Edge Caches**: Mid-level data centers that store content that is not frequent enough to be in an Edge Location, but needs to be closer than the home Region.

How do they benefit?
- **Acceleration with Amazon CloudFront (CDN)**
If your contract system needs to serve heavy PDF documents to users in different cities, CloudFront uses Edge Locations to cache those files.
    - Result: A user in Bogotá downloads the contract from a local server in their city, rather than traveling to the Virginia Region (us-east-1).
- **Security with AWS WAF and Shield**
Edge Locations are the first line of defense. Services such as AWS WAF (Web Application Firewall) inspect traffic at the “edge” before it even reaches your instances or EKS clusters.
- **AWS Global Accelerator**
This service uses the AWS backbone to direct your users' traffic to the nearest Edge Location. This prevents traffic from passing through multiple hops on the public internet, reducing jitter and latency.

## AWS Infrastructure features
- Elasticiy and scalability
- Fault tolerance
- High availability
