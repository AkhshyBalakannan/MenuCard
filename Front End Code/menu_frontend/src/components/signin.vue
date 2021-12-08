<template>
  <div class="container">
    <form>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="email" class="col-form-label">Email</label>
        </div>
        <div class="col-auto">
          <input
            type="text"
            id="email"
            class="form-control"
            v-model="user_data['username']"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="password" class="col-form-label">Password</label>
        </div>
        <div class="col-auto">
          <input
            type="password"
            id="password"
            class="form-control"
            v-model="user_data['password']"
          />
        </div>
      </div>
      <div class="row g-3 align-items-center">
        <div class="col-auto">
          <label for="remember" class="col-form-label">Remember</label>
        </div>
        <div class="col-auto">
          <input
            type="checkbox"
            id="remember"
            v-model="user_data['remember']"
          />
        </div>
      </div>
      <div>
        <button @click.prevent="signin">submit</button>
      </div>
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
        remember: false,
      },
      user_token: "",
    };
  },
  beforeMount(){
    if (this.$cookie.get("token")){
      this.$router.push('/');
    }
    console.log()
  },
  methods: {
    signin: function () {
      console.log("Making Connection to server");
      this.$http
        .post("http://127.0.0.1:5000/user/login", this.user_data)
        .then(function (data) {
          let date = 1;
          if (this.remember == true) {
            date = 1000;
          }
          this.user_token = data.body.token;
          this.$cookie.set("token", this.user_token, date);
          if (this.$router.currentRoute.query.next){
            this.$router.push(this.$router.currentRoute.query.next)
          }
          else{
            this.$router.push('/')
          }
        });
    },
  },
};
</script>

<style>
</style>