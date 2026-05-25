# British Airways Data Science Job Simulation - Task 1


## Github: 
https://github.com/techexplorer152/ba-forage-data-science-tasks

### Task Description 
This repository contains a Python data
aggregation pipeline developed for the
British Airways Airport Planning team.
The objective of this project is to 
construct a script for processing a 
specific dataset included in this 
repository


### Justification
The data points are first separated 
into 2 groups SHORT and LONG, then 
into 4 subgroups: Morning, Lunchtime, 
Afternoon, and Evening. This structure
allows airport teams to easily plan 
staffing schedules and catering 
volumes for specific morning or 
evening waves. To eliminate structural
data bias caused by varying aircraft
fleet sizes across the network, the 
model avoids calculating simple 
statistical averages of individual 
flights; instead, it utilizes a 
macro-weighted capacity approach, 
dividing the total sum of eligible 
tier passengers within each profile
by the total combined physical seat 
capacity.




### Python Libraries
Ensure your local Python environment has the necessary libraries installed:
```bash
pip install pandas openpyxl