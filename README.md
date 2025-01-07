### Overview
## Kimball

### The numeric measures in a fact table fall into three categories. The most fl exible and
    useful facts are fully additive; additive measures can be summed across any of the
    dimensions associated with the fact table. Semi-additive measures can be summed
    across some dimensions, but not all; balance amounts are common semi-additive facts
    because they are additive across all dimensions except time. Finally, some measures
    are completely non-additive, such as ratios. A good approach for non-additive facts is,
    where possible, to store the fully additive components of the non-additive measure
    and sum these components into the fi nal answer set before calculating the fi nal
    non-additive fact. This fi nal calculation is often done in the BI layer or OLAP cube.


### Null-valued measurements behave gracefully in fact tables. The aggregate functions
(SUM, COUNT, MIN, MAX, and AVG) all do the “right thing” with null facts. However,
nulls must be avoided in the fact table’s foreign keys because these nulls would
automatically cause a referential integrity violation. Rather than a null foreign key,
the associated dimension table must have a default row (and surrogate key) repre-
senting the unknown or not applicable condition.
## The goal of this ELT pipeline is to extract data from a relationnal database source Passing through a message broker and then load it in an HDFS file system in order to be analyzed by a Bi/Data analyst in order to gain insights on the market related to the data beeing processed

# The term fact represents a business measure. Imagine standing in the marketplace watching products being sold and writing down the unit quantity and dollar sales amount for each product in each sales transaction. Based on this definition from "The datawarehouse toolkit" : The term fact represents a business measure. Imagine standing in the marketplace watching products being sold and writing down the unit quantity and dollar sales amount for each product in each sales transaction, I choose to organise data on the lakehouse as follows:

## The idea that a measurement event in the physical world has a one-to-one relationship to a single row in the corresponding fact table is a bedrock principle for dimensional modeling. Everything else builds from this foundation.

#### All fact tables have two or more foreign keys that connect to the dimension tables primary keys Here are a listing of those foreign keys: 
- Fact table: Booking

#### Based on this definition of dimension table from "The datawarehouse toolkit" Dimension tables are integral companions to a fact table. The dimension tables contain the textual context associated with a business process measurement event. They
#### describe the “who, what, where, when, how, and why” associated with the event.
#### If you want to identify a dimension look at this definition: . In a query or report request, attributes are identified as the BY words. For example, when a user wants to see dollar sales by brand, brand mustbe available as a dimension attribute.
- Dimensional tables: passenger, airport, airline ... 
- 1
- 2
- 3
- 4
- 5
- 6


Step 1: The first step in the design is to decide what business process to model by combin-ing an understanding of the business requirements with an understanding of the available source data.In our retail case study, management wants to better understand customer pur- chases as captured by the POS system

Step 2: What level of data detail should be made available in the dimensional model?

Step 3: Identify the Dimensions

Step 4: Identify the Facts
The fourth and fi nal step in the design is to make a careful determination of which
facts will appear in the fact table

Percentages and ratios, such as gross margin, are non-additive. The
numerator and denominator should be stored in the fact table. The ratio can then
be calculated in a BI tool for any slice of the fact table by remembering to calculate
the ratio of the sums, not the sum of the ratios.



The date dimension is a special dimension because it is the one dimension nearly
guaranteed to be in every dimensional model since virtually every business process

Every join between dimension and fact tables in the data warehouse
should be based on meaningless integer surrogate keys. You should avoid using a
natural key as the dimension table’s primary key.


