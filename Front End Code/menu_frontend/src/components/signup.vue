<template>
  <div class="container">
    <form>
        <input type="text" placeholder="username" v-model="user_data['username']">
        <input type="email" placeholder="email" v-model="user_data['email']">
        <input type="password" placeholder="password" v-model="user_data['password']">
        <input type="password" placeholder="confirm_password" v-model="user_data['confirm_password']">
        <button @click.prevent="signup">submit</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data: {
        username: "",
        password: "",
        email: "",
      },
      user_token: "",
    };
  },
  created(){
    if (this.$cookie.get("login")){
      this.user_token = this.$cookie.get("login")
      console.log(this.user_token)
    }
  },
  methods: {
    signup: function () {
      console.log("checking");
      this.$http
        .post("http://127.0.0.1:5000/user/register", this.user_data)
        .then(function (data) {
          this.user_token = data.body.token;
          this.$cookie.set("login", this.user_token, date);
        });
    },
  },
};
</script>

<style>
</style>