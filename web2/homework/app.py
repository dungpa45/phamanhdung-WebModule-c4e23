import mlab
from river import River


mlab.connect()

#ex 2
# record = River.objects(continent__istartswith="Africa")
# print(len(record))
# for r in record:
#     print(r.name)

# ex3
record = River.objects(continent__istartswith="S. America",length__lte=1000)
print(len(record))
for r in record:
    print(r.name)
