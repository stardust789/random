import rpy
x = [5.05, 6.75, 3.21, 2.66]
y = [1.65, 26.5, -5.93, 7.96]
rpy.set_default_mode(rpy.NO_CONVERSION)
linear_model = rpy.r.lm(rpy.r("y ~ x"), data = rpy.r.data_frame(x=x, y=y))
rpy.set_default_mode(rpy.BASIC_CONVERSION)
print linear_model.as_py()['coefficients']
print rpy.r.summary(linear_model)
