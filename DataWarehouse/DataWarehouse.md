# Data Warehouse
Based on the book "The Data Warehouse Toolkit Third Edition, by Ralph Kimball and Margy Ross.

## Different worlds of Data Capture and Data Analysis
- Operational systems  are optimized to process transactions quickly, this kind of system:
    - Tipically  do not mantain history
    - Update data to reflect the most current state

- DW/BI system on the other hand  worry about whether operational processes are working correctly.
    - Demand historical context be preserved to accurately evaluate the organizations's performance over time.

## Goals of Data Warehousing and Business Intelligence
    - The DW/BI system must make information easily accessible
        - Data must be intuitive
        - The data's structures and labels should mimic the business users' thought process and vocabulary.
    - The DW/BI system must present information consistently
        - Data must be credible
        - Data must be carefully assembled from a variety of sources, cleansed, quality assured, and release only when it is fit for user consumption.
    - The DW/BI system must adapt to change
        -  The DW/BI system must be designed to handle the invevitable change gracefully so that it doesn't invalidate date existing data or applications.
    - The DW/BI system must present information in a timely way.
    - The DW/BI system must be a secure bastion that protects the information assets
    - The DW/BI system must serve as the authoritative and trustworthy foundation for improved decision making.

## DW/BI manager responsabilities
    - Understand  the business users
        - Understand their job responsabilities, goals and objetives
        - Determine the decisions that the business users want to make with the help of the DW/BI system
        - Identify the "best" users who make effective, high-impact decisions.
    - Deliver high-quality, relevant and accesible information and analytics to the business users
        - Choose tthe most robust, actionable data to present in the DW/BI
        - Continously monitor the accuracy of the data and analyses
        - Adapt to changing user profiles, requirements, and business priorities along with the availability of new data sources.
    - Sustain the DW/BI environment
        - Using the success of the DW/BI to justify staffing and ongoing expenditures
        - Update the DW/BI system on a regular basis
        - Maintain the business users' trust
        - Keep the business users, executive sponsors and IT  management happy

## Dimensional Modeling introduction
### Fact tables for Measurements
- The fact table in a dimensional model stores the performance measurements resulting from an organization's business process events.
- The term fact represents a business measure.
- The designer should make very effort to put textual data into dimensions where they can be correlated more effectively with the other textual
dimension attributes and consume mush less space.
- You should not store redundant textual information in fact tables. Unless the text is unique for every row in the fact table, it belongs in the dimension table.
- Fact tables tend to be deep in terms of the number of rows, but narrow  in terms of the numbers of columns.
- Fact tables categories:
    1. Transaction
    2. Periodic snapshot
    3. Accumulating snapshot
- All fact tables have two or more foreign key that connect to the dimension tables primary keys.
- The fact table generally has its own primary key composed of a subset of the foreign keys. This key is often called a composite key.

### Dimension tables for Descriptive Context
- Dimension tables are integral companions to a fact table. 
- The dimension tables contain the textual context associated with a business process measurement event.
- They describe the "who, what, where, how and why" associated with the event.
- Dimension tables often have many columns or attributes (50 to 100 attributes)
- Dimension tables tend to have fewer rows than fact tables, but can be wide with many large text columns.
- Each dimension table is defined by a single primary key.
- Dimension attributes are critical to making the DW/BI system usable and understandable.
- Attributes should consist of real words rather than cryptic abbreviations.
- The DW is only as good as the dimension attributes
- Dimension tables often represent hierarchical relationships. 

**Note**:
The designer's dilema of whether a numeric quantity is a fact or a dimension attribute is rarely a difficult decision. Continuously valued numeric observations are almost always facts; discrete numeric observations drawn from a small list are almost always dimension attributes.