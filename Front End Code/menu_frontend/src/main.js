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

Vue.http.interceptors.push(function (request) {
  if (this.$store.getters.token) {
    request.headers.set('Authorization', this.$store.getters.token)
  }
});

import { ValidationProvider, extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';


Vue.component('validation-provider', ValidationProvider);

extend('required', {
  ...required,
  message: 'This field is required'
});

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
