def The_Digit_of_Life(date_time):
    #if the date_time is not int than it work
    if date_time is not int:
        sum_date=0
        for i in date_time:
            sum_date=sum_date+int(i)
        j=0
        for z in str(sum_date):
            j=j+int(z)
        return j
print(The_Digit_of_Life("20000101"))  
