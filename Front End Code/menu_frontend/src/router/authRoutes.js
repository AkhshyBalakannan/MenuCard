import Signin from '../components/signin.vue'
import MenuCard from '../components/menucard.vue'
import SignUp from '../components/signup.vue'
import Profile from '../components/profile.vue'
import SignOut from '../components/signout.vue'



import guest from './middleware/guest'
import auth from './middleware/auth'
import isAdmin from './middleware/isAdmin'
import middlewarePipeline from './middlewarePipeline'


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
    }
]
