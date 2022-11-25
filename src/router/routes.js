
const routes = [
	{
		path: '/',
		component: () => import('layouts/GraphLayout.vue'),
		children: [
			{ path: 'graph', component: () => import('pages/GraphPage.vue') }
		]
	},
	{
		path: '/content',
		component: () => import('layouts/ContentLayout.vue'),
		children: [
			{ path: '', component: () => import('pages/ContentPage.vue') },
			{ path: ':keys(.*)*', component: () => import('pages/ContentPage.vue') }
		]
	},
	{
		path: '/test',
		component: () => import('layouts/ContentLayout.vue'),
		children: [
			{ path: '', component: () => import('src/pages/TestPage.vue') },
			{ path: ':keys(.*)*', component: () => import('src/pages/TestPage.vue') }
		]
	},

	// Always leave this as last one,
	// but you can also remove it
	{
		path: '/:catchAll(.*)*',
		component: () => import('pages/ErrorNotFound.vue')
	}
]

export default routes
