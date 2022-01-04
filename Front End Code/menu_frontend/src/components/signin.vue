<template>
  <div class="main-bg">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-6">
          <div class="card shadow">
            <div class="card-title text-center border-bottom">
              <h2 class="p-3">Signin</h2>
              <div class="alert alert-warning" role="alert" v-if="message">
                {{ message }}
              </div>
            </div>
            <form method="post" @submit.prevent="signin">
              <div class="card-body">
                <div class="mb-4">
                  <validation-provider rules="required" v-slot="{ errors }">
                    <label for="username" class="form-label"
                      >Username/Email</label
                    >
                    <input
                      type="text"
                      v-model="user_data.username"
                      class="form-control"
                      id="username"
                    />
                    <span class="required_field_false">{{ errors[0] }}</span>
                  </validation-provider>
                </div>
                <div class="mb-4">
                  <validation-provider rules="required" v-slot="{ errors }">
                    <label for="password" class="form-label">Password</label>
                    <input
                      type="password"
                      v-model="user_data.password"
                      class="form-control"
                      id="password"
                    />
                    <span class="required_field_false">{{ errors[0] }}</span>
                  </validation-provider>
                </div>
                <!-- <div class="mb-4">
                      <input
                        type="checkbox"
                        class="form-check-input"
                        id="remember"
                      />
                      <label for="remember" class="form-label">Remember Me</label>
                    </div> -->
                <div class="d-grid">
                  <button class="btn text-dark main-bg" type="submit">
                    SUBMIT
                  </button>
                </div>
                <router-link class="offset-4" to="signup"
                  >Wanna Join Us</router-link
                >
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
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
      message: "",
    };
  },
  methods: {
    signin: function () {
      console.log("Making Connection to server");
      this.$http
        .post(this.$store.getters.url + "/user/login", this.user_data)
        .then(function (data) {
          if (data.body.token) {
            this.message = "";
            this.$store.dispatch("set_token", data.body.token);
            this.$store.dispatch("troggle_on_auth");
            if (data.body.admin) {
              this.$store.dispatch("troggle_on_admin");
            }
            this.$router.push("menucard");
          }
          else{
            this.message = "Please check User name or Password";
          }
        });
    },
  },
};
</script>

<style scoped>
.main-bg {
  background-color: #dadada;
  margin: 7% 0% 5% 0%;
}

input:focus,
button:focus {
  border: 1px solid #dadada;
  box-shadow: none;
}

.form-check-input:checked {
  background-color: #dadada;
  border-color: #dadada;
}

.card,
.btn,
input {
  border-radius: 0 !important;
}
</style>
