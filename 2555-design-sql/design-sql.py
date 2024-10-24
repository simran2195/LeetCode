class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        
        self.tables = {name: {} for name in names}
        # self.tables = {
        #     "users": {
        #         2: ["Bob", "30"]  # Only Bob remains after Alice (ID 1) was deleted
        #     },
        #     "orders": {
        #         1: ["Order1", "Pending", "2024-10-24"],
        #         2: ["Order2", "Shipped", "2024-10-23"]
        #     }
        # }
                
        # Keep track of the next available row ID for each table.
        self.next_id = {name: 1 for name in names}
        # self.next_id = {
        #     "users": 3,   # Even though row ID 1 was deleted, the next row ID will be 3
        #     "orders": 3   # After inserting two rows, the next row ID will be 3
        # }
        self.columns = dict(zip(names, columns))


    def insertRow(self, name: str, row: List[str]) -> None:
        row_id = self.next_id[name]  # Get the current row ID to insert
        self.tables[name][row_id] = row  # Insert the row into the table
        self.next_id[name] += 1  # Increment the next row ID
        

    def deleteRow(self, name: str, rowId: int) -> None:
        if rowId in self.tables[name]:  # Check if the row exists
            del self.tables[name][rowId]  # Delete the row

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        if rowId in self.tables[name]:
            return self.tables[name][rowId][columnId - 1]  # Return the value
        return ""
        


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)