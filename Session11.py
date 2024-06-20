quote1 = "Search the candle rather than cursing the darnkness\n"
quote2 = "Be Exceptional\n"

#file = open("quotes.txt", "w")
file = open("quotes.txt", "a")
file.write(quote1)
file.write(quote2)

#free memory resource 
file.close()
print("Data Written....")