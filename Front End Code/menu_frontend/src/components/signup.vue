<template>
  <div>
    <h1>SIGNUP PAGE</h1>

    <input type="text" v-model="user_data.username" placeholder="username" />
    <input type="email" v-model="user_data.email" placeholder="email" />
    <input
      type="password"
      v-model="user_data.password"
      placeholder="password"
    />
    <input type="password" placeholder="confirm password" />
    <button @click.prevent="signup">Sign UP</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data: {
        username: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    signup: function () {
      this.$http
        .post(this.$store.getters.url + "/user/new", this.user_data)
        .then((data) => {
          console.log(data);
          this.$router.push("signin");
        });
    },
  },
};
</script>

<style>
</style>
