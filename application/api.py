from flask_restful import Resource,reqparse,marshal, Api,fields, marshal_with, abort
from flask_caching import Cache
from flask import current_app as app,jsonify,send_from_directory,session
from application.models import *
from datetime import datetime as dt
import os
from application import tasks
from application.jwt_setup import aise_kuch_na_hone_dunga
import jwt
import json
import time
from datetime import datetime
app.config["IMAGE_UPLOADS"] = "blogdev\src\assets\images\dp"
api = Api(app)

# fields =================================fields================================
# fields ==================================fields===============================

# Dp_field
dp_fields = {
    "dp_name":fields.String,
    "email_id":fields.String
}



# follow_field
follow_field={
    'follower_id':fields.Integer,
    'followed_id':fields.Integer
}
# user name field
name_fields = {
    "firstname":fields.String,
    "lastname":fields.String,
    "dp":fields.List(fields.Nested(dp_fields))
}

comment_fields = {
    "comment": fields.String,
    "comment_time": fields.String,
    "user":fields.List(fields.Nested(name_fields))
}

like_fields = {
    "List_user":fields.List(fields.Integer)
}
# post field
post_fields = {
    "post_id" : fields.Integer,
    "description" : fields.String,
    "image_name" : fields.String,
    "user_id" : fields.Integer,
    "time_created":fields.String,
    "comment":fields.List(fields.Nested(comment_fields)),
    "like":fields.List(fields.Nested(like_fields)),
    "user":fields.List(fields.Nested(name_fields)),    
}

# user field
user_fields = {
    "user_id" : fields.Integer,
    "firstname" : fields.String,
    "lastname" : fields.String,
    "email_id" : fields.String,
    "password" : fields.String,
    "deadline" : fields.String,
    "gender" : fields.String,
    "dp":fields.Nested(dp_fields),
    "posts" : fields.List(fields.Nested(post_fields)),
    "followed":fields.List(fields.Nested(follow_field)),
    "followers":fields.List(fields.Nested(follow_field))
}

# cache setup
app.config["CACHE_TYPE"] = "RedisCache"
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"  
app.config['CACHE_DEFAULT_TIMEOUT'] = 30
cache= Cache(app)
#  ============================================SignUp Parser==================================
# # ==
 
create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('firstname')
create_user_parser.add_argument('lastname')
create_user_parser.add_argument('email_id')
create_user_parser.add_argument('password')
create_user_parser.add_argument('deadline')  # dob hai ye 
create_user_parser.add_argument('gender')



# ============================================LoginParser==================================
# ============================================================================================

follow_req=reqparse.RequestParser()
follow_req.add_argument('follower_id',type=int)
follow_req.add_argument('followed_id',type=int)




login_user_parser = reqparse.RequestParser()
login_user_parser.add_argument('email_id')
login_user_parser.add_argument('password')


# search_parser = reqparse.RequestParser()
# search_parser.add_argument('name')

# ==============================DP parser ==============================================
dp_parser = reqparse.RequestParser()
dp_parser.add_argument('dp_name')

# =========================Add-post ================

add_post = reqparse.RequestParser()
add_post.add_argument('post_desc')
add_post.add_argument('post_image')


# ===========Comment ===========
com_parser =reqparse.RequestParser()
com_parser.add_argument('comment')
com_parser.add_argument('user_id')


# ========== Like Parser ===========

like_parser =reqparse.RequestParser()
like_parser.add_argument('post_id')
like_parser.add_argument('user_id')


@app.route('/eheboy')
@cache.cached(timeout=50)
def testingcache():
    time.sleep(10)
    return "le beta hogya cache"


class Follows(Resource):
    
    @marshal_with(follow_field)
    def post(self,id):
        data=follow_req.parse_args()
        my_id=User.query.filter(User.user_id==id).first()
        
            
        following = Follow(follower_id=data.get('followed_id'), followed_id=my_id.user_id)
        db.session.add(following)
        db.session.commit()
        return {'status':'done'}






class Unfollows(Resource):
    
    @marshal_with(follow_field)
    def post(self,id):
        data=follow_req.parse_args()
        my_id=User.query.filter(User.user_id==id).first()
        

        unfollowing = Follow.query.filter_by(follower_id=data.get('followed_id'), followed_id=my_id.user_id).first()
        if unfollowing:
            db.session.delete(unfollowing)
            db.session.commit()
            return {'status':'done'}
        





