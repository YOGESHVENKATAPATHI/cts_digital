import { createRouter, createWebHistory }
    from 'vue-router'

import CoursesView
    from '../views/CoursesView.vue'

import ProfileView
    from '../views/ProfileView.vue'

const router = createRouter({

    history: createWebHistory(),

    routes: [

        {
            path: '/',
            component: CoursesView
        },

        {
            path: '/profile',
            component: ProfileView
        }

    ]

})

export default router