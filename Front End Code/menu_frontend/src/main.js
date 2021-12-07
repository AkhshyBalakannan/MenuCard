import Vue from 'vue'
import App from './App.vue'
import NavBar from './components/navbar.vue'
import VueResource from 'vue-resource'
import VueCookie from 'vue-cookie'

Vue.component('app-navbar',NavBar);


Vue.use(VueResource);

// Require dependencies
// Tell Vue to use the plugin
Vue.use(VueCookie);

new Vue({
  el: '#app',
  render: h => h(App)
})
