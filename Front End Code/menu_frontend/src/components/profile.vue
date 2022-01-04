<template>
  <div>
    <div class="container mt-3">
      <div class="row d-flex justify-content-center">
        <div class="col-md-7">
          <div class="card p-3 py-4 profile-body">
            <div class="text-center">
              <img
                src="https://i.imgur.com/bDLhJiP.jpg"
                width="100"
                class="rounded-circle"
              />
            </div>
            <div class="text-center mt-3">
              <span class="bg-secondary p-1 px-4 rounded text-white"
                >ABC-MENUCARD</span
              >
              <h5 class="mt-3 mb-0">{{ user_data.username }}</h5>

              <div class="px-4 mt-3">
                <p class="fonts">{{ user_data.email }}</p>
              </div>
              <form method="post" @submit.prevent="updateProfile">
                <div class="update">
                  <h4>Update Profile</h4>
                  <small>Each updation needs password for verification</small>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <div class="row mt-2">
                      <div class="col">
                        <label for="username">Username : </label>
                      </div>
                      <div class="col">
                        <input
                          class="form-control px-4"
                          type="text"
                          v-model="user_data.username"
                          id="username"
                          required
                        />
                        <span class="required_field_false">{{
                          errors[0]
                        }}</span>
                      </div>
                    </div>
                  </validation-provider>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <div class="row">
                      <div class="col"><label for="email">Email :</label></div>
                      <div class="col">
                        <input
                          class="form-control px-4"
                          type="text"
                          v-model="user_data.email"
                          id="email"
                          required
                        />
                        <span class="required_field_false">{{
                          errors[0]
                        }}</span>
                      </div>
                    </div>
                  </validation-provider>
                  <validation-provider rules="required" v-slot="{ errors }">
                    <div class="row">
                      <div class="col">*Password :</div>
                      <div class="col">
                        <input
                          class="form-control px-4"
                          type="password"
                          v-model="user_data.password"
                          required
                        />
                        <span class="required_field_false">{{
                          errors[0]
                        }}</span>
                      </div>
                    </div>
                  </validation-provider>
                  <button
                    class="btn btn-primary px-4 ms-3 mt-2"
                    @click.prevent="updateProfile"
                  >
                    Update Profile Details
                  </button>
                  <button
                    class="btn btn-primary px-4 ms-3 mt-2"
                    @click.prevent="deleteProfile"
                  >
                    Delete Profile
                  </button>
                </div>
              </form>
            </div>
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
        username: "",
        email: "",
        password: "",
        public_id: "",
      },
    };
  },
  created() {
    this.$http
      .get(this.$store.getters.url + "/user/profile")
      .then(function (data) {
        this.user_data = data.body;
      });
  },
  methods: {
    updateProfile() {
      if ( !(
          this.user_data.email == "" ||
          this.user_data.password == "" ||
          this.user_data.username == ""
        )
      ) {
        this.$http
          .patch(this.$store.getters.url + "/user/update", this.user_data)
          .then((data) => {
            this.$router.go();
          });
      } 
      else {
        alert("Please Fill All Fields for Updations");
      }
    },
    deleteProfile() {
      this.$http
        .delete(
          this.$store.getters.url + "/user/delete/" + this.user_data.public_id,
          this.user_data
        )
        .then((data) => {
          if (
            !(
              this.user_data.email == "" ||
              this.user_data.password == "" ||
              this.user_data.username == ""
            )
          ) {
            this.$store.dispatch("troggle_off_auth");
            this.$store.dispatch("troggle_off_admin");
            this.$store.dispatch("delete_token");
            this.$router.push("/signin");
          } else {
            alert("Please Fill All Fields for Deleting Profile");
          }
        });
    },
  },
};
</script>

<style scoped>
.profile-body {
  background-color: rgb(255, 238, 217);
}

.card {
  border: none;
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  cursor: pointer;
}

.card:before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 4px;
  height: 100%;
  background-color: #e1bee7;
  transform: scaleY(1);
  transition: all 0.5s;
  transform-origin: bottom;
}

.card:after {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 4px;
  height: 100%;
  background-color: #8e24aa;
  transform: scaleY(0);
  transition: all 0.5s;
  transform-origin: bottom;
}

.card:hover::after {
  transform: scaleY(1);
}

.fonts {
  font-size: 15px;
}

.update button {
  border: 1px solid #8e24aa !important;
  background-color: #8e24aa;
  color: #fff;
  height: 40px;
}
</style>