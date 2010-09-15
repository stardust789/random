from rpy import r
my_x = [5.05, 6.75, 3.21, 2.66]
my_y = [1.65, 26.5, -5.93, 7.96]
ls_fit = r.lsfit(my_x,my_y)
gradient = ls_fit['coefficients']['X']
yintercept= ls_fit['coefficients']['Intercept']

r.png("scatter_regression.png", width=400, height=350)
r.plot(x=my_x, y=my_y, xlab="x", ylab="y", xlim=(0,7), ylim=(-16,27),
       main="Example Scatter with regression")
r.abline(a=yintercept, b=gradient, col="red")
r.dev_off()
