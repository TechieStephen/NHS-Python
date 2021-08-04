# import humanize
# import datetime as dt
# # from humanize import *
#
# x = 1234559130
# print(humanize.intcomma(x))
# print(humanize.intword(x))
# print(humanize.naturalsize(1_000_000_000))
# date = dt.datetime.now()
# print(date)
# print(humanize.naturalday(date - dt.timedelta(days=3)))
# print(humanize.naturaltime(date - dt.timedelta(weeks=3)))
#

import mymodules
x = mymodules.calculator(70, 90)
print(x)
print(mymodules.turnToUpper('salad'))