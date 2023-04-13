<template>
    <div>
    <div id="navwrapper">
        <div id="navbar">
    
          <h1 class="logowrapper">Devbook</h1>
    
        </div>
      </div>
    
      <div id="contentwrapper">
        <div id="content">
    
          <div id="leftbod">
    
            <div class="connect bolder">
              Connect with friends and the
              world around you on Devbook.</div>
    
            <div class="leftbar">
              <!-- <img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xap1/t39.2365-6/851565_602269956474188_918638970_n.png" alt="" class="iconwrap fb1"/> -->
              <div class="fb1">
                <span class="rowtext">See photos and updates</span>
                <span class="rowtext2 fb1">from friends in News Feed</span>
              </div>
            </div>
    
            <div class="leftbar">
              <!-- <img src="https://fbcdn-dragon-a.akamaihd.net/hphotos-ak-xap1/t39.2365-6/851585_216271631855613_2121533625_n.png" alt="" class="iconwrap fb1"/> -->
              <div class="fb1">
                <span class="rowtext">Share what's new</span>
                <span class="rowtext2 fb1">in your life on your timeline</span>
              </div>
            </div>
    
    
    
    
          </div>
    
          <div id="rightbod">
            <div>
              <div class="signup bolder">Sign Up</div>
              <div class="free bolder">It's free and always will be</div>
    
              <div class="formbox">
                <input type="text" v-model="firstname" class="inputbody in1" placeholder="First name" >
                <input type="text" class="inputbody in1 fr" placeholder="Last name" v-model="lastname">
              </div>
              <div class="formbox">
                <input type="email" class="inputbody in2" placeholder="Email or mobile number" v-model="email_id">
              </div>
    
              <div class="formbox">
                <input type="text" class="inputbody in2" placeholder="New password" v-model="password">
              </div>
              <div class="formbox">
                <div class="bday">Birthday</div>
              </div>
              <div class="formbox">
                <span data-type="selectors">
                  <span>
                    <input type="date" id="deadline" v-model="deadline" required />
                  </span>
                  <div class="formbox mt1">
                    <span data-type="radio" class="spanpad">
                      <input type="radio" id="fem" v-model="gender" class="m0" value="female">
                      <label for="fem" class="gender">Female
                      </label>
                      <input type="radio" id="male" v-model="gender" class="m0" value="male">
                      <label for="male" class="gender">Male
                      </label>
                    </span>
                  </div>
                  <div class="formbox">
    
                  </div>
                  <div class="formbox">
                    <button type="submit" class="signbut bolder" v-on:click="signup">Sign Up</button>
                    <div>
                      if you are already register, then click the <router-link to="/">login</router-link> button
                    </div>
                  </div>
                </span>
              </div>
            </div>
          </div>
    
        </div>
    </div>
</div>  
</template>

<script>

export default {
    name: "Register",
    data(){

      return {
        link:"http://127.0.0.1:5000/",
        email_id:"",
        password:"",
        user_id:"",
        firstname:"",
        lastname:"",
        deadline:"",
        gender:"",

      };

    },
    methods:{
      signup(){
        console.log("hello beta");
        if (this.firstname != "" && this.email_id != "" && this.password != "" && this.deadline != "") {
        fetch(`${this.link}/api/Register`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            firstname: this.firstname,
            lastname:this.lastname,
            email_id: this.email_id,
            password: this.password,
            gender: this.gender,
            deadline:this.deadline,
          }),
        })
          .then((res) => {
            if (res.status === 404) {
              return res.json();
            }
            if (!res.ok) {
              throw new error("something wromng from server");
            }
            return res.json();
          })
          .then((data) => {
            if (data["message"] == "sale dusplicate maal bhejta") {
              alert("This Email_id is also used, pls try different email_id");
              this.$router.push({name:"Login"})
            }
            else{
              if(data["message"] == "bhai ye naam pehle se hai "){
                alert("pls use different firstname this nameis already used!!!")
                this.$router.push({name:"Reg"})

              }
              else{
                console.log(data);
                localStorage.setItem("token", data.token);
                localStorage.setItem("user_info",  JSON.stringify(data));
                this.$router.push({ name: "dp" });
              }  
            }

            
          });
      } else {
        alert("pls give all information!!");
        // we will handle for all case
      }
      }
    }
}
</script>
<style>

body {
  margin: 0;
  font-family: "Lucida Grande", tahoma, verdana, arial, sans-serif;
  line-height: 1.28;
  overflow:hidden;
}  

#navwrapper {
  width: 100%;
  height: 82px;
  background-color: blue;
}

#navbar {
  margin: 0 auto;
  width: 980px;
  height: 59px;
}

#contentwrapper {
  width: 100%;
  height: 606px;
  background-color: #edf0f5;
}

#content {
  margin: 0 auto;
  width: 980px;
  padding-top: 20px;
}

