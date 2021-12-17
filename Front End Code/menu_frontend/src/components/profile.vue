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
              <div class="update">
                <h4>Update Profile</h4>
                <small>Each updation needs password for verification</small>
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
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col"><label for="email">Email :</label></div>
                  <div class="col">
                    <input
                      class="form-control px-4"
                      type="text"
                      v-model="user_data.email"
                      id="email"
                    />
                  </div>
                </div>
                <div class="row">
                  <div class="col">*Password :</div>
                  <div class="col">
                    <input
                      class="form-control px-4"
                      type="password"
                      v-model="user_data.password"
                    />
                  </div>
                </div>
                <button
                  class="btn btn-primary px-4 ms-3 mt-2"
                  @click.prevent="updateProfile"
                >
                  Update Profile Details
                </button>
              </div>
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
      user_data: {},
    };
  },
  created() {
    if (this.$cookie.get("token")) {
      this.$http
        .get(this.$store.getters.url + "/user/profile")
        .then(function (data) {
          this.user_data = data.body;
        });
    } else {
      this.$router.push("/signin?next=" + this.$router.history.current.path);
    }
  },
  methods: {
    updateProfile() {
      this.$http
        .patch(
          this.$store.getters.url +
            "/user/update?t=" +
            this.$cookie.get("token"),
          this.user_data
        )
        .then((data) => {
          console.log(data);
          this.$router.go();
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