from mylinearregression import linearregression
amount=[34,108,64,88,99,51]
tip= [5,17,11,8,14,5]
model=linearregression(amount,tip)
model.fit()
print(model.b0,model.b1)
# test=[70,2000]
# p=model.predict(test)
# print(p.new_pred)
model.predict(amount)
print(model.new_pred)
k=model.MSE()
print(k)
model.drawregressionline()
