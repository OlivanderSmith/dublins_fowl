from app import db
from models import BlogPost

# create the Database and the DB tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I'm Good"))
db.session.add(BlogPost("Well", "I'm Well"))
db.session.add(BlogPost("Enthusuastic", "I'm Enthusiastic"))

# commit the changes
db.session.commit()
