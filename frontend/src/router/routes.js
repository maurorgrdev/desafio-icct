
const routes = [
  {
    path: '/',
    component: () => import('pages/Auth/LoginIndex.vue')
  },
  {
    path: '/users',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/User/UserIndex.vue') },
      { path: 'create', component: () => import('pages/User/UserCreate.vue') },
      { path: 'edit/:usuario_id', component: () => import('pages/User/UserEdit.vue'), props: true},
      { path: 'profile/:usuario_id', component: () => import('pages/User/UserProfile.vue'), props: true},
    ]
  },
  {
    path: '/login',
    component: () => import('pages/Auth/LoginIndex.vue'),
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
