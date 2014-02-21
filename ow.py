#d=[[('Script','CoalIndia'),('Qty','801'),('IPORate','297')],
#[('Script','esl'),('Qty','3442'),('IPORate','11')],
#[('Script','MCX'),('Qty','8'),('IPORate','1032')]]
d=[[('Script','CoalIndia'),('Qty',801),('IPORate',297)],
[('Script','ESL'),('Qty',3442),('IPORate',11)],
[('Script','MCX'),('Qty',8),('IPORate',1032)],
[('Script','AdaniPower'),('Qty',368),('IPORate',100)],
[('Script','BrigadeEnterprises'),('Qty',57),('IPORate',390)],
[('Script','ElectroSteels'),('Qty',3442),('IPORate',11)],
[('Script','EngineersIndia'),('Qty',119),('IPORate',290)],
[('Script','IFCI'),('Qty',1),('IPORate',60)],
[('Script','J%26KBank'),('Qty',447),('IPORate',1255)],
[('Script','L%26TFinance'),('Qty',353),('IPORate',52)],
[('Script','MCXIndia'),('Qty',8),('IPORate',1032)],
[('Script','OilIndia'),('Qty',57),('IPORate',1050)],
[('Script','PFC'),('Qty',500),('IPORate',200)],
[('Script','ReliancePower'),('Qty',16),('IPORate',450)],
[('Script','RECLtd'),('Qty',121),('IPORate',105)],
[('Script','SJVNLtd'),('Qty',338),('IPORate',26)],
[('Script','SBM'),('Qty',13),('IPORate',575)],
[('Script','VijayaBank'),('Qty',1),('IPORate',60)],
[('Script','StandardCharteredPLC'),('Qty',209),('IPORate',99.8)]]
for i in xrange(len(d)):
		d1=float(d[i][1][1])
		d2=float(d[i][2][1])
		invt=reduce(lambda x,y:x*y,[d1,d2])
		d[i].append(("Investment",invt))

script=[]
for i in xrange(len(d)):
	script.append(d[i][0][1])


TotalInvestment=0
for i in xrange(len(d)):
	TotalInvestment = TotalInvestment + d[i][3][1]

#print d
print "Total Investment = ",  TotalInvestment

#for i in xrange(len(script)):
#	print script[i]

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
