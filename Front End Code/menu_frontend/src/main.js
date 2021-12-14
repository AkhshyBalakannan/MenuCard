import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'
import router from './router/router'
import store from './store'
import navbar from './components/navbar.vue'

// Vue.component('app-navbar', NavBar);

Vue.use(VueResource);
Vue.use(VueCookie);

Vue.component('app-navbar', navbar)

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
