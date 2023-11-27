class Table:
    def __init__(self, result):
        """ RESERVE: Previous attempt at storing data (too many moving parts, hard to organize)
        self.previous_close = ""
        self.open = ""
        self.bid = ""
        self.ask = ""
        self.day_range = ""
        self.year_range = ""
        self.volume = ""
        self.avg_volume = ""
        self.market_cap = ""
        self.beta = ""
        self.pe_ratio = ""
        self.eps = ""
        self.earning_date = ""
        self.div_yield = ""
        self.ex_div_date = ""
        self.year_est= ""
        """

        
        """ FORMAT OF TABLE w/ Indices
        0.  Previous Close: 234.21
        1.  Open: 233.75
        2.  Bid: 235.66 x 1100
        3.  Ask: 235.70 x 1300
        4.  Day's Range: 232.33 - 238.75
        5.  52 Week Range: 101.81 - 299.29
        6.  Volume: 64,848,436
        7.  Avg. Volume: 121,688,838
        8.  Market Cap: 748.477B
        9.  Beta (5Y Monthly): 2.28
        10. PE Ratio (TTM): 76.20
        11. EPS (TTM): 3.09
        12. Earnings Date: Jan 23, 2024 - Jan 29, 2024
        13. Forward Dividend & Yield: N/A (N/A)
        14. Ex-Dividend Date: N/A
        15.1y Target Est: 224.90
        """
        self.table_headers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.table_data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.update_table(result)
    
    def print_table(self):
        for number in range(16):
            print(self.table_headers[number] + ": " + self.table_data[number])

    def update_table(self, result):
        if result != "":
            counter = 1
            itr_header = 0
            itr_data = 0

            #DEBUGGING
            #print(result)
            
            for row in result:
                #Accesses Header Values
                if counter % 2 == 1:
                    self.table_headers[itr_header] = row.text
                    itr_header += 1

                #Accesses Data Values
                if counter % 2 == 0: 
                    self.table_data[itr_data] = row.text
                    itr_data += 1

                #Increment Counter
                counter += 1