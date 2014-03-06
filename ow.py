class myscripts:
	def __init__(self):
		self.d=[[('Script','CoalIndia'),('Qty',801),('IPORate',267)],
		[('Script','ESL'),('Qty',3442),('IPORate',11)],
		[('Script','MCX'),('Qty',8),('IPORate',1032)],
		[('Script','ADANIPOWER'),('Qty',368),('IPORate',100)],
		[('Script','BRIGADE'),('Qty',57),('IPORate',390)],
		[('Script','ENGINERSIN'),('Qty',119),('IPORate',275)],
		[('Script','IFCI'),('Qty',1),('IPORate',60)],
		[('Script','L%26TFH'),('Qty',353),('IPORate',52)],
		[('Script','J%26KBank'),('Qty',477),('IPORate',1255)],
		[('Script','OIL'),('Qty',143),('IPORate',418)],
		[('Script','PFC'),('Qty',500),('IPORate',200)],
		[('Script','RPOWER'),('Qty',16),('IPORate',450)],
		[('Script','RECLTD'),('Qty',121),('IPORate',105)],
		[('Script','SJVN'),('Qty',338),('IPORate',26)],
		[('Script','MYSOREBANK'),('Qty',13),('IPORate',575)],
		[('Script','VIJAYABANK'),('Qty',1),('IPORate',60)],
		[('Script','STAN'),('Qty',209),('IPORate',99.8)]]

		for i in xrange(len(self.d)):
			d1=float(self.d[i][1][1])
			d2=float(self.d[i][2][1])
			invt=reduce(lambda x,y:x*y,[d1,d2])
			self.d[i].append(("Investment",invt))

		self.script=[]
		for i in xrange(len(self.d)):
			self.script.append(self.d[i][0][1])
	

		TotalInvestment=0
		for i in xrange(len(self.d)):
			TotalInvestment = TotalInvestment + self.d[i][3][1]

#print d
		print "Total Investment = ",  TotalInvestment

#for i in xrange(len(script)):
#	print script[i]

#uncomment the following line to print script list
#print "Script = ", script
#d1=int(d[0][1][1])

#d2=int(d[0][2][1])
#d1=int(d.items()[0][1])
#d2=int(d.items()[1][1])
#for i in xrange(len(d)):
#	d1=int(d[i][1][1])
#	d2=int(d[i][1][1])
#	invt=reduce(lambda x,y:x*y,[d1,d2])
#	print invt
#	d[i].append(("Investment",invt))
#d.append(d3)
#d.append(dict(zip('Investment','invt')))
#print "Printing d[0] after modification"
#print d
#allscripts()
#a2=myscripts()
#a2.allscripts()
