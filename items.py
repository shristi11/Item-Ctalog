from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#creating user1
user1 = User(name="Shrist Grg", email="shristyzrg@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# category for Camping
category1 = Category(name="Camping", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Pepper Spray", user_id=1, description="Stop an angry, charging bear with this amazingly effective deterrent. DAP Bear Spray has been proven effective in dozens of bear attacks. Dring a bow over a decade ago, Mark Mathwny was attacked by a grizzly bear and sffered nmeros bite lacereations in the head nad Neck. Mark experience changed his life. Since then he has dedicated himself to improving a prodct designed to safegard people against malings, and to help them coexist with wildlife.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Delx Air Mattress", user_id=1, description="A delx version of intex Delx Qeen air mattress with the bilt in pmp and pillow rest is the ltimate in lxcirios air mattress. ", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="North Face Bagpack", user_id=1, description="The flexvent sspention system boasts comparission molded sholder straps, and a padded air mesh back pannel with a specific floating padded laptop sleeve in main compartment proects laptop frpm bmos and falls.", category=category1)

session.add(item3)
session.commit()

item4 = CategoryItem(name="Mmmy Sleeping bag", user_id=1, description="Best choice brands presents new sleeoping bag. This envelop style sleeping bsg is lightweight for easy transportation and will keep yo cozy dring night. yo will be able to keep temperatre weather conditions from being an isse.", category=category1)

session.add(item4)
session.commit()

# Fitness category
category2 = Category(name="Fitness Equipment", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Power Guidance pull up Bands", user_id=1, description="Wheather yo are st starting ot with the pll ps and downs yo are b athelete working on regaining or enhancing yor stherngth the Power Guidance pull up Bands will help yo take yor pll ps and downs and chin training to the next level ", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Thick Folding Gym Mat", user_id=1, description="Gymnastics mat can be sed for varid physical activites not only in the gymm bt also for yoga, dancing, light strechinf, martial arts and general excercise. Or mattres is designed for schools, clbs teams or individals", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Yes Yoga Ball", user_id=1, description="Yoga ball can be sed for varid physical activites not only in the gymm bt also for yoga, dancing, light strechinf, martial arts and general excercise.", category=category2)

session.add(item3)
session.commit()

# Baseball category
category3 = Category(name="Baseball", user_id=1)

session.add(category3)
session.commit()

# Water Sports
category4 = Category(name="Water Sports", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="Solstice convertible Kayak", user_id=1, description="Get ready for adventre with this brand new Solictice Whitewater Roge Kayak! This 2 person infalatable kayak is craftl made with heavy dty k80 material that ill keep bringinh yo back for more.A", category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Aqa Googles ", user_id=1, description="The seal xp is  a hybrid google that combines the sperior vision and exceptional comfort of the deal mask with the low profile and hydropnaes os the kaman googles. The low profile wrap arontd the design o yhe dfdeal xp .", category=category4)

session.add(item2)
session.commit()

# Golf
category5 = Category(name="Golf", user_id=1)

session.add(category5)
session.commit()

# Archery
category6 = Category(name="Archery", user_id=1)

session.add(category6)
session.commit()

item1 = CategoryItem(name="Bear Archery Cruzer", user_id=1, description="Introducing the all new 2016 Cruzer bow designed, tested and manufactured to meet the needs of any bowhunter, from the little ones on up to dad. This bow will fit everyone The new Cruzer bow has an incredible draw length range from 12inch to 13 inch, and adjustable draw weights that start way down at 5 lbs and go way up to 70 lbs. The new Cruzer bow comes completely rigged with the latest high quality accessories from Trophy Ridge and will be the last bow you will ever need to buy.", category=category6)

session.add(item1)
session.commit()

item2 = CategoryItem(name="TROPHY RIDGE BEAR REACT H5", user_id=1, description="New Trophy Ridge React H5 5-Pin. 019 Sight RH. Trophy Ridge React H5 sight. Take your accuracy to the next level with React Technology. Mathematical precision of React Technology automatically adjusts all pins to the optimal location.", category=category6)

session.add(item2)
session.commit()

# Climbing & Caving Equipment
category7 = Category(name="Climbing & Caving Equipment", user_id=1)

session.add(category7)
session.commit()

item1 = CategoryItem(name="Aluminum Carabiner D-Ring Key Chain", user_id=1, description="Brand new in bulk package. Made from light weight aluminum alloy. It Includes a 1 inch diameter nickel plated steel split ring for other attachments. Great for outdoor activity, camping, fishing, hiking, traveling, keychain etc. It Is not made for climbing adventure.The carabiner features a spring loaded gate which allows them to be quickly and securely attached to a wide range of fixing points. It can open and close smoothly as the spring-loaded gate makes it easy to attach important items to a pack or belt. Two pieces as a set for salPlease note that latest version might vary slightly from time to time from manufacture without advance notice", category=category7)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Paracord-100 Feet Nylon Parachute Cord", user_id=1, description="550 Paracord is the most used, dependable, tough and long lasting cord we offer. It can be used for countless projects and perfect for crafting, repairing and other paracord projects.Paracord was first used by the U.S. Military.They would use it for many applications such as attaching equipment to harnesses, tying rucksacks to vehicle racks and for securing camouflage nets to trees or vehicles. However, it's most popular use was it use as suspension lines for parachutes for US paratroopers during World War 2.", category=category7)

session.add(item2)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name