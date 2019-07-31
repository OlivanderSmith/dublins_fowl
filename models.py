from app import db

# create table called BlogPost


class BlogPost(db.Model):

    # give name to table and column headers
    __tablename__ = "Posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

# This init is not neccessary actually as the SQLAlchemy automatically inits when columns have keyword arguments as titles
    # initiate the table
    # def __init__(self, title, description):
    #     self.title = title
    #     self.description = description

    # define how it will be represented (returned)
    def __repr__(self):
        return 'Title - {}, Description - {}'.format(self.title, self.description)