class Myfollowing(Resource):
    
    # @marshal_with(follow_field)
    def post(self,id):
        data=follow_req.parse_args()
        myfollowing=Follow.query.filter_by(follower_id=id).all()
        temp=[]
        for follower in myfollowing:
            temp.append(follower.followed_id)
            
        print(temp)


        return temp
    



class Myfollowers(Resource):
    
    @marshal_with(follow_field)
    def post(self,id):
        data=follow_req.parse_args()
        myfollower=Follow.query.filter_by(followed_id=id).all()
        temp=[]
        for follower in myfollower:
            temp.append(follower.follower_id)
            
        print(temp)
        return temp
    
    



# ?export posts

@app.route('/api/export/<int:user_idd>', methods=['GET'])
def export_post(user_idd):
    posts = Post.query.filter_by(user_id=user_idd).all()
    with open(f'csvs/{user_idd}_Det.csv', 'w') as posts_csv:
        posts_csv.write("SNo,Post_cation,Post_Image,Created_Time\n")
        for i in range(len(posts)):

            list = posts[i]
            print(list)
            posts_csv.write(f'{i+1},{list.description},{list.image_name[:20]},{list.time_created}\n')
            
        
    return send_from_directory("csvs",f'{user_idd}_Det.csv')



class Search(Resource):
    
    @marshal_with(user_fields)
    def get(self,name):
       
        users = User.query.all()
        user_det = []
        for user in users:
            naam = user.firstname.lower()
            name = name.lower()
            if naam == name:
                user_det.append(user)
            else:
                if name[0] in naam[:2]:
                    user_det.append(user)
                else:
                    # abort(404,messages={"This name is not present!!!....Sorry!"})   
                    print("bye") 
        

        print(user_det)
        return user_det
    


     

class Myfollowersname(Resource):
    @marshal_with(user_fields)
    def get(self,id):
        # data=follow_req.parse_args()
        # post=Post.query.filter_by(user_id=id).all()
        myfollowerid=Follow.query.filter_by(followed_id=id).all()
        temp=[]
            # user=[]
        for follower in myfollowerid:
                    
            user=User.query.filter_by(user_id=follower.follower_id).first()
            temp.append(user)
         
        print(temp)
        return temp
api.add_resource(Myfollowersname, "/myfollowername/<int:id>")

class Myfollowingname(Resource):
    @marshal_with(user_fields)
    def get(self,id):
       
        myfollowedid=Follow.query.filter_by(follower_id=id).all()
        temp=[]
            # user=[]
        for follower in myfollowedid:
                    
            user=User.query.filter_by(user_id=follower.followed_id).first()
            temp.append(user)
        
        print(temp)
        return temp
api.add_resource(Myfollowingname, "/myfollowingname/<int:id>")






class Login(Resource):
    def post(self):
        # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        args = login_user_parser.parse_args()
        print(args)
        # username = args.get("username" ,None)
        email_id = args.get("email_id" ,None)
        password = args.get("password" ,None)

        # if username is None: 
        #     return {
        #         "message" : "pls give username"
        #     } , 404

        if email_id is None:
            return {
                "message" : "pls give email_id also"
            } , 404
            
        if password is None:
           return {
                "message" : "pls give password also"
            } ,404     

        user = User.query.filter(User.email_id == email_id).first()
        if user:
            if(user.password == password):
                u_id = user.user_id
                return jsonify({
                    "firstname":user.firstname,
                    "lastname":user.lastname,
                    "deadline":user.deadline,
                    "gender":user.gender,
                    "email":user.email_id,
                    "password":user.password,
                    "user_id":u_id,
                    
                    "token" : jwt.encode({"email":
                    user.email_id, "iat": time.time(),"exp":time.time()+1800}, app.config['SECRET_KEY'])
  


                })
            else:
                abort(404, message="email_id or password not match")    

        else:
            abort(404, message="No user exists")
        
class all_user(Resource):
    
    @marshal_with(user_fields)
    # @cache.memoize(timeout=5)
    def get(self):
        # print("get userid", user_id)
        user_Det = User.query.all()
        
        print(user_Det)
        
        return user_Det
        
        

