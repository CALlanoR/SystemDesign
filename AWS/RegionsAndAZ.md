# Section 3: Regions & AZ

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
These PoPs host Amazon CloudFront, a content delivery network (CDN); Amazon Route 53, a public Domain Name System (DNS) resolution service; and AWS Global Accelerator (AGA), an edge networking optimization service.

## AWS Infrastructure features
- Elasticiy and scalability
- Fault tolerance
- High availability
