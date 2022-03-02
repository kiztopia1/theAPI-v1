def update_stock (model, sell_amount, id):
	a = model.objects.get(id= id)
	# checking if stock is under min_stock
	a.stock_level = a.stock_level - sell_amount
	if(a.stock_level < a.min_stock ):
		a.stock_alert = True
	a.save()