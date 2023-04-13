<script setup>
// import './assets/main.css'
import dp from './components/choose_dp.vue'
import Login from './components/Login.vue'
import Reg from './components/Register.vue'
import hello from './components/hello.vue'
import add_post from './components/add_post.vue'
import profile from './components/profile.vue'
import all_user from './components/all_user.vue'

import "/src/assets/main.css"
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
 <!-- <dp /> -->
 <!-- <Reg /> -->
 <div>
     <!-- <Login /> -->
     <!-- <add_post /> -->
     <!-- <all_user /> -->
     <!-- <profile /> -->
  <router-view />
  <!-- <hello /> -->
 </div>
</template>

<style >

</style>

<script>

// search = function(){
//         var name = document.querySelectorAll('#search_name');
//         console.log(name.value);
//         this.$router.push({ path: 'search_user' });
// }
</script>