h1 {
  font-family: tahoma, verdana, arial, sans-serif;
  font-size: 38px;
  letter-spacing: 0.05px;
  margin: 0;
  color: #fff;
  -webkit-font-smoothing: antialiased;
}

.logowrapper {
  display: block;
  padding: 20px 0;
}

#button {
  position: relative;
  width: 45px;
  height: 18px;
  background-color: #5b72a9;
  border: 1px solid #999;
  border-color: #8b9dc3 #2f477a #29447e #1a356e;
  -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
  cursor: pointer;
  font-size: 11px;
  font-weight: bold;
  text-align: center;
  color: #fff;
}

.row1 {
  color: #fff;
  font-size: 11px;
  width: 164px;
  cursor: pointer;
}

.inputtext {
  border-color: #1d2a5b;
  margin: 0;
  width: 142px;
  border: 1px solid #bdc7d8;
  margin: 0;
  padding: 3px;
  background-color: #faffbd;
}

.row2 {
  color: #9daccb;
  font-size: 11px;
  width: 164px;
  cursor: pointer;
}

#leftbod {
  width: 565px;
  display: inline-block;
}

.connect {
  width: 409px;
  height: 72px;
  padding: 42px 0 24px;
  font-size: 26px;
  font-weight: 700;
  line-height: 36px;
  color: #333;
  display: inline-block;
}

.leftbar {
  padding-bottom: 10px;
  margin-top: 20px;
}

.iconwrap {
  margin-right: 20px;
  width: 55px;
}

.rowtext {
  font-size: 16px;
  font-weight: bold;
  color: #333;
}

.fb1 {
  display: inline-block;
  vertical-align: middle;
}

.rowtext2 {
  font-size: 15px;
  color: #666;
  margin-left: 10px;
}

#rightbod {
  display: inline-block;
  vertical-align: top;
  width: 399px;
  height: 200px;
  float: right;
}

.signup {
  font-size: 36px;
  -webkit-font-smoothing: antialiased;
  font-weight: 700;
  margin-bottom: 5px;
}

.bolder {
  font-family: "Open Sans", sans-serif;
  text-rendering: optimizelegibility;
  color: #333;
}

.free {
  font-size: 19px;
  margin-bottom: 20px;
}

.formbox {
  display: inline-block;
  width: 399px;
}

.inputbody {
  display: inline-block;
  font-size: 18px;
  padding: 8px 10px;
  border: 1px solid #bdc7d8;
  -webkit-border-radius: 5px;
  color: #333;
  margin-bottom: 10px;
}

::-webkit-input-placeholder {
  color: #999;
}

::-moz-placeholder {
  color: #999;
}

:-ms-input-placeholder {
  color: #999;
}

.in1 {
  width: 172px;
}

.in2 {
  width: 377px;
}

.fr {
  float: right;
}

.fl {
  float: left;
}

.bday {
  font-size: 19px;
  color: #141823;
  -webkit-font-smoothing: antialiased;
  margin-bottom: 5px;
  
}

.selectbody {
  display: inline-block;
  height: 30px;
  font-size: 13px;
  border: 1px solid #bdc7d8;
  -webkit-border-radius: 5px;
  color: #141823;
}

.why {
  font-size: 11px;
  color: #3b5998;
  width: 150px;
  margin-left: 10px;
  cursor: pointer;
}

.h:hover {
  text-decoration: underline;
}

.gender {
  font-size: 18px;
  color: #141823;
  cursor: pointer;
  padding: 0 10px 0 3px;
  margin-right: 4px;
  line-height: 18px;
  vertical-align: middle;
}

.spanpad {
  padding: 5px 0 5px 4px;
  display: inline-block;
}

.mt1 {
  margin-top: 15px;
}

.m0 {
  margin: 0;
}

.agree {
  font-size: 11px;
  color: #777;
  width: 316px;
  margin: 11px 0 11px;
}

.link {
  color: #3b5998;
  display: inline-block;
  cursor: pointer;
}

.signbut {
  font-size: 19px;
  font-weight: 700;
  letter-spacing: 1px;
  color: #fff;
  min-width: 194px;
  padding: 7px 20px;
  text-align: center;
  -webkit-border-radius: 5px;
  background: #42b72a;
  /* -webkit-box-shadow: inset 0 1px 1px #a4e388; */
  border: 1px solid;
  border-color: #42b72a;
  margin-top: 10px;
  margin-bottom: 10px;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
  cursor: pointer;
}

.signbut:hover {
  background-color: rgb(17, 145, 17);
}

.create {
  border-top: 1px solid #a0a9c0;
  color: #666;
  font-size: 13px;
  font-weight: bold;
  margin-top: 10px;
  padding-top: 15px;
}

#deadline {
  border: 1px solid #bdc7d8;
  border-radius: 5px;
  padding: 5px;
  font-family: "Lucida Grande", tahoma, verdana, arial, sans-serif;
}
</style>
