<template>
  <body class="main-bg">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-6">
          <div class="card shadow">
            <div class="card-title text-center border-bottom">
              <h2 class="p-3">SIGN UP</h2>
            </div>
            <form method="POST" @submit.prevent="signup">
              <div class="card-body">
                <div class="mb-4">
                  <validation-provider rules="required" v-slot="{ errors }">
                    <label for="username" class="form-label">Username</label>
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
                    <label for="email" class="form-label">Email</label>
                    <input
                      type="email"
                      v-model="user_data.email"
                      class="form-control"
                      id="email"
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
                <div class="mb-4">
                  <validation-provider rules="required" v-slot="{ errors }">
                    <label for="confirmpassword" class="form-label"
                      >Confirm Password</label
                    >
                    <input
                      type="password"
                      class="form-control"
                      id="confirmpassword"
                      v-model="user_data.confirm_password"
                    />
                    <span class="required_field_false">{{ errors[0] }}</span>
                  </validation-provider>
                </div>
                <div class="d-grid">
                  <button class="btn text-dark main-bg">SUBMIT</button>
                </div>
              </div>
            </form>
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
        cofirm_password: "",
      },
    };
  },
  methods: {
    signup: function () {
      if (this.password === this.confirm_password) {
        this.$http
          .post(this.$store.getters.url + "/user/new", this.user_data)
          .then((data) => {
            console.log(data);
            this.$router.push("signin");
          });
      } else {
        alert("Please Check Password");
      }
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
.required_field_false {
  color: red;
}
</style>
