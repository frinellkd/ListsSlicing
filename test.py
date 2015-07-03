new_list = [1,2,3,4,5,6,7,8]
value = 3




def cust_inst(new_list):
	new_list[:] = new_list[::-1] 
	print new_list


cust_inst(new_list)
print new_list