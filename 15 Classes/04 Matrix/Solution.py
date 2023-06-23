class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = []
        self.columns = []
        self.create_matrix()

    def create_matrix(self):
        # Create Rows:
        num = ""
        row = []
        for i, char in enumerate(self.matrix_string):
            if char.isdigit():
                num += char
                if i == len(self.matrix_string) - 1:
                    row.append(int(num))
                    self.rows.append(row)
            elif char == "\n":
                row.append(int(num))
                self.rows.append(row)
                row = []
                num = ""
            elif char == " ":
                row.append(int(num))
                num = ""

        # Create Columns:
        i = 0
        j = 0
        column = []
        while j < len(self.rows[0]):
            if i < len(self.rows):
                column.append(self.rows[i][j])
                i += 1
            else:
                self.columns.append(column)
                column = []
                i = 0
                j += 1

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
        
