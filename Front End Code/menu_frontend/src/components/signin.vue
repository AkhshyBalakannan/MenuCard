<template>
  <div>
    <h1>SIGNIN PAGE</h1>
    <button @click="signin">click me</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data: {
        username: "admin",
        password: "password",
      },
      user_token: "",
    };
  },
  methods: {
    signin: function () {
      console.log("Making Connection to server");
      this.$http
        .post("http://127.0.0.1:5000/user/login", this.user_data)
        .then(function (data) {
          if (data.body.token) {
            this.user_token = data.body.token;
            this.$store.dispatch("troggle_on_auth");
            this.$cookie.set("token", this.user_token, 100);
          }
        });
    },
  },
};
</script>

<style>
</style>