class userApi(Resource):
    # @token_required
    
    @marshal_with(user_fields)
    # @cache.memoize(timeout=5)
    def get(self, user_id):
        # print("get userid", user_id)
        user_Det = User.query.all()
        print(user_Det)
        print(user_Det[0].email_id)
        user = User.query.filter(User.user_id == user_id).first()
        # print(user)
        post = Post.query.all()
        # print(list)
        if user:
            return user
        else:
            return "", 4

class Feed(Resource):
    # @token_required
    # 
    @marshal_with(post_fields)
    # @cache.memoize(timeout=5)
    def get(self,id):
        
        
        postic = Post.query.all()
        fol = Follow.query.all()
        l = [id]
        # print(fol)
        for f in fol:
            # print(str(f.followed_id) +" "+ str(f.follower_id))
            if(f.followed_id == id):
                l.append(f.follower_id)
        # print(l) 
        post=[]       
        for p in postic:
            # p.user.firstname
            # print(post)
            if p.user_id in l:
                post.append(p)
            print(p.user_id)
        
        post = post[::-1]
        print(post)
        return post
        # else:
        #     return "", 4
class Register(Resource):

    def post(self):
        
            # print("post userid")
        # return {"user_id": "tune di hi kaha be"}
        args = create_user_parser.parse_args()
        firstname = args.get("firstname" ,None)
        lastname = args.get("lastname" ,None)
        email_id = args.get("email_id" ,None)
        password = args.get("password" ,None)
        deadline = args.get("deadline", None)
        gender = args.get("gender",None)
        print(gender)

        if firstname is None: 
            abort(404, message="pls give firstname")

        if lastname is None: 
            abort(404, message="pls give lastname")

        if email_id is None:
            abort(404, message="pls give email_id")
            
        if password is None:
            abort(404, message="pls give correct password")
        
        if deadline is None: 
            abort(404, message="pls give DOB")

        if gender is None: 
            abort(404, message="pls give Gender")    
        
        user = User.query.filter(User.email_id == email_id).first()
        if user:
            abort(404, message="sale dusplicate maal bhejta")  

        user = User.query.filter(User.firstname == firstname).first()
        if user:
            abort(404, message="bhai ye naam pehle se hai ")
            
        newuser = User(firstname = firstname,lastname = lastname, email_id = email_id, password=password, gender = gender, deadline = deadline)
        db.session.add(newuser)
        db.session.commit()
        return {
            "firstname":newuser.firstname,
            "lastname":newuser.lastname,
            "email":newuser.email_id,
            "password":newuser.password,
            "user_id":newuser.user_id,
            "deadline":newuser.deadline,
            "gender":newuser.gender,
            "token" : jwt.encode({"email":
             newuser.email_id, "iat": time.time(),"exp":time.time()+1800}, app.config['SECRET_KEY'])
        }
    
