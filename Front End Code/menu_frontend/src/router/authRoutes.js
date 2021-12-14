import Signin from '../components/signin.vue'
import SignUp from '../components/signup.vue'
import SignOut from '../components/signout.vue'

import guest from './middleware/guest'

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
