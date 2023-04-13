from application.database import db


    # def __repr__(self) -> str:
    #     return f"{self.user_idd}-{self.randn}"



class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
    primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
    primary_key=True)

class DP(db.Model):
    __tablename__ = 'dp'

    dp_id = db.Column(db.Integer, primary_key=True,autoincrement=True, nullable=False)
    dp_name = db.Column(db.String, nullable=False)
    # email_id = db.Column(db.String, unique=True,db.ForeignKey("user.email_id"))
    email_id = db.Column(db.String, db.ForeignKey("user.email_id"), nullable=False)


class Comment(db.Model):
    __tablename__ = 'comment'
    com_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(180), nullable=False)
    comment_time = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id', ondelete="CASCADE"), nullable=False)


class Like(db.Model):
    __tablename__ = 'like'
    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id',ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id', ondelete="CASCADE"), nullable=False)



class Post(db.Model):

    __tablename__ ='post'
    post_id=db.Column(db.Integer,primary_key=True, autoincrement=True)
    description=db.Column(db.Text)
    time_created=db.Column(db.String, nullable=False)
    image_name=db.Column(db.String(),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "user.user_id"), nullable=False)
    
    comment = db.relationship("Comment",backref= "post",lazy = True)
    like = db.relationship("Like",backref= "post",lazy = True)
    # firstname = db.Column(db.String, db.ForeignKey(User.firstname), nullable=False)
    # # lastname = db.Column(db.String, db.ForeignKey(
    #     "user.lastname"), nullable=False)
    
    # user_name = db.Column(db.String(), db.ForeignKey(User.username,ondelete='CASCADE'), nullable=False)
    # user_name=db.Column(db.String,db.ForeignKey(User.username,ondelete='CASCADE'),nullable=False)

    

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String, nullable=False, unique = True)
    lastname = db.Column(db.String, nullable=False)
    email_id = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    deadline = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    posts = db.relationship("Post",backref= "user",lazy = True)
    comment = db.relationship('Comment',
                                foreign_keys=[Comment.user_id],
                                backref=db.backref('user', lazy='joined'),
                                lazy='dynamic',
                                )
    dp = db.relationship("DP",backref= "user",lazy = True)
    followed = db.relationship('Follow',
                                foreign_keys=[Follow.follower_id],
                                backref=db.backref('follower', lazy='joined'),
                                lazy='dynamic',
                                )

    followers = db.relationship('Follow',
                                foreign_keys=[Follow.followed_id],
                                backref=db.backref('followed', lazy='joined'),
                                lazy='dynamic',
                                )
    

    
    def follow(self, user):
        if not self.is_following(user):
            f = Follow(follower=self, followed=user)
            db.session.add(f)

    def unfollow(self, user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)

    def is_following(self, user):
        return self.followed.filter_by(
            followed_id=user.id).first() is not None        

    def is_followed_by(self, user):
        return self.followers.filter_by(
            follower_id=user.id).first() is not None
    # randn = db.Column(db.String, nullable=False, unique=True)



