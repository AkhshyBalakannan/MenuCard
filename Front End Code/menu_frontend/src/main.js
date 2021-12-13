import Vue from 'vue'
import App from './App.vue'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'
import router from './router/router'
import store from './store'

// Vue.component('app-navbar', NavBar);

Vue.use(VueResource);
Vue.use(VueCookie);


new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
