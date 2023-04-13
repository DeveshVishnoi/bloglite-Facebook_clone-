<template>
  <div>
    <div class="header">
      <div class="header__left">
        <img
        src="src\assets\images.jfif"
            alt=""
        />
        <div class="header__input">
          <span class="material-icons"> search </span>
          <input type="text" placeholder="Search Facebook" id="s_name"/>
        </div>
        <div class="header__input">
          <button class="search" v-on:click="search">Search</button>
          <!-- <span class="material-icons"> search </span>
          <input type="text" placeholder="Search Facebook" /> -->
          </div>
      </div>

      <div class="header__right">
        <router-link to="/add-post">
          <button class="btns">+ Add Post</button>
        </router-link>
        <button class="btns  red" v-on:click="logout">
          <i class="fa fa-sign-out" style="font-size:15px"></i>  Log Out
          </button>
        <div class="header__right">
          <router-link :to="'/' + this.user_id + '/profile'"
            ><div class="header__info">
              <img
                class="user__avatar"
                src="data:image/png;base64,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"
                alt=""
              />
              <h4>{{ username }}</h4>
            </div></router-link
          >
        </div>

        <!-- <span class="material-icons"> forum </span>
      <span class="material-icons"> notifications_active </span>
      <span class="material-icons"> expand_more </span> -->
      </div>
    </div>
    <!-- header ends -->

    <!-- main body starts -->
    <div class="main__body">
      <!-- sidebar starts -->
      <div class="side">
        <div class="sidebar">
          <router-link :to="'/' + this.user_id + '/profile'" style="text-decoration: none;color: rgb(7, 7, 171); "
            ><div class="sidebarRow">
              <img
                class="user__avatar"
                src="data:image/png;base64,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"
                alt=""
              />
              <h4>{{ username }}</h4>
            </div></router-link
          >

          <a style="text-decoration: none;color: rgb(7, 7, 171); "><div class="sidebarRow">
            <span class="material-icons"> import_contacts </span>
            <h4>Devbook helps you connect the people</h4>
          </div></a>

          <router-link to="/add-post" style="text-decoration: none;color: rgb(7, 7, 171); "
            ><div class="sidebarRow">
              <i class='fas fa-plus' style='font-size:30px;color:rgb(88,120, 255);'></i>
              <h4>Add Post</h4>
            </div></router-link
          >
          <router-link to="/users" style="text-decoration: none; color: rgb(7, 7, 171);"
            ><div class="sidebarRow" >
              <span class="material-icons"> groups </span>
              <h4>All User</h4>
            </div></router-link
          >

          

          <div v-on:click="export_post" class="sidebarRow" style="text-decoration: none;" id="webkit">
            <span class="material-icons">
              downloading
              </span>
            <h4>Export</h4>
          </div>

          <router-link to="/friends" style="text-decoration: none; color: rgb(7, 7, 171);"
            ><div class="sidebarRow" >
              
              <span class="material-icons"> group </span>
              <h4>My Friends</h4>
            </div></router-link
          >

          <!-- <div class="sidebarRow">
            <span class="material-icons"> video_library </span>
            <h4>Videos</h4>
          </div> -->

          <!-- <div class="sidebarRow">
            <span class="material-icons"> expand_more </span>
            <h4>More</h4>
          </div> -->
        </div>
      </div>
      <!-- sidebar ends -->

      <!-- feed starts -->
      <div class="feed">
      <div class="box-design post-div" v-for="(post, index) in posts[0]" :key="index">
        <div class="post-infarmation">
          <div>
            <div class="profil-ing-div post-profile-img">
            <a  id="profile-link">
              <img id="Profile_images" :src="post.user[0].dp[0].dp_name" >
            </a>
          </div>
          </div>
          <div class="post-three-dot">
            <h2><a  id="profile_name">{{ post.user[0].firstname }} {{ post.user[0].lastname }}
            </a></h2>
            <p>
              {{ post.time_created }}
              
            </p>

            
          </div>
        </div>

          <p class="post-hader-text" id="post_h_T">{{ post.description }}</p>
          <img id="post-image-12" class="post-images" :src="post.image_name" v-if="post.image_name"  >

        <div class="post-info-input">
          

        </div>

        <div class="actavite">
          <div class="lcs-btn lcs-btn_i" v-on:click="like_btn(post.post_id,user_id)">
            <div>
              <div  v-for="like in likes" :key='like'>
              <p id="likebtn" style="color:blue"  v-if="like == post.post_id">
                <i id="post-icon-btn_i" style="font-size:20px; " class="fa fa-thumbs-up"></i> 
                <span id="post-icon-text_i"> Like :{{post.like.length}}</span>
              </p>
              <!-- <p style="color:blue">
                <i id="post-icon-btn_i" style="font-size:20px; " class="fa">&#xf087;</i> 
                <span id="post-icon-text_i"> Like </span>
              </p> -->
              </div>
              
            </div>
          </div>
          <div class="lcs-btn" v-on:click="comment(post.post_id)">
            <p><i class="far fa-comment-alt"></i>  Comment : {{post.comment.length}}</p>
          </div>
          <div class="lcs-btn">
            <p><i class="fas fa-share"></i> Share</p>
          </div>
        </div>


        <div class="comment-site">
          
          <div class="comment-input">
            <input id="input" type="text" placeholder="Write a comment…" v-model="comments">
            
          </div>
          <div class="profil-ing-div">
            <button v-on:click="Post_comment(post.post_id)">Post</button>
          </div>
        </div>

      </div>
    </div>
    <div class="body" style="display:none">
      <div class="comment">
        <span style="display:flex;flex-direction:column-reverse"><span><h4 style="text-align:center">Comments : {{com.length}}</h4></span><span v-on:click='cut' class="cross"><button><i class="fas fa-times-circle"></i></button></span></span>
        <div  v-for="(c, index) in com" :key="index" >
          <p >{{ c.user[0].firstname }}{{ c.user[0].lastname }} : </p> <p class="usecom">{{c.comment}}</p>
        </div>
        
        
        
      </div>
    </div>


      

      <!-- feed ends -->

    </div>

    <!-- main body ends -->

    
  </div>