At the most granular level, the airline captures data at the leg level. The leg
represents an aircraft taking off at one airport and landing at another without any
intermediate stops. Capacity planning and fl ight scheduling analysts are interested
in this discrete level of information because they can look at the number of seats
to calculate load factors by leg. Operational aircraft fl ight metrics are captured at
the leg level, such as fl ight duration and the number of minutes late at departure
and arrival. Perhaps there’s even a dimension to easily identify on-time arrivals.
The next level of granularity corresponds to a segment. Segments refer to a
single fl ight number (such as Delta fl ight number 40 or DL0040) fl own by a single
aircraft. Segments may have one or more legs associated with them; in most cases
segments are composed of just one leg with a single take-off and landing. If you
take a fl ight from San Francisco to Minneapolis with a stop in Denver but no air-
craft or fl ight number change, you have fl own one segment (SFO-MSP) but two
legs (SFO-DEN and DEN-MSP). Conversely, if the fl ight fl ew nonstop from San
Francisco to Minneapolis, you would have fl own one segment as well as one leg.
The segment represents the line item on an airline ticket coupon; passenger revenue
and mileage credit is determined at the segment level. So although some airline
departments focus on leg level operations, the marketing and revenue groups focus
on segment-level metrics.
Next, you can analyze fl ight activity by trip. The trip provides an accurate picture
of customer demand. In the prior example, assume the fl ights from San Francisco
to Minneapolis required the fl yer to change aircraft in Denver. In this case, the trip
from San Francisco to Minneapolis would entail two segments corresponding to the
two involved aircraft. In reality, the passenger just asked to go from San Francisco
to Minneapolis; the fact that she needs to stop in Denver is merely a necessary evil.
For this reason, sales and marketing analysts are also interested in trip level data.
Finally, the airline collects data for the itinerary, which is equivalent to the entire
airline ticket or reservation confi rmation number.
The DW/BI team and business representatives decide to begin at the segment-level
grain. This represents the lowest level of data with meaningful revenue metrics.
Alternatively, you could lean on the business for rules to allocate the segment-level
metrics down to the leg, perhaps based on the mileage of each leg within the seg-
ment. The data warehouse inevitably will tackle the more granular leg level data for
the capacity planners and fl ight schedulers at some future point. The conforming
dimensions built during this fi rst iteration will be leveraged at that time.
There will be one row in the fact table for each boarding pass collected from
passengers. The dimensionality associated with this data is quite extensive, as
illustrated in Figure 12-2. The schema extensively uses the role-playing technique.
The multiple date, time, and airport dimensions link to views of a single underly-
ing physical date, time, and airport dimension table, respectively, as we discussed
originally in Chapter 6: Order Management.

The passenger dimension is a garden variety customer dimension with rich attri-
butes captured about the most valuable frequent fl yers. Interestingly, frequent fl yers
are motivated to help maintain this dimension accurately because they want to
ensure they’re receiving appropriate mileage credit. For a large airline, this dimen-
sion has tens to hundreds of millions of rows.
Marketing wants to analyze activity by the frequent fl yer tier, which can change
during the course of a year. In addition, you learned during the requirements pro-
cess that the users are interested in slicing and dicing based on the fl yers’ home
airports, whether they belong to the airline’s airport club at the time of each fl ight,
and their lifetime mileage tier. Given the change tracking requirements, coupled
with the size of the passenger dimension, we opt to create a separate passenger pro-
fi le mini-dimension, as we discussed in Chapter 5: Procurement, with one row for
each unique combination of frequent fl yer elite tier, home airport, club membership
status, and lifetime mileage tier. Sample rows for this mini-dimension are illustrated
in Figure 12-3. You considered treating these attributes as slowly changing type
2 attributes, especially because the attributes don’t rapidly change. But given the
number of passengers, you opt for a type 4 mini-dimension instead. As it turns
out, marketing analysts often leverage this mini-dimension for their analysis and
reporting without touching the millions of passenger dimension rows.

The aircraft dimension contains information about each plane fl own. The origin
and destination airports associated with each fl ight are called out separately to
simplify the user’s view of the data and make access more effi cient.
The class of service fl own describes whether the passenger sat in economy, pre-
mium economy, business, or fi rst class. The fare basis dimension describes the terms
surrounding the fare. It would identify whether it’s an unrestricted fare, a 21-day
advance purchase fare with change and cancellation penalties, or a 10 percent off
fare due to a special promotion.
The sales channel dimension identifi es how the ticket was purchased, whether
through a travel agency, directly from the airline’s phone number, city ticket offi ce, or
website, or via another internet travel services provider. Although the sales channel
relates to the entire ticket, each segment should inherit ticket-level dimensional-
ity. In addition, several operational numbers are associated with the fl ight activity
data, including the itinerary number, ticket number, fl ight number, and segment
sequence number.
The facts captured at the segment level of granularity include the base fare rev-
enue, passenger facility charges, airport and government taxes, other ancillary
charges and fees, segment miles fl own, and segment miles awarded (in those cases
in which a minimum number of miles are awarded regardless of the fl ight distance).

 You should list those data elements whose quality is known to be unac-
ceptable, and list whether an agreement has been reached with the source systems
to correct the data before extraction. List those data elements discovered during
data profi ling, which will be continuously monitored and fl agged as part of the
ETL process.


You should use the bus matrix of business processes to generate a priority
list for conforming dimensions (columns of the bus matrix). Annotate each row
of the bus matrix with whether there is a clear executive demand for the busi-
ness process to participate in the integration process, and whether the ETL team
responsible for that business process has agreed.


Fixed Dimension Information
slowly changing Dimension Information