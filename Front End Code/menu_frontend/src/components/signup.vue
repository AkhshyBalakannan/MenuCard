<template>
  <body class="main-bg">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-6">
          <div class="card shadow">
            <div class="card-title text-center border-bottom">
              <h2 class="p-3">SIGN UP</h2>
            </div>
            <div class="card-body">
                <div class="mb-4">
                  <label for="username" class="form-label">Username</label>
                  <input
                    type="text"
                    v-model="user_data.username"
                    class="form-control"
                    id="username"
                  />
                </div>
                <div class="mb-4">
                  <label for="email" class="form-label">Email</label>
                  <input
                    type="email"
                    v-model="user_data.email"
                    class="form-control"
                    id="email"
                  />
                </div>
                <div class="mb-4">
                  <label for="password" class="form-label">Password</label>
                  <input
                    type="password"
                    v-model="user_data.password"
                    class="form-control"
                    id="password"
                  />
                </div>
                <div class="mb-4">
                  <label for="confirmpassword" class="form-label"
                    >Confirm Password</label
                  >
                  <input
                    type="password"
                    class="form-control"
                    id="confirmpassword"
                  />
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
                  <button class="btn text-dark main-bg" @click.prevent="signup">
                    SUBMIT
                  </button>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
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

<style scoped>
.main-bg {
  background-color: #dadada;
  margin: 2% 0% 0% 0%;
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
