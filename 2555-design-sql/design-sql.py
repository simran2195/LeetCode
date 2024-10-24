class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        
        self.tables = {name: {} for name in names}
                
        # Keep track of the next available row ID for each table.
        self.next_id = {name: 1 for name in names}
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