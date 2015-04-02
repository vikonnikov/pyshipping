import pyshipping
from pyshipping.package import Package
from pyshipping.binpack_simple import binpack

packages = [
    Package([100, 100, 100]),
    Package([70, 80, 90]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([100, 100, 100]),
    Package([70, 70, 90])]

print binpack(packages, Package([200, 200, 300]))

# from pyshipping.plot import Strip
# 
# s = Strip()
# p1 = Package([90, 75, 30])
# p2 = Package([100, 100, 100])
# p3 = Package([50, 50, 50])
# s.add(p1)
# s.add(p2)
# s.add(p3)
# 
# s.draw()
# s.save()