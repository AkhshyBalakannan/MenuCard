import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import authRoutes from './authRoutes'
import menuRoutes from './menuRoutes'

import Profile from '../components/profile.vue'
import Notfoundpage from '../components/notFoundPage.vue'

import auth from './middleware/auth'
import middlewarePipeline from './middlewarePipeline'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        ...authRoutes,
        ...menuRoutes,
        {
            path: '*',
            name: '404page',
            component: Notfoundpage,
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