"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employeeMap = {e.id: e for e in employees}

        def findRes(eid):
            employee = employeeMap[eid]
            return (employee.importance + sum(findRes(eid) for eid in employee.subordinates))

        return findRes(id)