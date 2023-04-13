import dp from './components/choose_dp.vue'
import Login from './components/Login.vue'
import Reg from './components/Register.vue'
import hello from './components/hello.vue'
import add_post from './components/add_post.vue'
import edit_post from './components/edit_post.vue'
import profile from './components/profile.vue'
import all_user from './components/all_user.vue'
import friends from './components/friends.vue'
import search_user from './components/search_user.vue'
import profile_frnds from './components/profile_frnds.vue'

import { createRouter, createWebHistory } from 'vue-router'


const routes = [
    { 
        name:'Login',
        component:Login,
        path:'/'
    },
    { 
        name:'friends',
        component:friends,
        path:'/friends'
    },
    { 
        name:'all_user',
        component:all_user,
        path:'/users'
    },
    { 
        name:'Reg',
        component:Reg,
        path:'/reg'
    },
    {
        name:'dp',
        component:dp,
        path:'/set_dp'
    },
    {
        name:'hello',
        component:hello,
        path:'/feed'
    },
    {
        name:'search_user',
        component:search_user,
        path:'/:str/search_user'
    },
    {
        name:'add_post',
        component:add_post,
        path:'/add-post'
    },

    {
        name:'profile',
        component:profile,
        path:'/:id/profile'
    }
    ,
    {
        name:'profile_frnds',
        component:profile_frnds,
        path:'/:id/profile_frnd'
    }
    ,
    {
        name:'edit_post',
        component:edit_post,
        path:'/:post_id/edit-post'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router