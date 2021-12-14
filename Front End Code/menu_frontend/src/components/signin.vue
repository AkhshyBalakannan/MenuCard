<template>
  <div>
    <h1>SIGNIN PAGE</h1>
    <input type="text" v-model="user_data.username" placeholder="username" />
    <input
      type="password"
      v-model="user_data.password"
      placeholder="password"
    />
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
        .post(this.$store.getters.url + "/user/login", this.user_data)
        .then(function (data) {
          if (data.body.token) {
            this.user_token = data.body.token;
            this.$store.dispatch("troggle_on_auth");
            this.$cookie.set("token", this.user_token, 100);
            if (data.body.admin) {
              console.log(data.body.admin);
              this.$store.dispatch("troggle_on_admin");
            }
            this.$router.push("menucard");
          }
          console.log(data);
        });
    },
  },
};
</script>

<style>
</style>
