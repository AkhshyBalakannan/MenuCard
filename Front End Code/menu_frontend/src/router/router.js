import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'

import Signin from '../components/signin.vue'
import MenuCard from '../components/menucard.vue'
import SignUp from '../components/signup.vue'
import Profile from '../components/profile.vue'
import SignOut from '../components/signout.vue'



import guest from './middleware/guest'
import auth from './middleware/auth'
import isAdmin from './middleware/isAdmin'
import middlewarePipeline from './middlewarePipeline'


Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [{
        path: '/signup',
        name: 'signup',
        component: SignUp,
        meta: {
            middleware: [
                guest
            ]
        }
    },
    {
        path: '/signin',
        name: 'signin',
        component: Signin,
        meta: {
            middleware: [
                guest
            ]
        }
    },
    {
        path: '/signout',
        name: 'signout',
        component: SignOut,
    },
    {
        path: '/profile',
        name: 'profile',
        component: Profile,
        meta: {
            middleware: [
                auth
            ]
        }
    }
    ]
})

router.beforeEach((to, from, next) => {
    if (!to.meta.middleware) {
        return next()
    }
    const middleware = to.meta.middleware

    const context = {
        to,
        from,
        next,
        store
    }


    return middleware[0]({
        ...context,
        next: middlewarePipeline(context, middleware, 1)
    })

})



export default router