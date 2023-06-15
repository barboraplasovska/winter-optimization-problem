# Winter optimization problem

This research project aims to address the concerns of Montréal residents regarding snowplowing operations while considering the delicate issue of increasing the allocated funds. The objective is to minimize the cost of a typical snowplowing day by finding an efficient and cost-effective path for snowplows around the Montréal road network. Additionally, a drone-based aerial analysis will be performed to identify the sectors requiring immediate snowplowing. The report provides a summary of the data used, the study perimeter, hypotheses, model choices, selected solutions, cost model for snow removal operations, and limitations of the proposed model.

See the demo for a demonstration of our proposed solution.


## Install the project
```sh
when you clone the project or install it just use this command.
42sh$ jupyter-notebook
and after that just select the demo.ipynb file and press on the Run button

```

## The Structure

### The Drone Directory
- There is the drone.py file in the drone directory. It contains the functions to calculate the distance of the drone in the five districts

### The Snowplow Directory
- There is the snowplow.py file in the snowplow directory. It contains the functions to calculate the distance of the snowplows in the the five districts

### The Cost Directory
- There is the cost.py file in the cost directory. It contains six functions to calculate the cheapest cost and the number of the drones and the snowplows

### The Report
- There is the Rapport.pdf file. It contains the report of the project with an introduction, our way of thinking for the drone and snowplows and of course a conclusion

### The AUTHORS
- There is the AUTHORS file. It contains the name of all the members of the group

