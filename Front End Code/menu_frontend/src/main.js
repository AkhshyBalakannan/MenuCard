import Vue from 'vue'
import App from './App.vue'
import NavBar from './components/navbar.vue'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'
import VueRouter from 'vue-router'

Vue.component('app-navbar', NavBar);


Vue.use(VueResource);

// Require dependencies
// Tell Vue to use the plugin
Vue.use(VueCookie);
Vue.use(VueRouter);

import Routes from './routes'

const router = new VueRouter({
  mode: 'history', // default mode : 'hash'
  routes: Routes
})

new Vue({
  el: '#app',
  render: h => h(App),
  router:router
})