</template>

<script>
import "/src/assets/main.css"
export default {
  data(){
    return {
      isActive:false,
      user_id:JSON.parse(localStorage.getItem('user_info')).user_id,
      username:JSON.parse(localStorage.getItem("user_info")).firstname + " " + JSON.parse(localStorage.getItem("user_info")).lastname,
      posts:[],
      com:[],
      likes:[],
      likes_len:"",
      com_len:"",
      comments:"",
      link:"http://127.0.0.1:5000"
    }
  },
  // delimiters: ['${', '}'],
  methods:{



    like_btn(p_id,u_id){

      
          fetch(`${this.link}/api/${p_id}/like`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              sar_babu: localStorage.getItem("token"),
            },
            body: JSON.stringify({
              post_id: p_id,
              user_id: u_id,
            }),
          })
            .then((res) => {
              if (res.ok) {
                return res.json();
              } else if (res.status === 401) {
                throw new Error();
                // console.log(res);
              } else {
                // console.log(res);
              }
            })
            .then((data) => {
              console.log(data),
              this.all_like();
              // this.all_post();
              // this.all_comments(id);
              // this.$router.push({ name: "hello" });
              // document.querySelector('#input').value = null;
              // this.all_post();
            })
            .catch((err) => this.$router.replace({ name: "Login" }));

       
    },

    all_like(){
      fetch(`${this.link}/api/${this.user_id}/like`, {
        method: "GET",
        headers: { "sar_babu": localStorage.getItem("token"),},
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((res) => {
          
            
              this.likes = res.l;
              this.likes_len = res.l.length;
              console.log(res.l.length);
              console.log(this.likes_len);
              this.all_post();
              console.log(res);
              this.$router.push({ name: "hello" });
            
             
        })
        .catch((err) => this.$router.replace({ name: "Login" }));

    },

    logout(){
            // this.$store.commit('token_mutate', "");
            localStorage.clear();
            this.$router.replace({ name: "Login" });
        },
        cut(){
          if(document.querySelector(".body").style.display=='block'){
            document.querySelector(".body").style.display = "none";
          }
        },

    comment(id){
      if (document.querySelector(".body").style.display == "none") {
        document.querySelector(".body").style.display = "block";
        this.all_comments(id);
        // this.all_post()
      } else if (document.querySelector(".body").style.display == "block") {
        this.all_comments(id),
        this.all_post();
      }
    }  , 
    
    Post_comment(id){
      document.querySelector('#input').value = null;
      fetch(`${this.link}/api/${id}/comment`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          sar_babu: localStorage.getItem("token"),
        },
        body: JSON.stringify({
          comment: this.comments,
          user_id: this.user_id,
        }),
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
            // console.log(res);
          } else {
            // console.log(res);
          }
        })
        .then((data) => {
          // this.all_post();
          // console.log(data);
          // this.all_post();
          this.all_comments(id),
          this.all_post();
          // this.$router.push({ name: "hello" });
          // document.querySelector('#input').value = null;
        })
        .catch((err) => this.$router.replace({ name: "Login" }));
    },

    all_comments(id){
      fetch(`${this.link}/api/${id}/comment`, {
        method: "GET",
        headers: { "sar_babu": localStorage.getItem("token"),},
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((res) => {
          
            if(res.length != 0){
              
              this.com = res;
              this.com_len = this.com.length;
              console.log(res),
              this.all_post();
              this.$router.push({ name: "hello" });
            }
            else{
              // alert("Welcome to DevBook!, You have 0 Comments on this Posts , Thank You From DevBook Developer")
              this.com = res;
            }  
        })
        .catch((err) => this.$router.replace({ name: "Login" }));

    },
            
    all_post(){
      fetch(`${this.link}/api/${this.user_id}/feed`, {
        method: "GET",
        headers: { "sar_babu": localStorage.getItem("token"),},
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((res) => {
          // (this.email_id = res.email_id),
            // (this.username = res.username),
            // (this.password = res.password),
            // (this.user_id = res.user_id),
            if(res.length != 0){
              (this.posts.push(res));
              // this.posts[0] = this.posts[0].reverse();
              console.log(this.posts[0]);
            }
            else{
              alert("Welcome to DevBook!, You have 0 blogs , Pls create some Blogs and follow your friends. Thank You From DevBook Developer")
            }  
        })
        .catch((err) => this.$router.replace({ name: "Login" }));
    },
    del_post(id) {
      fetch(`http://127.0.0.1:5000/api/${this.user_id}/${id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "sar_babu": localStorage.getItem("token"),
        },
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((data) => {
          console.log(data);
          // this.get_user_details();
          this.all_post();

        })
        .catch((err) => {
          alert(err);
        });

    }, 
    export_post() {
      fetch("http://127.0.0.1:5000/api/export/" + this.user_id, {
        method: "GET",
        headers: { "x-access-token": localStorage.getItem("token") },
      })
        .then((res) => {
          if (res.ok) {
            return res.blob();
          } else if (res.status === 401) {
            throw new Error();
          }
        })
        .then((file) => {
          var a = document.createElement("a");
          a.href = window.URL.createObjectURL(file);
          a.download = `${this.user_id}_Det.csv`;
          a.click();
        });
    },
    search(){
        var name = document.querySelector('#s_name');
        console.log(name.value);
        this.$router.push({ path: `/${name.value}/search_user` });
    },
    Dp(){
      fetch(`${this.link}/api/dp/${this.user_id}`,{
        method:'GET',
        headers: { "sar_babu": localStorage.getItem("token"),},
        
      }).then((res) =>{
        if(res.status == 404){
          return res.json();
        }
        if(!res.ok){
          throw new error("something wromng from server");
           
        }
        return res.json();
      }).then((data) =>{
        localStorage.setItem('dp',data.dp_name)
        console.log(data);
      })
    }
    
  },
    
   
  
  

// Close the dropdown menu if the user clicks outside of it
  

  mounted() {
    this.all_post();
    this.Dp();
    this.all_like();
    // this.all_comments(id);
    
  },
  beforeMount() {
    this.Dp();
  },
};

</script>

<style>
/* Dropdown Button */

#webkit{
  color: rgb(7, 7, 171);
  
}




.cross button{
  float:right;
  cursor: pointer;
  padding:2px 4px;
}
.usecom{
  margin-top:5px;
  width:300px;
  padding:5px;
  
  max-height:100px;
  border-radius:4px;
  color:black;
  
  background-color: rgb(208, 211, 255);
  
}

.body{
  float:right;
  width:35;
  min-height:fit-content;
 
  max-height:100px;
  box-sizing: border-box;
}
.comment{
  border-radius: 5px;
  box-shadow: 0px 1px 2px #3335;
  background-color: #fff;
  padding: 10px;
  margin-bottom: 15px;
  margin-top:10px;
  padding: 10px;
  margin-left:30px;
  min-height:fit-content;
 overflow:scroll;
  max-height:600px;
  min-width:300px;
  
  
  

}

.btns {
  padding: 10px 10px;
  background-color: rgb(18, 228, 18);
  border-radius: 5px;
  margin-right: 15px;
  cursor:pointer;
  border:none;
}
.red_like {
  color: red
  
}
.red {
  background-color:red;
  color: white;
}

.fa {
  font-size: 25px;
  cursor: pointer;
  user-select: none;
}
.search{
  cursor:pointer;
  border:none;
}
#opt{
  border:none;
}
#opt:hover {
  color: blue;
}
.dropbtn {
  background-color: #a5cfeb;
  color: white;
  padding: 6px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.sidebar a h4{
  text-decoration: none;
}

.dropdown:hover #myDropdown {
  display: block;
}

/* Dropdown button on hover & focus */
.dropbtn:hover,
.dropbtn:focus {
  background-color: #2980b9;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
  float: right;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 120px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 5px 10px;
  text-decoration: none;
  display: block;
  cursor: pointer;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}

/* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
.show {
  display: block;
}
</style>