class ProfilePic(Resource):
    
    def get(self, id):

        user = User.query.filter(User.user_id == id).first()

        email = user.email_id

        dp = DP.query.filter(DP.email_id == email).first()

        return{
            "dp_name":dp.dp_name,
        }
    

    
    def post(self,id):
        args = dp_parser.parse_args()
        dp_name = args.get("dp_name" ,None)

        user = User.query.filter(User.user_id == id).first()
        email = user.email_id

        if dp_name is None or dp_name == "":
            # print("Image must have a file name")
            filename = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAIoAigMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABQYBAwQCB//EADsQAAIBAgMFBAYGCwAAAAAAAAABAgMEBREhEhMxQVEiI3GxBjJSYYGRFEJTodHhFSQzNUNicoKSwfD/xAAUAQEAAAAAAAAAAAAAAAAAAAAA/8QAFBEBAAAAAAAAAAAAAAAAAAAAAP/aAAwDAQACEQMRAD8A+4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAByXmIW1mu+n2stILVsjMWxrZcqFk9VpKp08CAlJyk5SbbfFt6sCYufSGtNtW9KMI9Zasj6mIXlXPbuavgnl5HMANm/rfbVP8ANnune3VP1Liqv7maABKUMdvKbW92KseeayfzRMWWM2t01By3VR/Vnz8GVMAX4FVwzGKtq1Trt1KPDXjHwLPSqwrU41KUlKElmmgPYAAAAAAABA4/ibjnaUJa/wASS5e4k8Tu1ZWc6um1wgnzZTZOUpOUnnJvNt82BgAAADfbWVxdPuaba5ybySA0AlFgdxlrVpJ9NTnucMurdbUobUfag8/u4gcYAAEjg+IuyrbFR9xN9r+V9SOAF9i1JJppprNNGSG9HLze0ZW032qXq++P5EyAAAAAAVr0muHK5p0E9Kcdp+L/AC8yGOnE6m9xC4ln9dpfDQ5gAAA7sKsvpdZuee6hrL3+4ssIxhFRglGK4JcEceDU1Tw+m0tZ5yf/AHwR2gAABC43h8YxdzQWX2kV5kKXOcFUhKElpJNP4lNlHZk10eQGAAB1YZcfRr6lU5bWzLwehdCgF5s6m9tKNR8ZQTfyA3AAAAAKLcPO4q/1y8zWb7+G7vq8OlR+ZoAGDJgCz4PVjPDqWusM4s7dqPUrOFXqtarjU/ZT4v2X1LKkpRTjJNPVNcwM7SfBmHJcnqFDmNlaLoB5dRQjKc2lFJv5FPlLak31eZM41ewUXbUZbTb7xrkuhCgZBgyALlhH7sts/YRTS7YdDd2FvHpTj5AdAAAAACq+kdHd4hvMuzVinn71o/8ARFlsx60d1ZNwWdSn2o5c+qKmAAJHDcMldZVarcaP3y8PxA4aNGpWns0oSm+kUd0P0lhq9WW76ZbUfyLBSpU6MNilBRiuSR7AgVj1RLWhBvrtM8TvsQv+xQjKMXx2F5sn3CDfqx+R6Wmi0QFSubO4tn31Npe1xXzNBdGk01JJp8UyGxHCItOraRyfF01z8PwAhAOGgA22lF3FzSor68kn4cy8JZLLoV/0atG5yuprRdmHjzZYQAAAAAAVXHMOdrWdalHuZvkvVfQtR4q0oVqcqdSKlCSyaYFQwuz+mXGUl3UNZvr0RZ0lGKjFJJaJI12tjCxpOFLNxcm23xNoAAAAAAAAEJjlio/rVKOSb7xLzI6xtJ3txGlDNLjKWXqotc6Kr05U5LsyWTPVhZUrKju6S1espPjJgbaFGFClClTWUYrJGwAAAAAAAAAAa5Uk9Y6M2ADncWuKPJ1GHFPikBzA6N3H2TKjFcEgOdJvgjZGl7T+BtAGEklojIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB//Z'
            # session['dp'] = filename
            # session['id'] = user.user_id
            add_dp = DP(dp_name=filename, email_id=email)
            db.session.add(add_dp)
            db.session.commit()
            return {
                "dp_name":add_dp.dp_name,
                
                "email":add_dp.email_id,
            }
        

        else:
            # filename = dp_name
            # session['dp'] = filename
            # session['id'] = user.user_id
            add_dp = DP(dp_name=dp_name, email_id=email)
            db.session.add(add_dp)
            db.session.commit()
            # dp_name.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            # print(session)
            return {
                "dp_name":add_dp.dp_name,
                
                "email":add_dp.email_id,
            }
            # return render_template("index.html", filename=filename)

class hehe_Comment(Resource):
    
    
    @marshal_with(comment_fields)
    def get(self,post_id):
        coms = Comment.query.filter_by(post_id = post_id).all()
        print(coms)
        return coms


    
    
    @marshal_with(comment_fields)
    def post(self,post_id):

        args= com_parser.parse_args()
        comment = args.get('comment')
        print(comment)
        user_id = args.get('user_id')
        # post = post.query.filter(Post.post_id == post_id).first()
        print(post_id)
        new_comment = Comment(comment = comment, user_id = user_id,post_id = post_id,comment_time = dt.now().strftime("%I:%M:%S %p %d-%b-%Y"))

        db.session.add(new_comment)
        db.session.commit()

        return new_comment


        
api.add_resource(hehe_Comment, "/api/<int:post_id>/comment") 


