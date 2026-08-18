class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_total, cost_total = sum(gas), sum(cost)
        # we need more gas than cost overral to travel all stations.
        # since cost here is like gas consumptions. so if have more or equal gas than consumption,
        #  it is gurantee to travel all stations.
        if cost_total > gas_total: return -1
        
        index, tank = 0 , 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0: # if the tank goes below zero, that means the i can't be the starting index.
                tank = 0
                index = i+1 # set current index to i+1 because we know that this i gives negative tank so we have to start from next i, the goal is to check weather we can reach the end or not. not the full circle because we already check about that we have more/equal fuel to travell through all stations.
        return index


        