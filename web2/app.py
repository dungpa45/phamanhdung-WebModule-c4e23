import mlab
from movie import Movie
from resource import Resource
from faker import Faker

faker = Faker("en_US")

# for _ in range(50):
#     print(faker.state())

mlab.connect() #ket noi db

# delete by ID

# m = Movie.objects().with_id("5bf80192e7179a56e215533c")
# print(m.title)
# m.delete()

# r = Resource.objects().with_id("5bf7fed7f3fe55273cf97aa8")
# if r is None:
#     print("Not Found")
# else:
#     print("Found")
#     r.delete()
# print(r[2].id)
# print(r[0].id)
# r=resource_list = Resource.objects().first()

# # r = resource_list[0]
# print(r.id)





#############################################
#hien thi db

# movie_list = Movie.objects()
# for m in movie_list:
#     print(m.title)
#     print(m.year)
#     print(m.image)

# resource_list = Resource.objects()
# for r in resource_list:
#     print(r.name, r.city, r.year, r.height, r.weight,sep="\n")
#########################################

# ad db
# m = Movie(title="Deadpool", year=2016, image="https://m.media-amazon.com/images/S/aplus-media/vc/0ffc3cff-5aba-4444-9ee9-7f696f889701._SL300__.png")
# rs = Resource(name="Pham Anh Dung",city="Ha Noi",year=1997,height=167,weight=62)



#luu db
# m.save() 
# rs.save()
from random import randint
# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     year = randint(1953,2000)
#     height = randint(150,190)
#     weight = randint(40,150)
#     r = Resource(name=name,city=city,year=year,height=height,weight=weight)
#     r.save()

# record = Resource.objects(name="Brian Gomez")
# for r in record:
#     print(r.city)
#     print(r.height)
#     print(r.weight)

# record = Resource.objects(height=172)
# for r in record:
#     print(r.name)
#     print(r.city)
#     print(r.height)
#     print(r.weight)

# record = Resource.objects(name__istartswith="paul") # i la ignore case viet hoa thuong van nhan
# print(len(record))
# for r in record:
#     print(r.name)

# record = Resource.objects(height__gte=170)
# print(len(record))
# for r in record:
#     print(r.name)
#     print("=============")


# record = Resource.objects(height__lte=160,name__icontains="Em")
# print(len(record))
# for r in record:
#     print(r.name)
#     print("=============")
    
# record = Resource.objects()

# for r in record:
#     r.update(set__available=False)

r = Resource.objects().with_id("5bf80cf6f3fe551d4ccb5a10")
r.update(set__available= True)

