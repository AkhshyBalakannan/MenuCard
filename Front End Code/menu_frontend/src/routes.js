import Food from './components/food'
import Menucard from './components/menucard'
import Signin from './components/signin'
import Signup from './components/signup'
import Signout from './components/signout'
import Profile from './components/profile'


export default[
    { path: '/food', component: Food },
    { path: '/menucard', component: Menucard },
    { path: '/signin', component: Signin },
    { path: '/register', component: Signup },
    { path: '/signout', component: Signout },
    { path: '/profile', component: Profile },
]