<template>
  <div>
    <component :is='component'></component>
  </div>
</template>

<script>
import Menucard from './components/menucard.vue'
import Food from './components/food.vue'
import Signup from './components/signup.vue'
import Signin from './components/signin.vue'

export default {
  name: "app",
  components:{
    'app-menucard': Menucard,
    'app-food': Food,
    'app-signup': Signup,
    'app-signin': Signin
  },
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
      component: 'app-signup'
    };
  },
};
</script>

<style>
</style>
