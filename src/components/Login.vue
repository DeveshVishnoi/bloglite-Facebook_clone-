<template>
    
      <main>
        <div class="row">
            <div class="col-logo">
                <!-- <img  class="logo" src="../assets/devbook.png" alt="Logo">
                 -->
                 <h1 class="logo"><i class="fa fa-laptop" aria-hidden="true" ></i>DevBook</h1>
                <h2>Devbook helps you connect and share with the people in your life.</h2>
            </div>
            <div class="col-form">
                <div class="form-container">
                    <input type="text" v-model="email_id" placeholder="Email address or phone number" required>
                    <input type="password" v-model="password" placeholder="Password" required>
                    <button class="btn-login" v-on:click="login">Login</button>
                    <!-- <a href="#">Forgotten password?</a> -->
                    <router-link to="/reg"
                    ><button type="button" class="btn-new">
                      Create New Account
                    </button></router-link>
                </div>
                <!-- <p><a href="#"><b>Create a Page</b></a> for a celebrity, brand or business.</p> -->
            </div>
        </div>
    </main>
</template>

<script>

export default {
  name:"Login",
  data(){
    return {
      email_id:"",
      password:"",
      link:"http://127.0.0.1:5000/"
    }
  },
  methods:{
    login(){
      if(this.email_id == "" || this.password == ""){
        alert("bhai sari imnformation toh de");
      }
      else{
        fetch(`${this.link}/api/Login` ,{
          method:'POST',
          headers:{"Content-Type": "application/json" },
          body:JSON.stringify({
            email_id:this.email_id,
            password:this.password
          })
        }).
        then((res) => {
          if(res.status == 404){
            return res.json();
          }

          if(!res.ok){
            throw new Error("something went wrong srom serverside")
          }

          return res.json();
        }).
        then((data) =>{
          if (data.message == "email_id or password not match") {
              alert("email_id or password not match");
            } else if (data.message == "No user exists") {
              alert("No user exists");
            } else {
               console.log(data.message);
               console.log(data);
              localStorage.setItem("user_info", JSON.stringify(data));
              localStorage.setItem("token", data.token);
              // localStorage.setItem("user_id", data.user_id);
              this.$router.push({ name: "hello" });
            }
        }).catch("galat hai behenchdo");
      }
    }
  }
}
</script>

<style>


  * {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.logo{
  color:blue;
  margin-left:30px
}
body {
    font-family: 'Poppins', sans-serif;
    background-color: #f0f2f5;
    color: #1c1e21;
}
.logo .fa{
  font-size: 40px;
}
main {
    height: 70vh;
    width: 100vw;
    position: relative;
    margin: 0 auto;
}

footer {
    height: 30vh;
    background-color: #ffffff;
}

.row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    max-width: 1000px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.col-logo {
    flex: 0 0 50%;
    text-align: left;
}

.col-form {
    flex: 0 0 40%;
    text-align: center;
}

.col-logo img {
    max-width: 300px;
}

.col-logo h2 {
    font: 26px;
    font-weight: 400;
    padding: 0 30px;
    line-height: 32px;
}

.col-form .form-container {
    background-color: #ffffff;
    border: none;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 8px 16px rgba(0, 0, 0, 0.1);
    margin-bottom: 30px;
    padding: 20px;
    max-width: 400px;
    margin-top:10rem;
}

.col-form .form-container input, .col-form .form-container .btn-login {
    width: 100%;
    margin: 5px 0;
    height: 45px;
    vertical-align: middle;
    font-size: 16px;
}

.col-form .form-container input {
    border: 1px solid #dddfe2;
    color: #1d2129;
    padding: 0 8px;
    outline: none;
}

.col-form .form-container input:focus {
    border-color: #1877f2;
    box-shadow: 0 0 0 2px #e7f3ff;
}

.col-form .form-container .btn-login {
    background-color: #1877f2;
    border: none;
    border-radius: 6px;
    font-size: 20px;
    padding: 0 16px;
    color: #ffffff;
    font-weight: 700;
    cursor: pointer;
}

.col-form .form-container a {
    display: block;
    color: #1877f2;
    font-size: 14px;
    text-decoration: none;
    padding: 10px 0 20px;
    border-bottom: 1px solid #dadde1;
}

.col-form .form-container a:hover {
    text-decoration: underline;
}

.col-form .form-container .btn-new {
    background-color: #42b72a;
    border: none;
    border-radius: 6px;
    font-size: 17px;
    line-height: 48px;
    padding: 0 16px;
    color: #ffffff;
    font-weight: 700;
    margin-top: 20px;
    cursor:pointer
}

.col-form p {
    font-size: 14px;
}

.col-form p a {
    text-decoration: none;
    color: #1c1e21;
    font-weight: 600;
}

.col-form p a:hover {
    text-decoration: underline;
}

.footer-contents {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
}

footer ol {
  display: flex;
  flex-wrap: wrap;
  list-style-type: none;
  padding: 10px 0;
}

footer ol:first-child {
  border-bottom: 1px solid #dddfe2;
}

footer ol:first-child li:last-child button {
  background-color: #f5f6f7;
  border: 1px solid #ccd0d5;
  outline: none;
  color: #4b4f56;
  padding: 0 8px;
  font-weight: 700;
  font-size: 16px;
}

footer ol li {
  padding-right: 15px;
  font-size: 12px;
  color: #385898;
}

footer ol li a {
  text-decoration: none;
  color: #385898;
}

footer ol li a:hover {
  text-decoration: underline;
}

footer small {
  font-size: 11px;
}
</style>