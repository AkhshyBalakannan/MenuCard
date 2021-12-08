<template>
  <div>
    <app-navbar :current_user="current_user"></app-navbar>
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  data() {
    return {
      current_user: false,
    };
  },
  created(){
    if (this.$cookie.get("token")){
      this.current_user = true;
      }
      else{
        this.current_user= false
      }
    },
  beforeUpdate(){
    if (this.$cookie.get("token")){
      this.current_user = true;
      }
      else{
        this.current_user= false
      }
    },

};
</script>

<style>
</style>
