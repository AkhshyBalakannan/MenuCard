import MenuCard from '../components/menucard.vue'
import Food from '../components/food.vue'
import Meal from '../components/meal.vue'
import Link from '../components/link.vue'
import mealAddition from '../components/mealaddition.vue'
import foodAddition from '../components/foodaddition.vue'


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
        children: [{
            path: 'food',
            name: 'dashboard.food',
            component: Food,
            meta: {
                middleware: [
                    auth
                ]
            },
            children: [{
                path: 'add',
                name: 'food.add',
                component: foodAddition,
                meta: {
                    middleware: [
                        auth,
                        isAdmin
                    ]
                }
            }]
        },
        {
            path: 'meal',
            name: 'dashboard.meal',
            component: Meal,
            meta: {
                middleware: [
                    auth
                ]
            },
            children: [{
                path: 'add',
                name: 'meal.add',
                component: mealAddition,
                meta: {
                    middleware: [
                        auth,
                        isAdmin
                    ]
                }
            }]
        }]
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
