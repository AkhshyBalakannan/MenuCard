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
  beforeMount(){
    if (this.$cookie.get("token")){
      this.$router.push('/');
    }
  },
  methods: {
    signup: function () {
      console.log("Making Connection to server");
      this.$http
        .post("http://127.0.0.1:5000/user/new", this.user_data)
        .then(function (data) {
          console.log(data)
          this.user_token = data.body.token;
          this.$cookie.set("token", this.user_token);
        });
    },
  },
};
</script>

<style>
</style>