import Signin from '../components/signin.vue'
import SignUp from '../components/signup.vue'
import SignOut from '../components/signout.vue'
import Profile from '../components/profile.vue'
import CrudUser from '../components/cruduser.vue'

import guest from './middleware/guest'
import auth from './middleware/auth'
import isAdmin from './middleware/isAdmin'

export default [
    {
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
        },
    },
    {
        path: '/users/edit',
        name: 'allUser',
        component: CrudUser,
        meta: {
            middleware: [
                auth,
                isAdmin
            ]
        },
    },
]
