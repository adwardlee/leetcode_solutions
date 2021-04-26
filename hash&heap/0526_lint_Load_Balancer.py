'''
Description
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.

Example
Example 1:

Input:
  add(1)
  add(2)
  add(3)
  pick()
  pick()
  pick()
  pick()
  remove(1)
  pick()
  pick()
  pick()
Output:
  1
  2
  1
  3
  2
  3
  3
Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.
'''
import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.dict = {}
        self.list = []
    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id not in self.dict:
            self.dict[server_id] = len(self.list)
            self.list.append(server_id)
        return
    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        oneid = self.list[-1]
        num_index = self.dict[server_id]
        self.list[num_index] = oneid
        self.dict[oneid] = num_index
        self.list.pop()
        self.dict.pop(server_id)
    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        return random.choice(self.list)