class hehe_like(Resource):

    # 
    # @marshal_with(post_fields)
    def get(self,u_id):
        u = []
        likes = Like.query.filter_by(user_id = u_id).all()
        print(likes)
        for like in likes:
            u.append(like.post_id)
        print(u)    
        return {
            "l":u
        }


    
    # 
    @marshal_with(like_fields)
    def post(self,u_id):

        args= like_parser.parse_args()
        post_id = args.get('post_id',None)
        print(post_id)
        user_id = args.get('user_id',None)
        # post = post.query.filter(Post.post_id == post_id).first()
        print(user_id)

        post = Post.query.filter(Post.post_id == post_id).first()

        like = Like.query.filter_by(post_id = post_id,user_id = user_id ).first()
        if like:
            db.session.delete(like)
            db.session.commit()

        else:
            likes= Like(user_id = user_id,post_id = post_id) 
            db.session.add(likes)    
            db.session.commit()
            return likes
        # new_comment = Comment(comment = comment, user_id = user_id,post_id = post_id)

        # db.session.add(new_comment)
        # db.session.commit()

        return "h gya bro"

       

        
api.add_resource(hehe_like, "/api/<int:u_id>/like") 


class PostApi(Resource):
    # @marshal_with(list_fields)
    
    def get(self, user_id, post_id):
        # print("get userid", user_id, list_id)
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            post = Post.query.filter_by(post_id = post_id, user_id = user_id).first()
            print(post)
            if post:
                return {
                    "post_id" : post.post_id,
                    "description" : post.description,
                    "image_name" : post.image_name,
                    "user_id" : post.user_id,
                    "time_created":post.time_created,
                    "username": user.firstname + " "+user.lastname ,
                # "token" : jwt.encode({"email":
                
                #  newuser.email_id, "iat": time.time(),"exp":time.time()+1800}, app.config['SECRET_KEY'])
               }
            else:
                # return "apke pass iss index pe list nhin hai ", 404
                abort(404,message="apke pass iss index pe list nhin hai")
        else:
                   
            abort(404,message="user not found")
        
    
    def put(self, user_id, post_id):
        # print("put userid", user_id)

        args = add_post.parse_args()
        desc = args.get("post_desc" ,None)
        # print(type(title))
        img = args.get("post_image" ,None)
        

        
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            post = Post.query.filter_by(post_id = post_id, user_id = user_id).first()

            
            if post :
                post.time_created = dt.now().strftime("%I:%M:%S %p %d-%b-%Y")
                if desc is None:
                    post.description = post.description
                else:
                    post.description = desc
        

                if img is None: 
                    post.image_name = post.image_name

                else:
                    post.image_name= img
            else:
                abort(404,message="Not founda list of that index")            
        # list = List(title = title, desc = desc, user_id= user_id)
        db.session.add(post)
        db.session.commit()
        return marshal(post,post_fields)


    
    def delete(self, user_id, post_id):
        # print("delt userid", user_id)
        post = Post.query.filter_by(post_id = post_id).delete()
        print("hello baby")

                  
        
        db.session.commit()
        

        return {
            "message" : "Successfully deleted"
        }, 200

    
    def post(self,user_id):
        
        user_id = int(user_id)
        args = add_post.parse_args()
        desc = args.get("post_desc" ,None)
        print(desc)
        create_post=dt.now().strftime("%I:%M:%S %p %d-%b-%Y")
     
        img = args.get("post_image" ,None)
        print(img)

        

        if desc is None: 
            abort(404, message="No title specified!, pls give first title ")


        if img is None: 
            img =""

        
        post = Post(image_name = img, time_created = create_post,description = desc, user_id= user_id)
        db.session.add(post)
        db.session.commit()
        return marshal(post,post_fields)




api.add_resource(Register, "/api/Register")   
api.add_resource(Login, "/api/Login") 
api.add_resource(all_user, "/api/users") 
api.add_resource(userApi, "/api/<int:user_id>") 
api.add_resource(Feed, "/api/<int:id>/feed") 
api.add_resource(ProfilePic, "/api/dp/<int:id>") 
api.add_resource(PostApi, "/api/<int:user_id>/add","/api/<int:user_id>/<int:post_id>") 
api.add_resource(Myfollowers, "/myfollowed/<int:id>")
api.add_resource(Follows, "/follow/<int:id>")
api.add_resource(Unfollows, "/unfollow/<int:id>")
api.add_resource(Myfollowing, "/myfollow/<int:id>")    
api.add_resource(Search,"/search/<name>")