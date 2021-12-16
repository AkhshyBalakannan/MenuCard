import MenuCard from '../components/menucard.vue'
import Food from '../components/food.vue'
import Meal from '../components/meal.vue'
import Link from '../components/link.vue'
import mealEdit from '../components/mealEdit.vue'
import foodEdit from '../components/foodEdit.vue'


import auth from './middleware/auth'
import isAdmin from './middleware/isAdmin'


export default [
    {
        path: '/menucard',
        name: 'menucard',
        component: MenuCard,
        meta: {
            middleware: [
                auth
            ]
        },

    }, {
        path: '/food',
        name: 'dashboard.food',
        component: Food,
        meta: {
            middleware: [
                auth
            ]
        }
    }, 
    {
        path: '/food/edit',
        name: 'food.edit',
        component: foodEdit,
        meta: {
            middleware: [
                auth,
                isAdmin
            ]
        }
    },
    {
        path: '/meal',
        name: 'dashboard.meal',
        component: Meal,
        meta: {
            middleware: [
                auth
            ]
        }
    },
    {
        path: '/meal/edit',
        name: 'meal.edit',
        component: mealEdit,
        meta: {
            middleware: [
                auth,
                isAdmin
            ]
        }
    },
    {
        path: '/link',
        name: 'link',
        component: Link,
        meta: {
            middleware: [
                auth,
                isAdmin
            ]
        }
    }
]
