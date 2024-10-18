# Section 3: Regions & AZ

## AWS Global Infrastucture
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

## AWS Regions 
A region is a cluster of data centers
How to choose an AWS Region?
- Compliance with data governance and legal requirements: data never leaves a region without your explicit permission.
- Proximity to customers: reduced latency
- Available services within a Region
- Pricing: pricing varies region to region

## AWS Availability Zones
Each region has many zones, min is 3, max is 6
Each availability Zone (AZ) is one or more discrete data centers with redundant power, networking and connectiviy. They are isolated from disasters.

## AWS Points of Presence (Edge Locations)
These PoPs host Amazon CloudFront, a content delivery network (CDN); Amazon Route 53, a public Domain Name System (DNS) resolution service; and AWS Global Accelerator (AGA), an edge networking optimization service. 